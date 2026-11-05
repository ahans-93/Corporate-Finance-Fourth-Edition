# Corporate Finance Fourth Edition

**Corporate Finance: Theory and Practice — Pierre Vernimmen dan tim, Wiley, 2014.**

Dokumentasi untuk membaca buku, menelusuri sumber per halaman, dan mempelajari konsep keuangan perusahaan dalam bahasa Indonesia.

## Mulai membaca

- [Daftar isi seluruh buku dan catatan 50 bab](SUMMARY.md)
- [Panduan membaca](docs/reading-guide.md)
- [Indeks subbagian, soal, dan jawaban asli](docs/source-index.md)
- [Indeks rumus utama](docs/formulas.md)
- [Rumus lanjutan dan asumsi](docs/advanced-formulas.md)
- [50 latihan pendamping beserta pembahasan](docs/exercises.md)
- [Kasus terintegrasi: laporan keuangan sampai valuasi](docs/integrated-case.md)
- [Glosarium](docs/glossary.md)
- [PDF asli, 997 halaman](CoreCourseFinancialAccounting.pdf)
- [Peta sumber](docs/source-map.md) dan [status verifikasi](docs/verification.md)

## Isi repository

| Bagian | Isi |
| --- | --- |
| docs/book | Teks bahasa Inggris hasil ekstraksi 997 halaman, dibagi 50 bab serta pengantar, epilog, dan referensi |
| docs/study | 50 catatan Indonesia: konsep, formula, asumsi, contoh/kasus, implikasi, kekeliruan, dan uji pemahaman |
| docs/formulas.md | Indeks formula/kerangka utama per bab |
| docs/advanced-formulas.md | Formula tambahan: anuitas, FCFE, APV, duration, opsi, dan lainnya |
| data | Peta bab, data catatan yang dapat diproses, manifest halaman dan checksum |
| scripts | Generator dokumentasi dan validasi struktur serta contoh perhitungan |
| SUMMARY.md | Navigasi Markdown untuk GitHub dan impor GitBook |
| .gitbook.yaml | Konfigurasi root, beranda, dan daftar isi GitBook |

PDF sumber sudah ada di repository dan dipertahankan tanpa perubahan. Judul buku telah diperiksa pada halaman judul; nama file PDF tidak mencerminkan judul sebenarnya.

## Menggunakan di GitBook

Dokumentasi sudah dapat dibaca langsung di GitHub. Jika repository ini dihubungkan melalui Git Sync pada GitBook, gunakan root repository; beranda dan daftar isi sudah ditentukan dalam konfigurasi. Belum ada situs GitBook atau GitHub Pages yang dipublikasikan oleh pekerjaan ini.

## Menjalankan ulang

Dengan Python dan dependensi pada requirements.txt:

~~~sh
python -m pip install -r requirements.txt
python scripts/build_docs.py
python scripts/build_source_index.py
python scripts/finance_examples.py
python scripts/validate_docs.py
~~~

Generator akan membangun ulang teks sumber, catatan, indeks rumus, latihan, peta sumber, dan daftar isi dari PDF serta data JSON. Berkas pendamping yang ditulis manual dipertahankan.

## Ketelitian dan cakupan

Teks merupakan ekstraksi otomatis, bukan edisi digital yang sudah disunting ulang setiap simbolnya. PDF tetap menjadi acuan untuk formula bertingkat, tabel, grafik, dan halaman tanpa teks terbaca. Catatan Indonesia merupakan materi pendamping baru; tidak diklaim sebagai terjemahan resmi atau pemeriksaan independen setiap rumus dan seluruh soal asli. Rincian cakupan dan pengujian tersedia pada [status verifikasi](docs/verification.md).

Pembahasan standar akuntansi, hukum, data pasar, dan produk dalam buku mengikuti konteks edisi 2014. Angka pajak dan bunga pada latihan adalah asumsi pembelajaran. Hak atas buku tetap pada penulis dan penerbit.
