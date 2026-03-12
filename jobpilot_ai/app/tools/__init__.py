"""Shared utility subpackage for the jobpilot_ai app.

Available modules:

- docx_utils: Read, write, and extract text from DOCX files (python-docx).
- text_utils: Basic text cleaning (whitespace, newlines).
- logging_utils: Centralized logging and get_logger.
- openai_client: Reusable OpenAI wrapper (chat + embeddings + retries).
- config: Configuration loading (placeholder).
"""

from .logging_utils import get_logger, setup_logging
from .text_utils import clean_text

# Optional import: OpenAI SDK may not be installed yet.
try:
    from .openai_client import OpenAIClient, RetryConfig
except ModuleNotFoundError:  # pragma: no cover
    OpenAIClient = None  # type: ignore[assignment]
    RetryConfig = None  # type: ignore[assignment]

# Optional import: makes `import app.tools` work even before dependencies are installed.
try:
    from .docx_utils import extract_text_from_docx, read_docx, write_docx
except ModuleNotFoundError:  # pragma: no cover
    extract_text_from_docx = None  # type: ignore[assignment]
    read_docx = None  # type: ignore[assignment]
    write_docx = None  # type: ignore[assignment]

__all__ = [
    "clean_text",
    "extract_text_from_docx",
    "get_logger",
    "OpenAIClient",
    "read_docx",
    "RetryConfig",
    "setup_logging",
    "write_docx",
]

