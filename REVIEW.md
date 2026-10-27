## Security review instructions (IL5 uplift)
- Sensitive areas: `app/auth.py`, `app/settings.py`, `app/db.py`, `app/main.py` error handling and audit, `Dockerfile`, `k8s/`.
- Flag non-FIPS algorithms (MD5, SHA-1, RC4, DES/3DES, ECB, TLS < 1.2), disabled certificate validation, `latest` image tags, privileged containers, secrets in env/source/logs, verbose error output.
- A PR that claims to remediate a control must include the control crosswalk section and a regression test; flag it if either is missing.
- Reference findings with CWE and the 800-53 Rev 5 / STIG ID when you can; the Remediation Register is keyed on those.
