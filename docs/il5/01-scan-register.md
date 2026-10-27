# Scan register - il5-uplift-demo (step 3a, security)

CUI // treat as CUI unless the ISSM says otherwise. Implementation status only; the AO decides.

Repo / branch / commit: `achilli444/il5-uplift-demo` @ `il5/main` `ce1f17954c161f7a445f26a88f17b6d2ee77fe98`
Exclusions (from 00-boundary.md / ISSO): `tests/**`, `docs/**`
Child session: https://devin-gtm.devinenterprise.com/sessions/5b840eca3ca046dda2fd3ebc28f901f4

## Existing scanners
ISSO answer (Achal Amin, 2026-10-27, relayed by parent session): SonarQube via the connected `sonarqube` MCP server, existing quality profile unchanged. No other existing scanners named.

| Tool | Results location | Auth (secret name) | Fresh run from here | Profile / ruleset to honor | Disposition |
|---|---|---|---|---|---|
| SonarQube (SonarCloud, org `cog-gtm`) | SonarCloud project for this repo (none found) | MCP server env `SONARQUBE_MCP_TOKEN` | No (no project; Devin must not create one) | Existing quality profile, unchanged | **not available - no project** |

SonarQube detail (checked 2026-10-27 ~08:50 UTC): `search_my_sonarqube_projects` via the MCP server returned "Not authorized" (SonarCloud `api/authentication/validate` reports the configured token as invalid); an anonymous SonarCloud lookup in org `cog-gtm` found no project matching `il5`/`il5-uplift-demo` (`achilli444_il5-uplift-demo`, `il5-uplift-demo`, `cog-gtm_il5-uplift-demo` all "not found"). Per ISSO instruction no Sonar project or rules were created, and no ingest-mode profile/scan was created. To add later: fix the MCP token, create/locate the project, then run an ingest-mode scan.

## Devin Security 2.0
| Scan ID | URL | Orchestrating session | Profile | Effort | Repo / branch / SHA | Status | Findings |
|---|---|---|---|---|---|---|---|
| `scan-87996f1a24b348bfa10fbfa16f74bb7f` | https://devin-gtm.devinenterprise.com/code-scan/87996f1a24b348bfa10fbfa16f74bb7f | https://devin-gtm.devinenterprise.com/sessions/fb4c1b8ae7784fbaba86f77eb6894582 | `csprof-4d966f2e18014952ba752c95871c8849` "il5-uplift-demo scope (exclude tests/docs)" (new, scope-only: exclude_globs `tests/**`, `docs/**`) | Normal (user selected Normal on the setup form; parent brief had asked for Deep) | achilli444/il5-uplift-demo / il5/main / ce1f179 | completed 2026-10-27 (created 08:55 UTC, done before 09:01 UTC); ISSO pause request at 09:01 UTC arrived after completion, so nothing was paused | 8 total: 7 open, 1 dismissed by the scan's own triage |

Launch approval: setup form `il5-sec2-deep-1` submitted by Achal Amin in this session. No findings were assigned, fixed or dismissed by this session.

## Compliance


System: `il5-uplift-demo` - Mission Readiness Tracker (il5-uplift-demo). Repo `achilli444/il5-uplift-demo` @ `il5/main` (base SHA `ce1f17954c161f7a445f26a88f17b6d2ee77fe98`).

### Benchmark sources

| Framework slug | File | Version / release | SHA-256 | Source |
|---|---|---|---|---|
| `asd-stig-v6r5` | `U_ASD_V6R5_STIG.zip` | Application Security and Development STIG V6, Release: 5 Benchmark Date: 30 Sep 2026 (286 rules) | `b73e8a74d591982d49cdc9e0c5c0023b37ab87d91f3f3f150d6dab8baa23c435` | https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_ASD_V6R5_STIG.zip (via public.cyber.mil/stigs/downloads) |
| `asd-stig-v6r5` | `U_ASD_STIG_V6R5_Manual-xccdf.xml` (in zip) | as above | `34e8dfa6841229735082e341a1cf6c5a48eec84ce0e7e5d3f03ab02355fe066d` | parsed XCCDF |
| `kubernetes-stig-v2r6` | `U_Kubernetes_V2R6_STIG.zip` | Kubernetes STIG V2, Release: 6 Benchmark Date: 01 Apr 2026 (92 rules) | `2e66cc46e19889f337b40a7827745146c40c7b532529c03d826ba7462419876a` | https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Kubernetes_V2R6_STIG.zip (via public.cyber.mil/stigs/downloads) |
| `kubernetes-stig-v2r6` | `U_Kubernetes_STIG_V2R6_Manual-xccdf.xml` (in zip) | as above | `0ca995078bd987a153f5a3238d0812b331883809d11547882bf0cedf0b110e50` | parsed XCCDF |
| `nist-800-53-rev5-high` | `NIST_SP-800-53_rev5_HIGH-baseline-resolved-profile_catalog.json` | OSCAL SP 800-53 Rev 5.1.1 HIGH baseline, catalog version 5.2.0 | `a408708dcc11c864ebf98e8df9f64c07e0daf778e33f8bd71b40120da3db6a96` | https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/ |
| `dod-cc-srg-il5` | none uploaded | DoD Cloud Computing SRG, IL5 requirements | n/a | criteria authored from the IL5 code/config requirement set in the run-compliance-scans procedure, each tied to its 800-53 control; ISSO to confirm against the current CC SRG |

### Catalogs and scans

Scanned commit: `45da2de62033cd4ee260a7650259213a570d7e88` (origin/il5/main at launch), effort normal, launched 2026-10-27 after in-session approval of each setup form. Kubernetes STIG scan_paths: `k8s/**`, `Dockerfile`.

| Framework slug | Criteria loaded | Excluded | Profile ID | Scan ID | Session URL | Status | Findings |
|---|---|---|---|---|---|---|---|
| `nist-800-53-rev5-high` | 33 | 4 + inherited/organizational families | `csprof-569ee8cc2b86400cb32b5ff5d9613d8e` | `scan-b0d4def03df74cab9c8f66fb8b7316f9` | https://devin-gtm.devinenterprise.com/sessions/38ff0d94a9924dec96a87272c07ccc21 | partial - paused by ISSO at 2026-10-27T09:02:06Z | 17 |
| `dod-cc-srg-il5` | 12 | 6 | `csprof-96249806f4254aceaa69311cce6bd5ae` | `scan-c3960b3b4c884acf90dcf6931f910461` | https://devin-gtm.devinenterprise.com/sessions/8b9caa6eca2545058f9523d47727bd12 | partial - paused by ISSO at 2026-10-27T09:02:06Z | 53 |
| `asd-stig-v6r5` | 161 | 125 | `csprof-1136820cd35447b4aaae051feac112bd` | `scan-c8e52e9e2081421ea05148d95868147e` | https://devin-gtm.devinenterprise.com/sessions/45b9cf3742364260947f2579c911bbac | partial - paused by ISSO at 2026-10-27T09:02:06Z | 0 |
| `kubernetes-stig-v2r6` | 8 | 84 | `csprof-ee435f079d5848328f0141f32e1704cb` | `scan-63e0dadf072843d78ef6f9b5515c55f8` | https://devin-gtm.devinenterprise.com/sessions/1591f8db92d947ff96d216c432138c1f | completed (before ISSO pause) | 2 |
No findings were assigned, fixed or dismissed by this session. Criteria with findings so far: nist-800-53-rev5-high 22/33, dod-cc-srg-il5 12/12, asd-stig-v6r5 0/161, kubernetes-stig-v2r6 5/8.
