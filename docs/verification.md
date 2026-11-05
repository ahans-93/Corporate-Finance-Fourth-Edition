# Cakupan dan status verifikasi

Tanggal penyusunan: 5 November 2026.

## Yang diproses dan disediakan

| Pemeriksaan/cakupan | Hasil |
| --- | --- |
| Identitas | Corporate Finance: Theory and Practice, Fourth Edition; Wiley 2014, diperiksa pada PDF 5–6 |
| Sumber | CoreCourseFinancialAccounting.pdf, 997 halaman |
| Kelengkapan rentang | Halaman PDF 1–997 dipetakan tepat sekali, tanpa celah atau tumpang tindih |
| Hasil ekstraksi | 2.516.009 karakter dari pemrosesan seluruh halaman |
| Berkas sumber | 53: pengantar, 50 bab, epilog, dan materi referensi |
| Catatan belajar | 50 bab; sekitar 10.000 kata sebelum dokumen tambahan |
| Formula/kerangka utama | Satu entri per bab, ditambah formula lanjutan |
| Latihan pendamping | 50 pertanyaan dan pembahasan; contoh numerik/kasus dalam setiap bab |
| Integritas PDF | Checksum SHA-256 dicatat pada manifest dan diuji |
| Navigasi | Tautan lokal, struktur bab, pasangan formula, dan cakupan halaman diuji oleh validator |
| Perhitungan | Contoh numerik terpilih dan kasus terintegrasi diuji dengan skrip terpisah |

Lihat [manifest](../data/extraction-manifest.json) untuk checksum teks setiap halaman dan daftar berkas. Jalankan validator untuk memperoleh hasil pengujian pada versi lokal; laporan ini menjelaskan cakupan, bukan pengganti hasil eksekusi.

## Halaman tanpa teks hasil ekstraksi

Halaman PDF **1, 2, 314, 882, 940, 948, dan 966** tidak menghasilkan teks. Halaman tersebut tetap memiliki entri dalam dokumentasi dan tautan PDF. Tidak adanya teks tidak dinyatakan sebagai bukti halaman benar-benar kosong; dapat berupa pemisah atau materi gambar.

## Batas pemeriksaan

- Ekstraksi otomatis tidak menjamin bentuk persamaan, superscript, subscript, kolom, atau urutan tabel sama dengan PDF.
- Gambar dan grafik tidak dikonversi menjadi uraian data baru. PDF asli mempertahankan tampilan sumber.
- Catatan berbahasa Indonesia merangkum dan menjelaskan tema tiap bab; bukan terjemahan lengkap atau klaim audit manual setiap kalimat buku.
- Seluruh soal asli belum dihitung ulang satu per satu. Teks soal dan jawaban sumber dapat dibaca pada bab terkait, sedangkan latihan pendamping jelas dibedakan.
- Pengujian numerik memeriksa contoh yang dicantumkan di skrip, bukan semua angka dan persamaan sumber.
- Akuntansi, regulasi, dan statistik buku adalah konteks 2014. Penyesuaian analitis untuk valuasi berbeda dari jurnal yang diakui dalam laporan keuangan.

## Mengulangi pemeriksaan

~~~sh
python scripts/finance_examples.py
python scripts/validate_docs.py
~~~

Validator mengembalikan status gagal jika menemukan tautan lokal hilang, celah cakupan halaman, perubahan PDF, bab hilang, formula tidak berpasangan, atau hasil hitung yang tidak sesuai toleransi.
