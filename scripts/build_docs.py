from pathlib import Path
import json, hashlib, argparse
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1]
P=R/"CoreCourseFinancialAccounting.pdf"
def w(p,t):
    f=R/p; f.parent.mkdir(parents=True,exist_ok=True); f.write_text(t.rstrip()+"\n",encoding="utf-8")
ap=argparse.ArgumentParser(); ap.add_argument("--pages-json",type=Path); args=ap.parse_args()
cs=json.loads((R/"data/chapters.json").read_text(encoding="utf-8"))
ns=json.loads((R/"data/study-notes.json").read_text(encoding="utf-8"))
pages=json.loads(args.pages_json.read_text(encoding="utf-8")) if args.pages_json else [p.extract_text() or "" for p in PdfReader(P).pages]
assert len(pages)==997 and [n["n"] for n in ns]==list(range(1,51))
segs=[dict(slug="00-front-matter",title="Pengantar, identitas, dan simbol",pdfStart=1,pdfEnd=16)]+cs+[dict(slug="51-epilogue",title="Epilogue: Finance and Strategy",pdfStart=941,pdfEnd=948),dict(slug="52-reference-matter",title="Referensi historis, daftar isi, indeks, dan halaman penutup",pdfStart=949,pdfEnd=997)]
coverage=[]; manifest=[]
for s in segs:
    a,b=s["pdfStart"],s["pdfEnd"]; coverage+=list(range(a,b+1))
    path=f'docs/book/{s["slug"]}.md'
    lines=[f'# {s["title"]}',"",f'Halaman PDF {a}–{b}. [PDF asli](../../CoreCourseFinancialAccounting.pdf#page={a}).',"","> Ekstraksi otomatis bahasa asli. Rumus bertingkat, tabel, grafik, ligatur, urutan kolom, dan teks gambar dapat berubah atau tidak terbaca. Cocokkan dengan PDF sebagai acuan visual. Nomor PDF berbeda dari nomor cetak.",""]
    if "number" in s: lines += [f'[Catatan belajar bab {s["number"]}](../study/{s["slug"]}.md) · [Daftar isi](../../SUMMARY.md)',""]
    for p in range(a,b+1):
        t="\n".join(line.rstrip() for line in pages[p-1].replace("\x00","").splitlines()).strip()
        lines += [f"## Halaman PDF {p}","",f"[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page={p})",""]
        lines += ["~~~text",t,"~~~",""] if t else ["Tidak ada teks yang dapat diekstrak. Lihat PDF untuk memeriksa apakah halaman kosong, pemisah, atau gambar.",""]
    w(path,"\n".join(lines))
    manifest.append(dict(path=path,pdf_start=a,pdf_end=b,characters=sum(len(pages[p-1]) for p in range(a,b+1))))
assert coverage==list(range(1,998)), "Page gaps or overlap"
for c,n in zip(cs,ns):
    lines=[f'# Bab {n["n"]}: {n["topic"]}',"",f'**Judul sumber:** {c["title"]}. **Cetak mulai:** {c["printedStart"]}. **PDF:** {c["pdfStart"]}–{c["pdfEnd"]}.',"",f'[Teks sumber](../book/{c["slug"]}.md) · [PDF](../../CoreCourseFinancialAccounting.pdf#page={c["pdfStart"]}) · [Daftar isi](../../SUMMARY.md)',"","> Catatan pendamping Indonesia. Contoh adalah ilustrasi baru, bukan soal asli atau terjemahan resmi. Pajak dan bunga adalah asumsi latihan, bukan tarif aktual.","","## Konsep dan penalaran","",n["concept"],"","## Rumus atau kerangka analisis","","$$",n["formula"],"$$","",n["variables"],"","## Contoh dan langkah perhitungan","",n["example"],"","## Implikasi keputusan","",n["decision"],"","## Kesalahan yang perlu dihindari","",n["pitfall"],"","## Uji pemahaman","","**Pertanyaan:** "+n["question"],"","**Pembahasan:** "+n["answer"],"","## Lanjut membaca","","Teks sumber memuat subbagian, soal, jawaban, dan bibliografi pada rentang halaman bab sesuai hasil ekstraksi. Cocokkan simbol, grafik, dan tabel dengan PDF asli."]
    i=c["number"]
    if i>1: lines+=["",f'[Bab sebelumnya](./{cs[i-2]["slug"]}.md)']
    if i<50: lines+=["",f'[Bab berikutnya](./{cs[i]["slug"]}.md)']
    w(f'docs/study/{c["slug"]}.md',"\n".join(lines))
summary=["# Daftar isi","","* [Beranda](README.md)","* [Panduan membaca](docs/reading-guide.md)","* [Peta sumber](docs/source-map.md)","* [Indeks subbagian dan soal asli](docs/source-index.md)","* [Status verifikasi](docs/verification.md)","* [Indeks rumus](docs/formulas.md)","* [Rumus lanjutan](docs/advanced-formulas.md)","* [Latihan dan pembahasan](docs/exercises.md)","* [Kasus terintegrasi](docs/integrated-case.md)","* [Glosarium](docs/glossary.md)","","## Catatan belajar Indonesia",""]
for label,a,b in [("Pendahuluan",0,1),("I. Analisis keuangan",1,14),("II. Investor dan pasar",14,25),("III. Nilai",25,31),("IV. Kebijakan keuangan",31,39),("V. Manajemen keuangan",39,50)]:
    summary+=["",f"### {label}",""]+[f'* [Bab {c["number"]}: {ns[c["number"]-1]["topic"]}](docs/study/{c["slug"]}.md)' for c in cs[a:b]]
summary+=["","## Teks sumber bahasa Inggris","","* [Pengantar dan simbol](docs/book/00-front-matter.md)"]+[f'* [{c["number"]:02d}. {c["title"]}](docs/book/{c["slug"]}.md)' for c in cs]+["* [Epilog](docs/book/51-epilogue.md)","* [Referensi dan indeks](docs/book/52-reference-matter.md)"]
w("SUMMARY.md","\n".join(summary))
fm=["# Indeks rumus dan kerangka analisis","","Lima puluh rumus/kerangka utama catatan pendamping ditulis ulang dalam LaTeX. Ini bukan inventaris setiap persamaan buku. Rumus lainnya berada dalam teks sumber; gunakan PDF bila simbol berubah. Periksa asumsi sebelum menggunakan formula.",""]
ex=["# Latihan dan pembahasan","","Satu pertanyaan pendamping baru per bab. Soal dan jawaban asli tercakup pada teks sumber sesuai ekstraksi; seluruh soal asli belum dihitung ulang secara independen. Contoh pendamping menggunakan asumsi latihan.",""]
for c,n in zip(cs,ns):
    fm += [f'## Bab {n["n"]}: {n["topic"]}',"","$$",n["formula"],"$$","",n["variables"],"",f'[Penjelasan dan contoh](study/{c["slug"]}.md)',""]
    ex += [f'## {n["n"]:02d}. {n["topic"]}',"",n["question"],"","**Pembahasan:** "+n["answer"],"","**Contoh/kasus:** "+n["example"],"",f'[Bab terkait](study/{c["slug"]}.md)',""]
w("docs/formulas.md","\n".join(fm)); w("docs/exercises.md","\n".join(ex))
sha=hashlib.sha256(P.read_bytes()).hexdigest()
mapping=["# Identitas dan peta sumber","","**Corporate Finance: Theory and Practice, Fourth Edition**. Pierre Vernimmen; Pascal Quiry, Maurizio Dallocchio, Yann Le Fur, Antonio Salvi. Wiley, 2014. Identitas diperiksa pada PDF halaman 5–6.","","File sumber: CoreCourseFinancialAccounting.pdf. Nama asli dipertahankan.","",f"SHA-256: {sha}.","","997 halaman. Badan buku mulai PDF 17 = cetak 1. Pemetaan badan buku: PDF = cetak + 16. Rentang bab mencakup halaman pemisah sebelum bab berikutnya bila ada.","","| Bab | Judul | Cetak mulai | PDF |","| --- | --- | ---: | --- |"]+[f'| {c["number"]} | [{c["title"]}](book/{c["slug"]}.md) | {c["printedStart"]} | {c["pdfStart"]}–{c["pdfEnd"]} |' for c in cs]+["","Pengantar PDF 1–16; epilog PDF 941–948; referensi dan halaman akhir PDF 949–997. Data perusahaan dan pasar pada referensi merupakan data historis.","","[Manifest ekstraksi](../data/extraction-manifest.json) · [Peta bab](../data/chapters.json)"]
w("docs/source-map.md","\n".join(mapping))
report=dict(source_pdf=P.name,pdf_sha256=sha,pdf_pages=997,engine="pypdf plain text extraction",characters=sum(map(len,pages)),pages_without_extracted_text=[i+1 for i,t in enumerate(pages) if not t.strip()],segments=manifest,pages=[dict(pdf_page=i+1,characters=len(t),text_sha256=hashlib.sha256(t.encode()).hexdigest()) for i,t in enumerate(pages)])
w("data/extraction-manifest.json",json.dumps(report,ensure_ascii=False,indent=2))
w(".gitbook.yaml","root: ./\nstructure:\n  readme: README.md\n  summary: SUMMARY.md")
w("requirements.txt","pypdf==6.10.0")
w(".gitignore","__pycache__/\n*.py[cod]\n.venv/\n.work/\n")
print(json.dumps(dict(pages=997,source_files=len(segs),study_chapters=50,source_characters=report["characters"],pdf_sha256=sha)))
