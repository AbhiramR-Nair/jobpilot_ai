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

- **`app/`**: Main application package
  - **`app/agents/`**: Capability modules (job finding, parsing, matching, CV optimization, ATS checks, recruiter discovery, email generation)
  - **`app/graph/`**: LangGraph workflow and shared state model
  - **`app/tools/`**: Shared utilities (OpenAI client, logging, DOCX and text helpers)
  - **`app/database/`**: SQLite database layer
  - **`app/ui/`**: Streamlit UI entrypoint
- **`data/`**: Local data folders (CVs, optimized CVs, cached jobs)
- **`tests/`**: Test suite placeholder

Most Python modules currently expose **docstrings and type hints only** and do **not** implement behavior yet.

