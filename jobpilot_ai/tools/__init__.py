"""Shared utility subpackage for `jobpilot_ai`.

The `tools` package groups cross-cutting helpers that can be reused by
multiple feature modules without introducing tight coupling.

Available modules:

- docx_utils: Read, write, and extract text from DOCX files (python-docx).
- text_utils: Basic text cleaning (whitespace, newlines).
- logging_utils: Centralized logging and get_logger.
- config: Configuration loading (placeholder).
"""

from .docx_utils import (
    extract_text_from_docx,
    read_docx,
    write_docx,
)
from .logging_utils import get_logger, setup_logging
from .text_utils import clean_text

__all__ = [
    "clean_text",
    "extract_text_from_docx",
    "get_logger",
    "read_docx",
    "setup_logging",
    "write_docx",
]

