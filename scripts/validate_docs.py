"""Validate page coverage, chapter content, local links, math blocks, and examples."""
from pathlib import Path
import json,re,hashlib
from urllib.parse import unquote,urlsplit
from finance_examples import run_checks
R=Path(__file__).resolve().parents[1]
errors=[]; links=0
def require(ok,msg):
    if not ok: errors.append(msg)
manifest=json.loads((R/"data/extraction-manifest.json").read_text(encoding="utf-8"))
chapters=json.loads((R/"data/chapters.json").read_text(encoding="utf-8"))
notes=json.loads((R/"data/study-notes.json").read_text(encoding="utf-8"))
require(hashlib.sha256((R/manifest["source_pdf"]).read_bytes()).hexdigest()==manifest["pdf_sha256"],"Source PDF checksum mismatch")
coverage=[]
for seg in manifest["segments"]:
    path=R/seg["path"]
    require(path.exists(),f"Missing source {path}")
    if not path.exists(): continue
    text=path.read_text(encoding="utf-8")
    page_numbers=[int(x) for x in re.findall(r"^## Halaman PDF (\d+)$",text,re.M)]
    expected=list(range(seg["pdf_start"],seg["pdf_end"]+1))
    require(page_numbers==expected,f"Page headings mismatch: {seg['path']}")
    coverage+=page_numbers
require(coverage==list(range(1,998)),"All PDF pages must appear exactly once and in order")
require(len(list((R/"docs/book").glob("*.md")))==53,"Expected 53 source files")
require(len(list((R/"docs/study").glob("*.md")))==50,"Expected 50 study chapters")
require([n["n"] for n in notes]==list(range(1,51)),"Study data must cover 1 through 50")
required=["## Konsep dan penalaran","## Rumus atau kerangka analisis","## Contoh dan langkah perhitungan","## Implikasi keputusan","## Kesalahan yang perlu dihindari","## Uji pemahaman"]
for c in chapters:
    path=R/f'docs/study/{c["slug"]}.md'
    require(path.exists(),f"Missing study {c['number']}")
    if path.exists():
        t=path.read_text(encoding="utf-8")
        for heading in required: require(heading in t,f"Missing {heading}: {path.name}")
for path in R.rglob("*.md"):
    if ".git" in path.parts: continue
    t=path.read_text(encoding="utf-8")
    require("\x00" not in t,f"NUL in {path}")
    math_blocks=sum(line.strip()=="$$" for line in t.splitlines())
    require(math_blocks%2==0,f"Unpaired math block: {path}")
    in_fence=False; visible=[]
    for line in t.splitlines():
        if line.lstrip().startswith(("~~~",chr(96)*3)):
            in_fence=not in_fence
            continue
        if not in_fence: visible.append(line)
    require(not in_fence,f"Unclosed code fence: {path}")
    for target in re.findall(r"\]\(([^)\n]+)\)","\n".join(visible)):
        parsed=urlsplit(target.strip("<>"))
        if parsed.scheme or target.startswith("#"): continue
        local=unquote(parsed.path)
        if not local: continue
        links+=1
        resolved=(path.parent/local).resolve()
        require(resolved.is_relative_to(R.resolve()),f"Link outside repository: {path}: {target}")
        require(resolved.exists(),f"Broken local link: {path.relative_to(R)} -> {target}")
    if path.parent.name=="study":
        require("\\\\" not in t,"Unexpected doubled LaTeX slash in "+path.name)
calculations=run_checks()
report=dict(status="PASS" if not errors else "FAIL",pages_covered=len(coverage),source_files=53,study_chapters=50,
  markdown_files=len(list(R.rglob("*.md"))),local_links_checked=links,numerical_checks=len(calculations),errors=errors,numerical_results=calculations)
(R/"data/validation-results.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in report.items() if k!="numerical_results"},ensure_ascii=False))
if errors: raise SystemExit(1)
