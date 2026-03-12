"""LangGraph workflow state model for jobpilot_ai.

Defines the shared state shape passed between workflow nodes.
All fields are optional (total=False) so nodes can update state incrementally.
"""

from typing import Any, TypedDict


class WorkflowState(TypedDict, total=False):
    """State container for the job application assistant LangGraph workflow.

    Nodes read and write these keys as the graph runs. Only keys that have
    been set by a previous node or the initial invocation are present;
    unset keys are absent rather than None.
    """

    # --- User input & discovery ---
    user_query: str
    """Natural language query from the user (e.g. job search, optimization request)."""

    jobs: list[dict[str, Any]]
    """Raw job listings from the job finder (before parsing or ranking)."""

    ranked_jobs: list[dict[str, Any]]
    """Jobs ordered by relevance (e.g. from embedding_matcher)."""

    selected_jobs: list[dict[str, Any]]
    """Subset of jobs the user or workflow has selected for focus."""

    job_description: str
    """Full text of the current job description (for parsing, ATS, email context)."""

    # --- CV paths & optimization ---
    cv_path: str
    """Path to the user's current CV file (e.g. .docx)."""

    optimized_cv_path: str
    """Path to the generated optimized/tailored CV for the current job."""

    # --- Skills & matching ---
    job_skills: list[str]
    """Skills or keywords extracted from the job description."""

    cv_skills: list[str]
    """Skills or keywords extracted from the user's CV."""

    missing_skills: list[str]
    """Skills present in the job but not (clearly) in the CV."""

    # --- ATS ---
    ats_score: float
    """ATS compatibility score for the current CV vs job (e.g. 0–100)."""

    # --- Recruiter & outreach ---
    recruiter_name: str
    """Name of the recruiter or hiring contact for the current job."""

    recruiter_email: str
    """Email address of the recruiter or hiring contact."""

    generated_email: str
    """Draft outreach email generated for the current context."""

    # --- Persistence ---
    application_record: dict[str, Any]
    """Stored application metadata (e.g. job id, status, dates) for DB or UI."""
