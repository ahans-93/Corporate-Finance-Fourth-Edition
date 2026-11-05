"""Integrate uploaded formula references and a reviewed companion in docs/book.
Idempotent: run after build_docs.py, before source-index and validation.
"""
from pathlib import Path
import re,json,hashlib
R=Path(__file__).resolve().parents[1]
BOOK=R/"docs/book"
ORIG=BOOK/"supplements/kompilasi_rumus_corporate_finance.md"
CONFIG=R/"data/formula-supplement-review.json"
config=json.loads(CONFIG.read_text(encoding="utf-8"))
chapters=json.loads((R/"data/chapters.json").read_text(encoding="utf-8"))
source=ORIG.read_text(encoding="utf-8")
matches=list(re.finditer(r"^## (\d+\.\d+) (.+)$",source,re.M))
assert len(matches)==31
assert [int(n) for n in re.findall(r"\\tag\{(\d+)\}",source)]==list(range(1,151))
out=["# Kompilasi rumus corporate finance — versi telaah","","Pelengkap untuk buku Vernimmen edisi keempat. Disusun dari kompilasi yang Anda berikan, dengan nomor persamaan 1–150 dipertahankan agar perubahan mudah dibandingkan. Ada 31 kelompok bahasan, penjelasan asumsi, dan contoh. Nomor persamaan ini adalah nomor kompilasi, bukan nomor persamaan asli buku.","",
     "**Cakupan:** 23 persamaan ditulis ulang untuk memperjelas definisi, asumsi, tanda, atau cakupan. Ini bukan klaim bahwa seluruh persamaan buku telah diinventaris atau bahwa seluruh rumus kompilasi adalah kutipan literal dari 50 bab. Model pelengkap umum ditandai dalam catatan.","",
     "[Berkas asli Markdown](supplements/kompilasi_rumus_corporate_finance.md) · [LaTeX asli](supplements/kompilasi_rumus_corporate_finance.tex) · [PDF asli kompilasi](supplements/kompilasi_rumus_corporate_finance.pdf) · [Daftar koreksi](54-catatan-koreksi-rumus.md) · [Daftar buku](README.md)","","## Navigasi",""]
for i,(m,info) in enumerate(zip(matches,config["sections"]),1):
    assert m.group(1)==info["id"]
    out.append(f'- [S{i:02d}: {m.group(2)}](#s{i:02d})')
for i,(m,info) in enumerate(zip(matches,config["sections"]),1):
    body=source[m.end():matches[i].start() if i<len(matches) else len(source)].strip()
    body=re.sub(r"^# [1-5] .+\n?","",body,flags=re.M)
    body=re.sub(r"\*Dokumen Kompilasi Formula Vernimmen Corporate Finance.+?\*","",body,flags=re.S)
    for key,formula in config["replacements"].items():
        pattern=r"\$\$(?:(?!\$\$).)*?\\tag\{"+str(key)+r"\}(?:(?!\$\$).)*?\$\$"
        body=re.sub(pattern,lambda x:"$$"+formula+r" \tag{"+str(key)+"}$$",body,flags=re.S)
    body=body.replace(r"\text{Prepurchase Price}",r"P_{\text{repurchase}}")
    body=re.sub(r"^> (\$\$.*?\$\$)$",r"\1",body,flags=re.M)
    body=re.sub(r"\$\$(.*?)\$\$",lambda x:"\n$$\n"+x.group(1).strip()+"\n$$\n",body,flags=re.S)
    body=re.sub(r"\n{3,}","\n\n",body)
    if info["id"]=="1.8":
        body=body.replace("Model Prediksi Kebangkrutan Altman Z-Score (Bab 14)","Altman klasik: model pelengkap")
    related=" · ".join(f'[Bab {n}: {chapters[n-1]["title"]}](./{chapters[n-1]["slug"]}.md)' for n in info["chapters"])
    out += ["",f"## S{i:02d}","",f'**{info["id"]} — {m.group(2)}**',"",related,"","### Asumsi dan penjelasan","",info["assumptions"],"","### Persamaan","",body.strip(),"","### Contoh penerapan","",info["example"]]
    if info["id"]=="1.8":
        out += ["","### Bentuk yang dibahas buku pada bab 8","","[PDF 152, halaman cetak 136](../../CoreCourseFinancialAccounting.pdf#page=152) menyajikan bentuk Z-double-prime berikut. Pertahankan definisi dan koefisien versi sumber; jangan mengganti denominator atau ambang dengan varian lain.","","$$",r"Z''=6.6X_1+3.26X_2+6.72X_3+1.05X_4","$$","","Pada uraian halaman tersebut, X₁=working capital/total assets; X₂=retained earnings/total assets; X₃=operating profit/total assets; X₄=shareholders' equity/net debt. Buku menyebut area rendah di bawah 1,1, area tinggi di atas 2,6, dan area antara keduanya. Ini adalah reproduksi konteks buku, bukan model kredit yang dikalibrasi untuk seluruh perusahaan."]
    if info["id"]=="3.2":
        out += ["","**Penelusuran sumber:** [bab 27, PDF 513/cetak 497](27-measuring-value-creation.md#halaman-pdf-513) mendefinisikan CFROI sebagai pendekatan IRR dan membahas penyederhanaan yang mendekatkannya pada indikator akuntansi. Persamaan99 pada versi telaah merupakan kerangka IRR; gross cash flow/GCE tetap dapat dibaca sebagai cash yield sederhana, bukan formula CFROI asli yang lengkap."]
out += ["","## Cara menjalankan ulang","","Jalankan scripts/build_formula_supplement.py setelah generator buku. Data asumsi dan perubahan tersedia pada data/formula-supplement-review.json. Originals dipertahankan byte demi byte; PDF dan LaTeX lampiran tetap versi awal, sehingga koreksi berlaku pada Markdown versi telaah ini."]
reviewed="\n".join(out).rstrip()+"\n"
assert [int(n) for n in re.findall(r"\\tag\{(\d+)\}",reviewed)]==list(range(1,151))
(BOOK/"53-kompilasi-rumus.md").write_text(reviewed,encoding="utf-8")
# Add/update navigation in all 50 chapter files, preserving page source text.
for c in chapters:
    p=BOOK/f'{c["slug"]}.md'
    text=p.read_text(encoding="utf-8")
    text=re.sub(r"\n*<!-- formula-supplement:start -->.*?<!-- formula-supplement:end -->\n*","\n\n",text,flags=re.S)
    ids=[i for i,s in enumerate(config["sections"],1) if c["number"] in s["chapters"]]
    links=" · ".join(f'[S{i:02d}](53-kompilasi-rumus.md#s{i:02d})' for i in ids)
    if not links: links="[Kompilasi dan peta keterkaitan](53-kompilasi-rumus.md)"
    block="<!-- formula-supplement:start -->\n## Pelengkap rumus dan pembahasan\n\n"+links+f' · [Catatan belajar Indonesia](../study/{c["slug"]}.md) · [Koreksi dan asumsi](54-catatan-koreksi-rumus.md)'+"\n\nBagian ini adalah pelengkap; teks hasil ekstraksi halaman buku dimulai di bawah.\n<!-- formula-supplement:end -->\n\n"
    text=text.replace("## Halaman PDF ",block+"## Halaman PDF ",1)
    p.write_text(text,encoding="utf-8")
# Directory landing page.
rows=["# Corporate Finance Fourth Edition — teks buku dan pelengkap","","[Kompilasi 150 persamaan: versi telaah](53-kompilasi-rumus.md) · [Daftar koreksi](54-catatan-koreksi-rumus.md) · [Lampiran asli](supplements/README.md) · [Daftar isi utama](../../SUMMARY.md)","","| Bab | Teks sumber | Catatan Indonesia |","| --- | --- | --- |"]
for c in chapters:
    rows.append(f'| {c["number"]} | [{c["title"]}]({c["slug"]}.md) | [Pelajari](../study/{c["slug"]}.md) |')
rows += ["","[Pengantar dan simbol](00-front-matter.md) · [Epilog](51-epilogue.md) · [Referensi historis dan indeks](52-reference-matter.md)","","Seluruh halaman 1–997 memiliki rujukan. Teks adalah hasil ekstraksi; simbol atau grafik yang tidak terbaca tetap dirujuk ke PDF. Kompilasi pelengkap tidak mengubah teks sumber menjadi versi akuntansi atau hukum yang diperbarui."]
(BOOK/"README.md").write_text("\n".join(rows)+"\n",encoding="utf-8")
# Original file identities and checksums for audit, with no signed URLs.
files=[]
for filename in ["kompilasi_rumus_corporate_finance.md","kompilasi_rumus_corporate_finance.tex","kompilasi_rumus_corporate_finance.pdf"]:
    path=BOOK/"supplements"/filename
    raw=path.read_bytes()
    files.append(dict(path=path.relative_to(R).as_posix(),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
(R/"data/formula-supplement-manifest.json").write_text(json.dumps(dict(originals=files,numbered_equations=150,sections=31,rewritten_equations=sorted(map(int,config["replacements"]))),indent=2)+"\n",encoding="utf-8")
# Navigation outside source pages.
nav="* [Kompilasi 150 persamaan — versi telaah](docs/book/53-kompilasi-rumus.md)\n* [Koreksi dan asumsi kompilasi](docs/book/54-catatan-koreksi-rumus.md)\n"
summary=R/"SUMMARY.md"
t=summary.read_text(encoding="utf-8")
t=re.sub(r"\n*<!-- formula-nav:start -->.*?<!-- formula-nav:end -->\n*","\n\n",t,flags=re.S)
t=t.replace("## Catatan belajar Indonesia","<!-- formula-nav:start -->\n"+nav+"<!-- formula-nav:end -->\n\n## Catatan belajar Indonesia",1)
summary.write_text(t,encoding="utf-8")
print(json.dumps(dict(equations=150,sections=31,rewritten=len(config["replacements"]),chapters_linked=50,original_files=len(files))))
