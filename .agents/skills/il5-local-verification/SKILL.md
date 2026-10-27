---
name: il5-local-verification
description: Build, test, run and record the Mission Readiness Tracker (il5-uplift-demo) before any compliance PR is marked ready. Use before opening or updating any PR in this repo.
---

# Local verification for il5-uplift-demo

## Build and test
1. Install: `pip install -r requirements.txt`
2. Tests: `pytest -q` (3 tests, < 5 s). Pre-existing known failures: none.

## Run like production
3. Start: `TOKEN_SECRET=dev-only uvicorn app.main:app --host 127.0.0.1 --port 8000`
4. Ready signal: `curl -s http://127.0.0.1:8000/healthz` returns `{"ok":true}`
5. Container (optional): `docker build -t mrt:test . && docker run --rm -p 8000:8000 -e TOKEN_SECRET=dev-only mrt:test`

## Flows to exercise and record (add the ones the PR touches)
6. `GET /login` (banner text if implemented), `POST /login?username=operator&password=Password1` -> token; bad password -> 401; 3 bad passwords -> lockout if implemented.
7. `GET /assets/C-130J-01` with `Authorization: Bearer <token>` -> 200; `GET /assets/x' OR '1'='1` -> 404 (not a row) once SI-10 fix is in.
8. `GET /export` with and without `X-API-Key`; `GET /assets/does-not-exist` -> 404 JSON without a stack trace.
9. Check the audit log lines on stdout contain actor, action, object, source IP, UTC time, outcome once AU-3 fix is in.
10. Record the browser/curl session; save to `docs/il5/evidence/<unit-id>/`.

## Inherited / out of scope here
- Platform controls from AWS GovCloud / Platform One: SC-7, SC-28 at rest, tenant separation, kube-apiserver/etcd/kubelet STIG rules.
