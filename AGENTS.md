# Conventions
- `app/` is the package: `app.page()` builds the home page; `python -m app [port]` serves it on 127.0.0.1, port 8000 by default.
- The standard library only: add no dependency without asking.
- Tests live in `tests/`, one file per module, and import the package from the repository root.
- Check your work as the controller will: `python3.11 -m venv .venv`, `.venv/bin/pip install pytest==9.1.1 ruff==0.16.10`, then `.venv/bin/ruff check .` and `.venv/bin/python -m pytest -q`.
- `.venv/` and the caches are ignored: never commit them.
- `pyproject.toml`, `ruff.toml`, `AGENTS.md` and `.github/` are protected: a change to them waits for the owner.
