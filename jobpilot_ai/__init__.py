"""Top-level package for the `jobpilot_ai` job application assistant.

This package provides a modular architecture for:

- Discovering and aggregating job postings
- Parsing job descriptions into structured representations
- Generating and storing embeddings for semantic matching
- Planning CV optimization and ATS checks
- Discovering potential recruiter or contact information
- Generating personalized outreach emails
- Exposing a LangGraph-powered workflow and Streamlit UI

At this stage, modules only contain high-level documentation and
placeholders. Core logic and integrations will be added in later iterations.
"""

__all__ = [
    "job_finder",
    "job_parser",
    "embedding_matcher",
    "cv_optimizer",
    "ats_checker",
    "recruiter_finder",
    "email_generator",
]

