"""ATS-style checks and scoring module for `jobpilot_ai`.

Responsibilities (to be implemented later):

- Provide interfaces for evaluating how well a CV and/or cover letter
  aligns with a given job description from an ATS perspective.
- Perform checks such as:
  - Presence and density of key skills and keywords.
  - Alignment between required experience and stated experience.
  - Basic formatting and structure considerations that might affect
    parsing by common ATS systems.
- Expose a simple scoring and feedback model that:
  - Can be called from the LangGraph workflow.
  - Can be displayed in the Streamlit UI with human-readable guidance.
- Optionally coordinate with `cv_optimizer` to surface concrete
  suggestions for improvements.

Currently this module only defines intent and documentation; scoring
heuristics and LLM-assisted checks will be added in a later step.
"""

