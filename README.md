# jobpilot_ai

An **AI-powered job application assistant** that helps you:

- Discover relevant job postings
- Parse and analyze job descriptions
- Match roles against your profile using embeddings
- Optimize your CV for each role
- Run basic ATS-style checks
- Find recruiter contacts
- Generate tailored outreach emails

This repository currently contains **project structure and documentation stubs only**. Core logic and model integrations will be implemented later.

## Tech stack

- **Python**
- **LangGraph** for orchestrating assistant workflows
- **OpenAI API** for LLM-powered reasoning and generation
- **Streamlit** for the dashboard UI
- **SQLite** as the primary application database
- **FAISS** for similarity search over embeddings
- **python-docx** for CV and document handling

## High-level architecture

- **`jobpilot_ai/`**: Main Python package
  - **`job_finder.py`**: Locate and manage job listings
  - **`job_parser.py`**: Extract structured data from job descriptions
  - **`embedding_matcher.py`**: Build and query FAISS indexes for job/profile matching
  - **`cv_optimizer.py`**: Plan CV tailoring strategies per job
  - **`ats_checker.py`**: Run basic ATS-style checks on CVs and job matches
  - **`recruiter_finder.py`**: Model stubs for recruiter/contact discovery
  - **`email_generator.py`**: Email drafting/orchestration interfaces
  - **`workflow.py`**: LangGraph graph definition and node placeholders
  - **`db.py`**: SQLite database access layer
  - **`tools/`**: Shared utilities (configuration, logging, common types, etc.)
- **`app.py`**: Streamlit dashboard entrypoint

All Python modules currently expose **docstrings only** and do **not** implement behavior yet.

