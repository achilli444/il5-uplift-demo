# il5-uplift-demo (Mission Readiness Tracker) - authorization boundary and control ownership

## Boundary
- Repos / branches / deployables: `achilli444/il5-uplift-demo` @ `main`; one container image `mrt` built from `Dockerfile`, deployed by `k8s/deployment.yaml`.
- Platform / CSP (IL5 target): AWS GovCloud (US) EKS, Platform One Big Bang baseline (assumed for the demo).
- Data types: CUI (mission readiness status of named aircraft).

## Control ownership
| Family | Inherited (platform/CSP) | Organizational (policy/process) | Code-owned (this uplift) |
|---|---|---|---|
| AC | AC-17 (VPN/CAP) | AC-1, AC-2 account lifecycle | AC-3, AC-6, AC-7, AC-8, AC-11, AC-12 |
| AU | log storage/retention (CloudWatch/Loki) | AU-6 review | AU-2, AU-3, AU-3(1), AU-9, AU-12 |
| IA | DoD PKI / Keycloak IdP | IA-4 | IA-2(x), IA-5(1), IA-5(7), IA-11 |
| SC | SC-7, SC-28 at rest (KMS), tenant separation | | SC-8(1), SC-13, SC-23 |
| SI | | SI-4 monitoring | SI-10, SI-11, SI-15, SI-16, SI-2 |
| CM | cluster/kube-apiserver flags | CM-3 board | CM-5(6), CM-6, CM-7, CM-8 |
| SR / SA | | SR-1/2 | SR-3, SR-4, SR-11, SA-11, SA-15 |

## Applicable STIGs / SRGs (benchmarks from https://public.cyber.mil/stigs/downloads/ into docs/il5/catalog/)
| Document | Version / release | Applies to | Owner of non-code rules |
|---|---|---|---|
| DoD Cloud Computing SRG (IL5) | current | app config, crypto, PKI, banner, audit | platform (tenant separation, CAP/BCAP, physical) |
| Application Security and Development STIG | current | `app/`, `tests/` | - |
| Kubernetes STIG | current | `k8s/`, `Dockerfile` | platform team (apiserver/etcd/kubelet flags) |

## IL5 parameter values (ISSM, demo defaults)
- Idle timeout: 15 min; Lockout: 3 attempts / 15 min; Password: 15 chars min, 60-day max age, 24 history; Banner: standard DoD Notice and Consent Banner text; Audit fields: actor, action, object, source IP, UTC time, outcome; Retention: 1 year online.

## Baseline inventory (read-only, parent session step 1)
- System slug: `il5-uplift-demo`. Baseline: `main` @ `977214f9e95defb7075b11c74a610373711d4179`; uplift branch `il5/main`.
- Languages / frameworks: Python 3.12, FastAPI 0.115.6, uvicorn 0.32.1, SQLite (in-memory, stdlib `sqlite3`); tests: pytest 8.3.4 + httpx TestClient.
- Build / deploy: `requirements.txt` (pinned `==`, no hash-locked lockfile), `Dockerfile` (`python:3.12-slim`, tag not digest, runs as root), `k8s/deployment.yaml` (single Deployment, no Service/NetworkPolicy/RBAC). No CI workflows in the repo.
- Auth / session: `app/auth.py` (password hashing, HMAC-SHA256 bearer token issue/verify), `app/main.py` `login`, `require_token`; `app/settings.py` (API key, token secret, idle timeout).
- Crypto: `hashlib.md5` for passwords (`app/auth.py`), `hmac`/SHA-256 for tokens; no TLS termination in-app (platform ingress assumed).
- Logging / audit: `app/main.py` `audit()` via stdlib `logging` to stdout.
- Error handling: `app/main.py` `debug_exception_handler`.
- Data access: `app/db.py` (`find_asset` builds SQL by concatenation).
- IaC: `k8s/deployment.yaml` only; `Dockerfile`.
- Known gaps (seeded, see `app/main.py` docstring): G1 MD5 passwords, G2 hardcoded API key, G3 no idle timeout, G4 SQLi, G5 stack trace to client, G6 no DoD banner, G7 audit fields missing, G8 privileged pod / `latest` / secret in env.

## Scope note for reviewers
- IL5 vs. IL4 is mostly CUI sensitivity, NSS and tenant separation on the platform side (AWS GovCloud / Platform One, inherited). The code-level delta from IL2 is the 800-53 Rev 5 High enhancements (AC-2(x), AU-x(1), IA-2(x), SC-8(1), SC-28(1), SI-x) and the ASD / Kubernetes STIG rules checkable in this repo. This uplift does not "make the platform IL5"; it reports implementation status with evidence, and the AO decides.

## Approvers and evidence
- ISSO / ISSM / dev lead: Achal Amin. AO rep: not named.
- Evidence destination: `docs/il5/evidence/` in this repo.
