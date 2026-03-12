"""Logging setup helpers for jobpilot_ai.

Provides a centralized way to get module loggers and optionally
configure logging for the whole application. Reusable across all modules.
"""

import logging
import sys
from typing import Optional, TextIO


_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
_DATE_FMT = "%Y-%m-%d %H:%M:%S"

_root_logger_name = "jobpilot_ai"
_configured = False


def get_logger(name: str) -> logging.Logger:
    """Return a logger for the given module or component.

    Use the module __name__ when calling from a module so logs are
    clearly attributed, e.g. get_logger(__name__).

    Args:
        name: Logger name, typically __name__ of the calling module.

    Returns:
        A Logger instance. If setup_logging has been called, it will
        follow the configured level and format; otherwise it inherits
        from the root jobpilot_ai logger (or the default root).
    """
    if name.startswith(_root_logger_name):
        return logging.getLogger(name)
    return logging.getLogger(f"{_root_logger_name}.{name}")


def setup_logging(
    level: int | str = logging.INFO,
    stream: Optional[TextIO] = None,
    format_string: Optional[str] = None,
) -> None:
    """Configure logging for the jobpilot_ai package (idempotent).

    Call once at application startup (e.g. in app.py or __main__).
    Subsequent calls update the existing handler's level and format.

    Args:
        level: Logging level (e.g. logging.DEBUG, "INFO").
        stream: Where to send logs (default: sys.stderr).
        format_string: Log message format (default: time | level | name | message).
    """
    global _configured

    if isinstance(level, str):
        level = getattr(logging, level.upper(), logging.INFO)

    root = logging.getLogger(_root_logger_name)
    root.setLevel(level)

    if stream is None:
        stream = sys.stderr
    fmt = format_string or _FORMAT
    date_fmt = _DATE_FMT

    if not root.handlers:
        handler = logging.StreamHandler(stream)
        handler.setLevel(level)
        handler.setFormatter(logging.Formatter(fmt, datefmt=date_fmt))
        root.addHandler(handler)
    else:
        for h in root.handlers:
            h.setLevel(level)
            h.setFormatter(logging.Formatter(fmt, datefmt=date_fmt))

    _configured = True
