"""SQLite database access layer for `jobpilot_ai`.

This module is responsible for centralizing database-related concerns so
that the rest of the codebase can remain relatively storage-agnostic.

Planned responsibilities (to be implemented later):

- Define connection management helpers for the application's SQLite
  database (e.g., obtaining a connection, initializing schema).
- Describe logical tables and relationships, for example:
  - Jobs and parsed job metadata.
  - Candidates, CVs, and related documents.
  - Embedding records and references to FAISS index entries.
  - Recruiters/contacts and their association to jobs or companies.
- Provide simple CRUD-style interfaces that higher-level modules
  (`job_finder`, `job_parser`, `embedding_matcher`, etc.) can use
  without needing to know about SQL details.
- Keep the API flexible enough to evolve towards an ORM or alternative
  persistence layers if the project grows.

Currently this module only documents the database layer design. No
concrete schema definitions or queries have been implemented yet.
"""

