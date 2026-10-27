# Security findings summary - il5-uplift-demo (step 3a)

CUI // treat as CUI unless the ISSM says otherwise. Counts and locations only; no secret values. Implementation status, not a compliance determination.

Source file: `02-security-findings.json` (one array, `source`-tagged). Commit scanned: `il5/main` `ce1f179`. Scan register: `01-scan-register.md`.

## Counts per source by severity

| Source | Scan ID | Critical | High | Medium | Low | Total | Open | Suppressed |
|---|---|---|---|---|---|---|---|---|
| devin-security | scan-87996f1a24b348bfa10fbfa16f74bb7f | 0 | 3 | 1 | 4 | 8 | 7 | 1 |
| sonarqube | - (not available - no project) | - | - | - | - | 0 | 0 | 0 |

Open by severity: critical 0, high 3, medium 1, low 3. The suppressed item (CWE-209, low) was dismissed by the scan's own triage as a hygiene item; its SI-11 / G5 gap still needs a Register row.

## By CWE class (primary CWE)

| CWE | Class | Count |
|---|---|---|
| CWE-1392 | Default credentials | 1 |
| CWE-89 | SQL injection | 1 |
| CWE-321 | Hard-coded crypto key | 1 |
| CWE-798 | Hard-coded credentials | 1 |
| CWE-916 | Weak password hash | 1 |
| CWE-209 | Error info disclosure | 1 |
| CWE-307 | No auth-attempt limit | 1 |
| CWE-250 | Excess privilege | 1 |

## Overlap estimate
- Between sources: not applicable (only one source produced findings).
- Within devin-security (same file within 10 lines), for de-confliction: `app/main.py:44-52` is shared by the seeded-account finding (related location) and the login/lockout finding; `app/main.py:27-35` (audit helper) is near the stack-trace handler; `k8s/deployment.yaml:15-21` holds both the privileged-container and the committed token-secret findings; `app/auth.py:10-32` holds MD5 hashing and token verification (also a related location of the token-secret finding).

## Top findings (all 8, by severity) with file:line

| # | Severity | Status | CWE | Location | Title | Finding ID |
|---|---|---|---|---|---|---|
| 1 | high | new | CWE-1392 | `app/db.py:14-14` | Seeded default account with a weak password | sfind-2647d53325fa49519243f6d701ab8850 |
| 2 | high | new | CWE-89 | `app/db.py:23-26` | SQL injection in asset lookup | sfind-5c7b7171e8674100a127abbe1fe0f9b5 |
| 3 | high | new | CWE-321 | `k8s/deployment.yaml:19-21` | Token signing secret committed in plaintext lets anyone with repo access forge login tokens | sfind-49728a99fc644ef1b6eb34b07fef5de8 |
| 4 | medium | new | CWE-798 | `app/settings.py:4-4` | Hardcoded export API key gives anyone with repo access a full data dump | sfind-26befe282e82415fa22f0a2c4b951d46 |
| 5 | low | new | CWE-916 | `app/auth.py:10-12` | Unsalted MD5 password hashes and tokens that never expire | sfind-e7836101ac1942eeba8e1c0ebf22121b |
| 6 | low | suppressed | CWE-209 | `app/main.py:32-35` | Stack traces and error text returned to clients | sfind-aacad442895f4e1fb57f6165c7e26f53 |
| 7 | low | new | CWE-307 | `app/main.py:44-52` | Login takes passwords in the URL, has no lockout, and audit lines can be forged | sfind-3f4588d09080434c82dae59f9e9aa8a3 |
| 8 | low | new | CWE-250 | `k8s/deployment.yaml:15-18` | Container runs privileged as root | sfind-5041cbc2c178476cbb87355e2aea8eea |

## Runtime-validated
- `sfind-5c7b7171e8674100a127abbe1fe0f9b5` SQL injection (`app/db.py:23-26`): scan note reports a verified chain (token via seeded login or forged token, then full DB dump). Other findings are code-level; Normal effort does not runtime-validate each finding.

## Seeded gaps (00-boundary.md G1-G8) seen by this scan
- Found: G1 MD5 (auth.py), G2 hardcoded API key (settings.py), G3 no expiry/idle timeout (auth.py, same finding as G1), G4 SQLi (db.py), G5 stack trace (main.py, suppressed), G7 audit forging (part of login finding), G8 privileged pod / secret in env (deployment.yaml, Dockerfile).
- Not reported as a security finding: G6 DoD banner (expected from the Compliance scans, step 3b); G8 `latest` tag not called out separately.

## Excluded
- `tests/**`, `docs/**` (profile exclude_globs). In scope: `app/`, `k8s/`, `Dockerfile`, `requirements.txt`, root config files.

## Tools named but not run or ingested
- SonarQube: not available - no project for this repo in SonarCloud org `cog-gtm`; the MCP token was also rejected (Not authorized). No project or rules created, per ISSO.
