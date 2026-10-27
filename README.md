# il5-uplift-demo - Mission Readiness Tracker

Tiny FastAPI service with deliberately planted IL2-era gaps, used to exercise the `il5-uplift` Devin plugin
(IL2 -> IL5 runbook: SBOM, Security 2.0 + Compliance scans, de-confliction, remediation PRs, evidence).
See `app/main.py` docstring for the planted gaps (G1-G8) and `docs/il5/` for the uplift state.

Run: `pip install -r requirements.txt && uvicorn app.main:app --reload`  Test: `pytest -q`
