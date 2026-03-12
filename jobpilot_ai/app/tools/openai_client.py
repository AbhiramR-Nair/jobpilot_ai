"""Reusable OpenAI client wrapper for `jobpilot_ai`.

This module centralizes OpenAI API usage so all agents/modules can share:

- Loading API keys from `.env` (via python-dotenv)
- Chat completions
- Embeddings generation
- Basic retry logic with exponential backoff for transient failures
- Basic logging

Design goals:

- Keep the surface area small and stable.
- Avoid binding the rest of the codebase to OpenAI SDK details.
- Provide sensible defaults while allowing per-call overrides.
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass
from typing import Any, Iterable, Optional

from dotenv import load_dotenv
from openai import OpenAI
from openai import APIConnectionError, APIError, APITimeoutError, RateLimitError

from .logging_utils import get_logger

log = get_logger(__name__)


_TRANSIENT_EXCEPTIONS: tuple[type[Exception], ...] = (
    RateLimitError,
    APIConnectionError,
    APITimeoutError,
    APIError,
)


@dataclass(frozen=True)
class RetryConfig:
    """Configuration for retry behavior."""

    max_retries: int = 4
    """Maximum number of retries after the first attempt."""

    base_delay_s: float = 0.5
    """Base delay in seconds for exponential backoff."""

    max_delay_s: float = 8.0
    """Maximum delay between retries in seconds."""

    jitter_s: float = 0.25
    """Random jitter added to delays to reduce thundering herd."""


class OpenAIClient:
    """Small wrapper around the OpenAI SDK client.

    Typical usage:

    - Create once at app start (Streamlit session, CLI command, or worker).
    - Reuse for chat and embeddings across modules.
    """

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        load_env: bool = True,
        retry: RetryConfig | None = None,
        default_chat_model: str = "gpt-4o-mini",
        default_embedding_model: str = "text-embedding-3-small",
    ) -> None:
        """
        Args:
            api_key: OpenAI API key. If omitted and `load_env=True`, the key
                is loaded from environment variable `OPENAI_API_KEY`.
            load_env: If True, calls `load_dotenv()` to load variables from a
                local `.env` file (no error if missing).
            retry: Retry configuration for transient API failures.
            default_chat_model: Default model name used for chat completions.
            default_embedding_model: Default model name used for embeddings.
        """
        if load_env:
            load_dotenv()

        self._client = OpenAI(api_key=api_key)
        self._retry = retry or RetryConfig()
        self._default_chat_model = default_chat_model
        self._default_embedding_model = default_embedding_model

    def chat(
        self,
        *,
        messages: list[dict[str, Any]],
        model: Optional[str] = None,
        temperature: float = 0.2,
        max_output_tokens: Optional[int] = None,
        **kwargs: Any,
    ) -> str:
        """Run a chat completion and return the assistant text.

        Args:
            messages: OpenAI chat messages, e.g.
                [{"role": "user", "content": "..."}].
            model: Model name override (defaults to `default_chat_model`).
            temperature: Sampling temperature.
            max_output_tokens: Optional maximum output tokens.
            **kwargs: Additional OpenAI SDK parameters (forwarded).

        Returns:
            The assistant message content as a string. If the response has no
            content, returns an empty string.
        """
        model = model or self._default_chat_model

        def _call() -> str:
            resp = self._client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_output_tokens=max_output_tokens,
                **kwargs,
            )
            content = (resp.choices[0].message.content or "") if resp.choices else ""
            return content

        return self._with_retries(_call, action=f"chat(model={model})")

    def embeddings(
        self,
        *,
        inputs: str | Iterable[str],
        model: Optional[str] = None,
        **kwargs: Any,
    ) -> list[list[float]]:
        """Generate embeddings for one or more inputs.

        Args:
            inputs: A single string or an iterable of strings.
            model: Model name override (defaults to `default_embedding_model`).
            **kwargs: Additional OpenAI SDK parameters (forwarded).

        Returns:
            A list of embedding vectors (list[float]), one per input.
        """
        model = model or self._default_embedding_model
        input_list = [inputs] if isinstance(inputs, str) else list(inputs)

        def _call() -> list[list[float]]:
            resp = self._client.embeddings.create(model=model, input=input_list, **kwargs)
            return [item.embedding for item in resp.data]

        return self._with_retries(_call, action=f"embeddings(model={model}, n={len(input_list)})")

    def _with_retries(self, fn, *, action: str):
        """Execute `fn` with retries for transient OpenAI errors."""
        attempts = 0
        while True:
            try:
                if attempts:
                    log.info(
                        "Retrying %s (attempt %s/%s)",
                        action,
                        attempts + 1,
                        self._retry.max_retries + 1,
                    )
                return fn()
            except _TRANSIENT_EXCEPTIONS as e:
                if attempts >= self._retry.max_retries:
                    log.exception("OpenAI call failed after retries: %s", action)
                    raise

                delay = min(self._retry.max_delay_s, self._retry.base_delay_s * (2**attempts))
                delay += random.uniform(0, self._retry.jitter_s)
                log.warning(
                    "Transient OpenAI error during %s: %s. Sleeping %.2fs",
                    action,
                    type(e).__name__,
                    delay,
                )
                time.sleep(delay)
                attempts += 1

