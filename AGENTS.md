# AGENTS.md

## Run / test
- `pip install -r requirements.txt`; `pytest -q`; `uvicorn app.main:app --reload`.

## IL5 uplift
- This repo is in an IL2->IL5 uplift; the org `il5-uplift` plugin's guardrails apply.
- Before any PR: run the `il5-local-verification` skill in `.agents/skills/`.
- Control inputs: `docs/il5/00-boundary.md` (inherited vs. code-owned, parameter values); remediate only units in `docs/il5/12-remediation-scope.csv`.
