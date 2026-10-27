# 03 - Compliance summary (il5-uplift-demo)

CUI // treat as CUI unless the ISSM says otherwise. Implementation status only; findings are gaps for de-confliction, not control determinations. The AO decides.

System `il5-uplift-demo` (Mission Readiness Tracker), `achilli444/il5-uplift-demo` @ `il5/main` `45da2de`. Exported 2026-10-27T09:02:06Z. Scans paused (cancelled, findings kept) by ISSO at 2026-10-27T09:02:06Z; the Kubernetes STIG scan had already completed.

Compliance page: Devin → Code Scans → Compliance → system `il5-uplift-demo` (scan summary links below).

| Catalog | Status | Criteria loaded | Excluded | Criteria with findings | Findings (H/M/L) | Scan |
|---|---|---|---|---|---|---|
| `nist-800-53-rev5-high` | partial - paused by ISSO at 2026-10-27T09:02:06Z | 33 | 5 | 22 of 33 | 17 (12/3/2) | [scan-b0d4def03df74cab9c8f66fb8b7316f9](https://devin-gtm.devinenterprise.com/code-scan/b0d4def03df74cab9c8f66fb8b7316f9/summary) |
| `dod-cc-srg-il5` | partial - paused by ISSO at 2026-10-27T09:02:06Z | 12 | 6 | 12 of 12 | 53 (34/9/10) | [scan-c3960b3b4c884acf90dcf6931f910461](https://devin-gtm.devinenterprise.com/code-scan/c3960b3b4c884acf90dcf6931f910461/summary) |
| `asd-stig-v6r5` | partial - paused by ISSO at 2026-10-27T09:02:06Z | 161 | 125 | 0 of 161 | 0 (0/0/0) | [scan-c8e52e9e2081421ea05148d95868147e](https://devin-gtm.devinenterprise.com/code-scan/c8e52e9e2081421ea05148d95868147e/summary) |
| `kubernetes-stig-v2r6` | completed (before ISSO pause) | 8 | 84 | 5 of 8 | 2 (1/0/1) | [scan-63e0dadf072843d78ef6f9b5515c55f8](https://devin-gtm.devinenterprise.com/code-scan/63e0dadf072843d78ef6f9b5515c55f8/summary) |

Criteria evaluated vs. total for paused scans is not reported by the scan API; "criteria with findings" is a lower bound. ASD STIG V6R5 produced 0 findings before the pause, so it is effectively not yet evaluated - re-run with `scan_new_commits`/a new scan before relying on it.

## nist-800-53-rev5-high

By control family: AC 2, AC,CM,SI 1, AC,IA 2, AU 3, CM,IA 2, CM,IA,SC 1, CM,SR 1, IA,SC 1, SA 1, SC 1, SI 2

- [high] Bulk CUI export, token failures and server errors generate no audit records (AU-12, AU-2, AU-3) `sfind-f6b60b7f9fb743328283bef8b5716bfb`
- [high] Login endpoint has no unsuccessful-attempt limit or account lockout (AC-7) `sfind-ecc89cb0f7504931be4965ba9ac81cb4`
- [high] Global exception handler returns exception text and full traceback to clients (SI-11) `sfind-deb5aa96a0f6457ab882fc366750060a`
- [high] Token signing secret falls back to a known default value (CM-6, IA-5, SC-23) `sfind-d61fd21d9b2c4413bf1c124f4fe86ab0`
- [high] /export authorizes bulk CUI access by a shared static key, no user identity (AC-3, AC-6, IA-2) `sfind-b937e9a720544d689205b0e71d2a2249`
- [high] Container runs privileged as root with no hardening securityContext (AC-6, CM-6, CM-7, SI-16) `sfind-b768e4998357491492457a89f37ecc32`
- [high] Export API key hardcoded as a literal in source (CM-6, IA-5) `sfind-8e211180972c483791bf198517421c86`
- [high] Passwords submitted as URL query parameters, exposed in access logs (IA-5, SC-8) `sfind-8cfe61720de749868329ff77d5dfc0be`
- [high] Token signing secret committed as plaintext env value in manifest (CM-6, IA-5) `sfind-7cc6bb1419c04cefaa63ec4acf5a3ef7`
- [high] Audit records lack timestamp, source IP, actor and outcome fields (AU-3) `sfind-736ff286775847a7b1a5a0ec19b663d3`
- [low] Container exposes plain HTTP port 8000; TLS left to platform ingress (SC-8) `sfind-6c84f2c15ef84e5f81059e0cb4adaf32`
- [medium] Test suite covers only happy paths; no security regression tests or CI (SA-11, SA-15) `sfind-69577cac47814440a0ddc056c868eccd`
- [low] Audit records written to stdout via stdlib logging, storage handed to platform (AU-9) `sfind-5355279be4f442fcbc62af672cf2bb72`
- [medium] Deployment pulls image by mutable :latest tag, not digest (CM-6, SR-11, SR-3) `sfind-3328f386be164cecb894f0da16e0d6eb`
- [high] Session idle timeout unset and never enforced; tokens never expire (AC-11, AC-12, IA-11, IA-2) `sfind-209d1d2861c24d44a9dda7ed8438927f`
- [high] Asset path parameter reaches concatenated SQL without validation (SI-10) `sfind-1d5461de0ff2411cafce9d2419732d18`
- [medium] Login page shows no DoD Notice and Consent Banner before authentication (AC-8) `sfind-0fe0427f43d049809330266730c47ce4`

Out of scope (for ISSO): see `docs/il5/catalog/nist-800-53-rev5-high-excluded.csv` (5 items).

## dod-cc-srg-il5

By SRG requirement: SRG-IL5-AUDIT-CONTENT 4, SRG-IL5-AUDIT-CONTENT,SRG-IL5-BANNER,SRG-IL5-CRYPTO,SRG-IL5-CUI,SRG-IL5-SECRETS,SRG-IL5-SESSION 2, SRG-IL5-AUDIT-CONTENT,SRG-IL5-PKI,SRG-IL5-PRIV-ACCESS,SRG-IL5-SECRETS 1, SRG-IL5-AUDIT-RETENTION 3, SRG-IL5-BANNER 3, SRG-IL5-CRYPTO 2, SRG-IL5-CRYPTO,SRG-IL5-PASSWORD 1, SRG-IL5-CUI 8, SRG-IL5-LOCKOUT 3, SRG-IL5-PASSWORD 1, SRG-IL5-PASSWORD,SRG-IL5-SECRETS 1, SRG-IL5-PKI 3, SRG-IL5-PKI,SRG-IL5-PRIV-ACCESS 2, SRG-IL5-PRIV-ACCESS 2, SRG-IL5-SECRETS 9, SRG-IL5-SESSION 5, SRG-IL5-TRANSIT 3

- [medium] CUI asset and export JSON responses carry no CUI marking (SRG-IL5-CUI) `sfind-e6eef08956854d2893efc6a950ba996a`
- [high] No logout/revocation and require_token never checks token age (AC-11, AC-12, SC-23, SRG-IL5-SESSION) `sfind-d2baf3e161e04548928a15a2672fd1e2`
- [high] audit() records lack actor, source IP, UTC time and outcome; events unaudited (AU-12, AU-2, AU-3, SRG-IL5-AUDIT-CONTENT) `sfind-c295e6616dc443618872759835d35844`
- [medium] Password accepted as URL query parameter on POST /login (IA-5, SRG-IL5-SECRETS) `sfind-be3f190daf744b7e99c730705c742059`
- [low] Module docstring planted-gap register (G1-G8) (AC-11, AC-12, AC-8, AU-12, AU-3, CM-5, IA-5, SC-13, SI-10, SI-11, SR-3, SRG-IL5-AUDIT-CONTENT, SRG-IL5-BANNER, SRG-IL5-CRYPTO, SRG-IL5-CUI, SRG-IL5-SECRETS, SRG-IL5-SESSION) `sfind-9c07aca070fa46b48baf3db2435db84c`
- [high] Login has no failed-attempt counting or account lockout (AC-7, SRG-IL5-LOCKOUT) `sfind-99cceb585d9541e399767d672d536777`
- [high] /export authenticates by shared static API key with no user identity (SRG-IL5-PKI, SRG-IL5-PRIV-ACCESS) `sfind-960e6b3abb954a1abba8e742748c71ae`
- [low] Container exposes plain port 8000 with no Service/TLS in repo (SRG-IL5-TRANSIT) `sfind-8fe792c9ca06460db93af8dfab60910b`
- [high] Global exception handler returns exception text and traceback to clients (SRG-IL5-CUI) `sfind-7f81e912cfe64e5d91285e04694d9081`
- [high] POST /login uses local username/password, not DoD PKI/CAC (IA-2, SRG-IL5-PKI) `sfind-7f41c93945ce41ee8bbe556e729d9adc`
- [high] Export API key hard-coded as a literal in settings.py (IA-5, SRG-IL5-SECRETS) `sfind-7c727129093245ecb173c491301989be`
- [high] GET /login returns no DoD Notice and Consent Banner or acknowledgement (AC-8, SRG-IL5-BANNER) `sfind-761247cb324d4ebc98a3c1ea67722244`
- [high] TOKEN_SECRET falls back to hard-coded default 'change-me' (SRG-IL5-SECRETS) `sfind-6b9a0d298dac4eb1a29bc78614163a87`
- [low] Container securityContext privileged:true and runAsUser:0 (SRG-IL5-PRIV-ACCESS) `sfind-64a3fe7877b048898e8b4a846edf2d32`
- [high] SESSION_IDLE_MINUTES set to None; idle timeout never configured (SRG-IL5-SESSION) `sfind-505bad0e0e334dc3afa5a7154772add6`
- [high] Deployment sets TOKEN_SECRET as plaintext env value in manifest (SRG-IL5-SECRETS) `sfind-4c32d871862f401f9649464029e813c7`
- [low] Audit logging via logging.basicConfig to process stream (SRG-IL5-AUDIT-RETENTION) `sfind-14650026afae4c44b68502714dbe4892`
- [medium] users schema has no password age, history, or length enforcement (SRG-IL5-PASSWORD) `sfind-f7b04b70a5bb4057be5b79b23fbefd75`
- [high] Login has no failed-attempt counting or account lockout (AC-7, SRG-IL5-LOCKOUT) `sfind-f133bb95bf084949b91c51a42dd6e1de`
- [low] HMAC-SHA256 token signing with constant-time verification (SRG-IL5-CRYPTO) `sfind-e9c347b5c4524fa0a8ffd5ff8e9d1594`
- [low] stdlib logging basicConfig to stdout for audit records (SRG-IL5-AUDIT-RETENTION) `sfind-e8556a697e75414d87163576cab74547`
- [high] Global exception handler returns exception text and traceback to client (SRG-IL5-CUI) `sfind-e355037213e24a7a943c5b0a90804cb8`
- [high] find_asset concatenates input into SQL on the CUI assets table (SRG-IL5-CUI) `sfind-daed553023f746f3a810b8cf1c8df1da`
- [medium] Runtime image python:3.12-slim provides no FIPS-validated crypto module (SRG-IL5-CRYPTO) `sfind-ac194bbcc8c54053991ca58bdba0c9d8`
- [high] audit() records omit actor, source IP, UTC timestamp and outcome (AU-3, SRG-IL5-AUDIT-CONTENT) `sfind-8161f3a1753c4c2584317f8f6a2d8d49`
- [high] Local username/password login instead of DoD PKI/CAC via IdP (IA-2, SRG-IL5-PKI) `sfind-8076de51666a4ffc8fdc5235c7822a34`
- [medium] asset_read audit writes requested asset name into logs (SRG-IL5-CUI) `sfind-77fe55fe74ff4a1a9196cac7c1a0b941`
- [high] /export guarded only by shared hard-coded API key, no role check (SRG-IL5-AUDIT-CONTENT, SRG-IL5-PKI, SRG-IL5-PRIV-ACCESS, SRG-IL5-SECRETS) `sfind-73c87b82723440aeaf58734ef37eeeeb`
- [medium] uvicorn serves plaintext HTTP on 0.0.0.0 with no in-repo TLS termination (SRG-IL5-TRANSIT) `sfind-5f4814191cf746b9ad8ff28921d57849`
- [high] Seeded 'operator' account with literal weak password Password1 (SRG-IL5-PASSWORD, SRG-IL5-SECRETS) `sfind-44adba2dc1034e1fb670ea5155207fea`
- [high] Asset and export JSON responses carry no CUI marking (SRG-IL5-CUI) `sfind-4391e59747894fca90df2471b2d1c339`
- [high] GET /login returns no DoD Notice and Consent Banner (AC-8, SRG-IL5-BANNER) `sfind-3e66ecd6dae94fdcbd43e3fe1108cead`
- [medium] Token rejections, failed lookups and exports emit no audit record (AU-3, AU-6, SRG-IL5-AUDIT-CONTENT) `sfind-3d770b342d214f3cb328ba27f4a4ea71`
- [high] Bearer tokens never expire; no idle timeout or logout revocation (SRG-IL5-SESSION) `sfind-3629a945f30e44ffa7a56ca67045ea21`
- [high] Token signing key falls back to literal default 'change-me' (SRG-IL5-SECRETS) `sfind-22d267ce2c4342278086b0d487c0518e`
- [high] Passwords stored as unsalted MD5 hashes (SRG-IL5-CRYPTO, SRG-IL5-PASSWORD) `sfind-12da8fbcddaa479aa8e1027228eea944`
- [medium] CUI asset and export JSON responses carry no CUI marking (SRG-IL5-CUI) `sfind-f85d21757c3042f3a10cadda155d8804`
- [high] TOKEN_SECRET falls back to hard-coded default 'change-me' (SRG-IL5-SECRETS) `sfind-f7f4adf7ccae4e9096f1d7ceee26e3d9`
- [high] /export authenticates by shared static API key with no user identity (SRG-IL5-PKI, SRG-IL5-PRIV-ACCESS) `sfind-e8d72597a018434c80f5fb2b3f12e039`
- [low] Container securityContext privileged:true and runAsUser:0 (SRG-IL5-PRIV-ACCESS) `sfind-e4ff744dd2024f258c7d5130dc328cb6`
- [high] Export API key hard-coded as a literal in settings.py (IA-5, SRG-IL5-SECRETS) `sfind-e4b9785ac3214b8d91e1e90c99ce728e`
- [medium] Password accepted as URL query parameter on POST /login (IA-5, SRG-IL5-SECRETS) `sfind-d8140ebef3824a89bf79bd43858dab4f`
- [low] Audit logging via logging.basicConfig to process stream (SRG-IL5-AUDIT-RETENTION) `sfind-c598331cedac4ffe9c909aca7f0782e6`
- [high] Deployment sets TOKEN_SECRET as plaintext env value in manifest (SRG-IL5-SECRETS) `sfind-aa7b37083afc4ace99fbdb71081b5f52`
- [low] Container exposes plain port 8000 with no Service/TLS in repo (SRG-IL5-TRANSIT) `sfind-99a65f9993994400b1f5dedfe0c57f0a`
- [high] No logout/revocation and require_token never checks token age (AC-11, AC-12, SC-23, SRG-IL5-SESSION) `sfind-901a35851e914817beb6d4f3d5aed495`
- [high] Login has no failed-attempt counting or account lockout (AC-7, SRG-IL5-LOCKOUT) `sfind-7b8167f9a283407c8c16364ec584bff4`
- [high] audit() records lack actor, source IP, UTC time and outcome; events unaudited (AC-7, AU-12, AU-2, AU-3, SRG-IL5-AUDIT-CONTENT) `sfind-67042a81551e4e999fcef9519050cd7e`
- [high] GET /login returns no DoD Notice and Consent Banner or acknowledgement (AC-8, SRG-IL5-BANNER) `sfind-5a1f0638b2d84273ac66ac441f8ca7dc`
- [high] Global exception handler returns exception text and traceback to clients (SRG-IL5-CUI) `sfind-4c83e71b63d243cb9bc812714248c390`
- [high] SESSION_IDLE_MINUTES set to None; idle timeout never configured (SRG-IL5-SESSION) `sfind-3fa71bc5d7b94a8eb6e91c3ff3a21a13`
- [high] POST /login uses local username/password, not DoD PKI/CAC (IA-2, SRG-IL5-PKI) `sfind-3f80e358303a491da32b454920dab3a2`
- [low] Module docstring planted-gap register (G1-G8) (AC-11, AC-12, AC-8, AU-12, AU-3, CM-5, IA-5, SC-13, SI-10, SI-11, SR-3, SRG-IL5-AUDIT-CONTENT, SRG-IL5-BANNER, SRG-IL5-CRYPTO, SRG-IL5-CUI, SRG-IL5-SECRETS, SRG-IL5-SESSION) `sfind-0f4eec87a608445dac83b1ef97244b01`

Out of scope (for ISSO): see `docs/il5/catalog/dod-cc-srg-il5-excluded.csv` (6 items).

## asd-stig-v6r5

No findings before pause.


Out of scope (for ISSO): see `docs/il5/catalog/asd-stig-v6r5-excluded.csv` (125 items).

## kubernetes-stig-v2r6

- [high] Dockerfile has no USER directive, so the mrt image runs as root (V-242383, V-242415, V-242437, V-274883) `sfind-9c145066b20045ed8e044d118d7a3695`
- [low] Dockerfile EXPOSE 8000 and uvicorn bind on port 8000 (V-242414) `sfind-53f0a8380cdf4c4189c2245afb3c5817`

Out of scope (for ISSO): see `docs/il5/catalog/kubernetes-stig-v2r6-excluded.csv` (84 items).
