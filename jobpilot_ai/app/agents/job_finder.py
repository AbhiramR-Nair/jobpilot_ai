"""Job discovery and collection module for `jobpilot_ai`.

Responsibilities (to be implemented later):

- Define abstractions for job sources (APIs, RSS feeds, web pages, manual input).
- Normalize job postings into a consistent internal representation.
- Support basic filtering (role, location, salary range, seniority, keywords).
- Provide hooks for persistence into the SQLite database.
- Expose a simple interface that the LangGraph workflow can call to
  retrieve candidate job postings for a given user profile.

This module is intentionally limited to structure and documentation at this
stage; no external integrations or business logic are implemented yet.
"""

