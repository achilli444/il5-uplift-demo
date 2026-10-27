# IL5 uplift state - il5-uplift-demo  (parent session updates this after every step; `--resume` reads it)

| Step | Status (todo / running / waiting-gate / done) | Evidence / URLs | Updated |
|---|---|---|---|
| 1 Init + boundary | done | 00-boundary.md on il5/main; baseline main @ 977214f | 2026-10-27 |
| 2 Child: SBOM | done | https://devin-gtm.devinenterprise.com/sessions/92802104a79942b2ba71f310cdfa439c -> docs/il5/evidence/sbom/ @ 9aa43ae (source 19 / image 108 purls; grype image 0C/58H) | 2026-10-27 |
| Gate 1 ISSO SBOM accepted | waiting-gate | approver, date, message link | |
| 3a Child: Security scan | running | https://devin-gtm.devinenterprise.com/sessions/5b840eca3ca046dda2fd3ebc28f901f4 (Security 2.0 + SonarQube ingest) | 2026-10-27 |
| 3b Child: Compliance scans | running | https://devin-gtm.devinenterprise.com/sessions/ef48afef75b74f0f8a53366bb4fc19a3 | 2026-10-27 |
| 4 Child: De-conflict + user selection | | 10-remediation-register.md, 12-remediation-scope.csv | |
| Gate 2 user selected units (who/how many) | | | |
| 5 Dispositions applied | | Findings export path | |
| 6 Wave 1 children | | unit -> child URL -> PR | |
| 7 Wave 2 children | | | |
| 8 Reconcile | | scan-new-commits results | |
| 8 Child: post-remediation SBOM | | child URL, package path, diff file | |
| 9 Child: Evidence | | package path + hash | |
| Gate 4 package to AO | | | |
| 10 Automations | | automation IDs | |

Repos/branch: achilli444/il5-uplift-demo, deploy branch main, uplift branch il5/main
Evidence destination: docs/il5/evidence/ (repo)
Approvers: ISSO Achal Amin, ISSM Achal Amin, dev lead Achal Amin, AO rep (not named)
ISSM parameter values: see 00-boundary.md

Parent session: https://devin-gtm.devinenterprise.com/sessions/d21b4bd30b9842b68f8283df20b9a52e
Existing scanners (ISSO answer 2026-10-27): Devin Security 2.0 + SonarQube ingest. Scans started in parallel with SBOM before Gate 1, per ISSO choice "Start scans now".
