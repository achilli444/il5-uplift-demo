"""Recompute review tables from retained scanner evidence (Python standard library)."""
import collections
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BANNER = 'CUI // demo marking - designation per ISSM (Achal Amin)'


def main():
    summary, quality, vulns, licenses = {}, {}, [], []
    for deployable in ('source', 'image'):
        base = next(ROOT.glob(f'*_{deployable}_sbom_*.cdx.json'))
        stem = base.name.removesuffix('.cdx.json')
        bom = json.loads(base.read_text())
        components = bom['components']
        packages = [c for c in components if c['type'] != 'file']
        unknown = [c for c in packages if not c.get('supplier') or c['supplier'].get('name', '').upper() == 'UNKNOWN']
        quality[deployable] = dict(cyclonedx_version=bom['specVersion'], spdx_version=json.loads((ROOT / (stem + '.spdx.json')).read_text())['spdxVersion'], serial_number_set=bool(bom.get('serialNumber')), metadata_component=bom['metadata']['component']['name'], dependency_graph_entries=len(bom.get('dependencies', [])), packages_missing_purl=[c for c in packages if not c.get('purl')], files_without_purl=sum(c['type'] == 'file' and not c.get('purl') for c in components), unknown_supplier_percent_packages=100*len(unknown)/len(packages), unknown_supplier_packages=[dict(name=c['name'], version=c.get('version'), ref=c['bom-ref']) for c in unknown])
        for c in components:
            values = [e.get('expression') or e.get('license', {}).get('id') or e.get('license', {}).get('name') or 'UNKNOWN' for e in c.get('licenses', [])]
            label = ' ; '.join(values) or 'UNKNOWN'
            licenses.append(dict(deployable=deployable, component=c['name'], version=c.get('version', ''), component_type=c['type'], bom_ref=c['bom-ref'], license=label, copyleft_flag='review' if re.search(r'GPL|MPL|EPL|CDDL|CECILL', label, re.I) else 'no-detected-copyleft', unknown_flag=str(label == 'UNKNOWN').lower()))
        for m in json.loads((ROOT / (stem + '.grype.json')).read_text())['matches']:
            v, a = m['vulnerability'], m['artifact']
            aliases = sorted({r['id'] for r in m.get('relatedVulnerabilities', []) if r['id'].startswith('CVE-')})
            scores = [str(c.get('metrics', {}).get('baseScore')) for c in v.get('cvss', []) if c.get('metrics', {}).get('baseScore') is not None]
            vulns.append(dict(deployable=deployable, scanner='grype', component=a['name'], version=a['version'], advisory=v['id'], CVE=v['id'] if v['id'].startswith('CVE-') else ';'.join(aliases), severity=v['severity'].upper(), CVSS=';'.join(sorted(set(scores))), fix_version=';'.join(v.get('fix', {}).get('versions', [])), exploitability_note='Database match only; runtime reachability and exploitation not assessed'))
        for result in json.loads((ROOT / (stem + '.trivy.json')).read_text()).get('Results', []):
            for v in result.get('Vulnerabilities', []):
                scores = [str(c.get('V3Score', c.get('V2Score', ''))) for c in v.get('CVSS', {}).values()]
                vulns.append(dict(deployable=deployable, scanner='trivy', component=v['PkgName'], version=v['InstalledVersion'], advisory=v['VulnerabilityID'], CVE=v['VulnerabilityID'] if v['VulnerabilityID'].startswith('CVE-') else '', severity=v['Severity'], CVSS=';'.join(sorted(set(scores))), fix_version=v.get('FixedVersion', ''), exploitability_note='Database match only; runtime reachability and exploitation not assessed'))
        rows = [v for v in vulns if v['deployable'] == deployable]
        sets = {s: {(v['component'], v['version'], v['CVE'] or v['advisory']) for v in rows if v['scanner'] == s} for s in ('grype', 'trivy')}
        lic = [v for v in licenses if v['deployable'] == deployable]
        summary[deployable] = dict(component_entries=len(components), package_entries=len(packages), file_entries=len(components)-len(packages), unique_package_purls=len({c['purl'] for c in packages if c.get('purl')}), severity_counts={s: dict(collections.Counter(v['severity'] for v in rows if v['scanner'] == s)) for s in ('grype', 'trivy')}, license_flags={k: sum(v[k] == val for v in lic) for k, val in [('copyleft_flag', 'review'), ('unknown_flag', 'true')]}, package_license_flags={k: sum(v[k] == val and v['component_type'] != 'file' for v in lic) for k, val in [('copyleft_flag', 'review'), ('unknown_flag', 'true')]}, scanner_disagreements={s + '_only': sorted(sets[s] - sets[other]) for s, other in [('grype', 'trivy'), ('trivy', 'grype')]})
    for name, rows in [('vulns.csv', vulns), ('licenses.csv', licenses)]:
        with (ROOT / name).open('w', newline='') as out:
            out.write('# ' + BANNER + '\n')
            writer = csv.DictWriter(out, fieldnames=list(rows[0]), lineterminator='\n')
            writer.writeheader()
            writer.writerows(rows)
    rank = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3, 'NEGLIGIBLE': 4, 'UNKNOWN': 5}
    top, seen = [], set()
    for v in sorted(vulns, key=lambda v: (rank.get(v['severity'], 5), v['component'], v['CVE'])):
        key = (v['component'], v['version'], v['CVE'])
        if v['CVE'] and v['fix_version'] and key not in seen:
            top.append(v)
            seen.add(key)
        if len(top) == 5:
            break
    summary['top_5_fixable_CVEs'] = top
    for name, data in [('summary.json', summary), ('quality-check.json', quality)]:
        (ROOT / name).write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
