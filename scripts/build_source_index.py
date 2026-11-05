"""Index source subheadings and question/answer page locations from Markdown."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1]
cs=json.loads((R/"data/chapters.json").read_text(encoding="utf-8"))
out=["# Indeks subbagian, soal, dan jawaban sumber","","Indeks otomatis ini membantu menemukan lokasi dalam teks asli. Judul mengikuti ekstraksi; judul panjang dapat terpotong. Label halaman menunjukkan kemunculan kata penanda, bukan jumlah soal atau jaminan seluruh jawaban terbaca. Cocokkan dengan PDF bila diperlukan.",""]
sections_total=0
for c in cs:
    src=R/f'docs/book/{c["slug"]}.md'
    chunks=re.split(r"^## Halaman PDF (\d+)\s*$",src.read_text(encoding="utf-8"),flags=re.M)
    sections=[]; markers={k:[] for k in ("SUMMARY","QUESTIONS","EXERCISES","ANSWERS","BIBLIOGRAPHY")}
    seen=set()
    for i in range(1,len(chunks),2):
        page=int(chunks[i]); body=chunks[i+1]
        for m in re.finditer(r"\bSection[ \t]+(\d+\.\d+)[ \t]*\n([^\n]+)",body):
            num,title=m.groups()
            if not num.startswith(str(c["number"])+".") or num in seen: continue
            seen.add(num); sections.append((num,title.strip(),page))
        for marker in markers:
            if re.search(r"\b"+marker+r"\b",body): markers[marker].append(page)
    out += [f'## Bab {c["number"]}: {c["title"]}',"",f'[Teks bab](book/{c["slug"]}.md) · [Catatan belajar](study/{c["slug"]}.md)',""]
    if sections:
        out+=["| Subbagian | Judul dari teks sumber | PDF |","| --- | --- | ---: |"]
        for num,title,page in sections:
            title=title.replace("|","/")
            out.append(f'| {num} | {title} | [{page}](book/{c["slug"]}.md#halaman-pdf-{page}) |')
    else: out+=["Nomor subbagian tidak dikenali otomatis; baca teks bab untuk urutan lengkap."]
    out+=["","**Lokasi penanda sumber:**",""]
    for marker,pages in markers.items():
        if pages:
            refs=", ".join(f'[{p}](book/{c["slug"]}.md#halaman-pdf-{p})' for p in pages)
            out.append(f"- {marker}: {refs}.")
    out+=[""]
    sections_total+=len(sections)
(R/"docs/source-index.md").write_text("\n".join(out).rstrip()+"\n",encoding="utf-8")
print(json.dumps(dict(chapters=len(cs),subsections_indexed=sections_total)))
