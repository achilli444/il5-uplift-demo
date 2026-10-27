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
