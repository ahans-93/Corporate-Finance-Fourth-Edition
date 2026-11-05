# Catatan koreksi dan batas penggunaan kompilasi rumus

Versi telaah: [kompilasi 150 persamaan](53-kompilasi-rumus.md). Nomor di bawah merujuk kompilasi yang diberikan, bukan penomoran buku asli.

## Perubahan terhadap 23 persamaan

| Nomor | Perbaikan | Alasan |
| --- | --- | --- |
| 2 | EBITDA dikurangi pajak kas operasi dan ΔWCR dilabeli OCF unlevered analitis | Tidak otomatis sama dengan CFO laporan arus kas; klasifikasi bunga dan pajak dapat berbeda |
| 3 | Rekonsiliasi NI ke CFO memasukkan penyesuaian nonkas dan reklasifikasi | Penambahan depresiasi/amortisasi/provisi saja belum selalu lengkap |
| 4 | CAF memperjelas unsur beban/penghasilan nonkas dan laba pelepasan | Hindari menyamakan kapasitas autofinansial dengan CFO setelah modal kerja; laba pelepasan jangan dikurangi dua kali |
| 5–6 | D&A menggantikan depresiasi saja | Amortisasi yang relevan ikut diperhitungkan, dengan penyesuaian nonkas lain bila diperlukan |
| 7 | Value added menggunakan produksi dikurangi konsumsi eksternal | Produksi dapat berbeda dari penjualan; pembelian dapat berbeda dari konsumsi |
| 8 | Pajak operasi selain pajak laba dan posisi subsidi diperjelas | Hindari penghilangan biaya atau penghitungan subsidi dua kali |
| 9 | Pos nonkas operasi yang belum diperhitungkan diberi batas | Provisi/impairment tidak boleh dikurangkan kembali jika sudah masuk EBITDA |
| 13 | WCR memasukkan aset lancar operasi lain | Definisi sebelumnya hanya menambah kewajiban operasi lain |
| 17 | Net debt memakai seluruh utang keuangan relevan dan kas eligible | Utang keuangan tidak terbatas pada pinjaman bank jangka pendek; restricted cash tidak otomatis tersedia |
| 38 | Label margin menjadi NOPAT margin | Pembilang sesudah pajak tidak sama dengan EBIT margin |
| 54 | Penyebut MIRR menjadi −PV dari cash flow negatif | Penyebut rasio pangkat harus positif dalam struktur MIRR biasa |
| 95–96 | EV–equity bridge menambah other claims | Preferred equity atau klaim lain perlu diperiksa; perimeter harus konsisten |
| 99 | CFROI ditulis sebagai persamaan IRR yang diselesaikan | Gross cash flow/gross capital adalah cash yield sederhana, bukan CFROI asli yang lengkap |
| 111 | P/E disamakan basis forward EPS dan forward net income | Earnings dan saham pembanding harus konsisten periode serta atribusinya |
| 125 | Harga buyback dinamai harga pembelian kembali | Memperjelas label “Prepurchase Price” pada Markdown asal |
| 136 | Sinergi memakai PV arus kas tambahan dan PV biaya integrasi | Tambahan pendapatan bukan kas bebas; manfaat pendanaan harus dibuktikan, bukan diasumsikan gratis |
| 137 | Uses LBO memakai equity purchase price + debt repaid/refinanced + fees | EV sudah mencerminkan klaim operasi; menambahkan utang target lagi tanpa bridge bisa menghitungnya dua kali |
| 138 | MoIC mencakup seluruh kontribusi dan penerimaan ekuitas | Versi exit/entry saja tidak cukup bila ada distribusi atau setoran interim |
| 145 | CIP memasukkan tenor T dan konvensi quote | Formula satu tahun tidak langsung cocok untuk tenor tiga bulan |
| 147 | PPP dilabeli nilai model/ekspektasi, memakai simbol inflasi π | Tidak sama dengan harga forward kontraktual atau kepastian spot masa depan |
| 150 | Delta hedge menambah tanda posisi dan multiplier kontrak | Long option memerlukan arah hedge berlawanan dari short option |

Penyebutan 23 berasal dari jumlah ID persamaan yang diubah; beberapa baris tabel menggabungkan lebih dari satu ID. Semua ID 1–150 dipertahankan satu kali dalam versi telaah.

## Dua pemeriksaan langsung terhadap buku

### CFROI: bab 27

[Halaman PDF 513, cetak 497](../../CoreCourseFinancialAccounting.pdf#page=513) menjelaskan CFROI asli sebagai pendekatan internal rate of return dari investasi yang ada. Perhitungan memperhitungkan gross capital employed yang disesuaikan, cash flow, dan umur aset. Karena itu angka gross cash flow/GCE tidak boleh dipresentasikan sebagai definisi lengkap CFROI.

Kerangka IRR pada persamaan99 adalah penyajian analitis yang ditulis ulang; pemulihan aset nondepresiasi bila relevan harus dimodelkan konsisten dengan periode dan basis inflasi. Detail penyesuaian suatu implementasi CFROI dapat berbeda.

### Altman: bab 8, bukan persamaan tunggal untuk semua perusahaan

[Halaman PDF 152, cetak 136](../../CoreCourseFinancialAccounting.pdf#page=152) membahas Z-double-prime. Kompilasi awal menampilkan bentuk Z klasik dengan lima variabel dan mengaitkannya ke bab14. Bentuk klasik dipertahankan sebagai pelengkap, dengan penjelasan perbedaan varian dan rujukan tambahan ke bab8.

Koefisien dan denominator pada salinan konteks buku mengikuti teks sumber halaman tersebut, termasuk definisi X₄ yang dicetak di sana. Jangan mencampurkan definisi ini dengan versi dari publikasi lain. Skor tidak otomatis menjadi probabilitas gagal bayar.

## Asumsi penting yang ditambahkan

- Cash flow nominal dipasangkan rate nominal dengan mata uang sama; periode kupon, bunga, varians, dan horizon harus selaras.
- Perpetuitas tumbuh memerlukan r>g; growing annuity saat r=g menggunakan limit.
- Rumus MM dengan pajak, Hamada, dan Harris-Pringle memiliki asumsi tax shield serta kebijakan leverage yang berbeda.
- Black–Scholes yang ditampilkan adalah opsi Eropa tanpa dividen; vega/rho perlu konversi jika dilaporkan per poin persentase.
- MoIC tidak memperhitungkan waktu; IRR=(MoIC)^(1/n)−1 hanya untuk satu investasi awal dan satu penerimaan akhir.
- Interest-rate swap sederhana menggunakan kerangka satu kurva; transaksi modern dapat memerlukan beberapa kurva dan adjustment kredit.
- Cash model Baumol dan Miller–Orr adalah model pelengkap, bukan kebijakan treasury universal. Varians harian dipasangkan rate harian.
- Delta hedge mengurangi sensitivitas lokal; gamma, perubahan volatilitas, basis risk, likuiditas, dan biaya rebalancing tetap ada.

## Berkas asli dan versi telaah

[Lampiran asli](supplements/README.md) memuat Markdown, LaTeX, dan PDF yang diberikan. Ketiganya dipertahankan tanpa perubahan isi. PDF dan LaTeX tersebut **belum memuat koreksi versi telaah**. Untuk penggunaan analitis, baca Markdown versi telaah bersama penjelasannya.

Klaim “seluruh rumus dari 50 bab” pada dokumen asal adalah keterangan dokumen asal, bukan kesimpulan verifikasi repository. Menambahkan kompilasi tidak berarti seluruh persamaan dan soal buku telah diaudit satu per satu.

## Pengujian

Validasi tambahan memeriksa nomor persamaan 1–150 tanpa hilang/duplikat, 31 bagian, tautan ke bab, checksum ketiga lampiran asli, dan contoh numerik yang tercantum dalam skrip. Pengujian contoh bukan pembuktian bahwa setiap model sesuai untuk setiap kasus nyata.

~~~sh
python scripts/validate_formula_supplement.py
python scripts/validate_docs.py
~~~
