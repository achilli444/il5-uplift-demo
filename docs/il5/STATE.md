# IL5 uplift state - <system-slug>  (parent session updates this after every step; `--resume` reads it)

| Step | Status (todo / running / waiting-gate / done) | Evidence / URLs | Updated |
|---|---|---|---|
| 1 Init + boundary | | 00-boundary.md @ <sha> | |
| 2 Child: SBOM | | child URL, package path | |
| Gate 1 ISSO SBOM accepted | | approver, date, message link | |
| 3a Child: Security scan | | child URL, scan IDs, 02-security-summary.md | |
| 3b Child: Compliance scans | | child URL, scan IDs, 03-compliance-summary.md | |
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

Repos/branch: 
Evidence destination: 
Approvers: ISSO <>, ISSM <>, dev lead <>, AO rep <>
ISSM parameter values: see 00-boundary.md
