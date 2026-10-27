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
