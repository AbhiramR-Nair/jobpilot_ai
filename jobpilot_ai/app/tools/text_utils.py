"""Basic text cleaning helpers for jobpilot_ai.

Reusable across modules for normalizing and cleaning extracted or
user-provided text before analysis or display.
"""

import re


def clean_text(
    text: str,
    *,
    normalize_whitespace: bool = True,
    strip: bool = True,
    collapse_newlines: bool = True,
    remove_empty_lines: bool = False,
) -> str:
    """Apply basic cleaning to a string.

    Args:
        text: Input text (e.g. from DOCX extraction or user input).
        normalize_whitespace: Replace runs of spaces/tabs with a single space.
        strip: Strip leading and trailing whitespace from the result.
        collapse_newlines: Replace multiple newlines with a single newline.
        remove_empty_lines: Drop lines that are empty or only whitespace.

    Returns:
        Cleaned text. Empty input returns "".
    """
    if not text:
        return ""

    if normalize_whitespace:
        text = re.sub(r"[ \t]+", " ", text)

    if collapse_newlines:
        text = re.sub(r"\n{2,}", "\n", text)

    if remove_empty_lines:
        text = "\n".join(line for line in text.splitlines() if line.strip())

    if strip:
        text = text.strip()

    return text

