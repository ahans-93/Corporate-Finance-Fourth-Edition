# Excel Functions for Financial Modelling & Valuation

Panduan berbahasa Indonesia untuk mengolah transaksi, menyusun proyeksi keuangan, dan membangun valuasi arus kas terdiskonto di Excel.

**Sumber utama** — Nishant Sharma, *Excel Functions for Financial Modelling & Valuation*, dengan lampiran *Excel Functions & Formulas* sepanjang 11 halaman. [Tautan pendek LinkedIn](https://lnkd.in/p/gEnfb5Qz) · [Posting asli](https://www.linkedin.com/posts/nishant-sharma-financial-modelling-mbafinance2325_excel-function-pdf-ugcPost-7525740778501951490-qsQ-/).

**Cakupan telaah** — Posting, daftar fungsi pada sampul, dan isi halaman 1–5 berhasil dibaca. Daftar pada sampul memuat 31 entri fungsi, termasuk `MODE` yang diperkenalkan sebagai `MODE.SNGL` pada halaman 2. Dokumentasi ini membahas semua entri tersebut dengan contoh baru dan referensi Microsoft. Isi halaman 6–11 belum dapat diperiksa langsung. Bagian proyeksi dan valuasi mengembangkan penerapan fungsi dengan contoh mandiri.

## Daftar isi

1. [Data latihan dan cara membaca rumus](#1-data-latihan-dan-cara-membaca-rumus)
2. [Katalog 31 fungsi](#2-katalog-31-fungsi)
3. [Dari transaksi ke proyeksi](#3-dari-transaksi-ke-proyeksi)
4. [Studi kasus valuasi DCF](#4-studi-kasus-valuasi-dcf)
5. [NPV, XNPV, IRR, dan XIRR](#5-npv-xnpv-irr-dan-xirr)
6. [Pemeriksaan model dan latihan](#6-pemeriksaan-model-dan-latihan)
7. [Rujukan](#7-rujukan)

## 1. Data latihan dan cara membaca rumus

Salin tabel ke Excel mulai dari A1. Masukkan tanggal sebagai nilai tanggal Excel. Untuk kolom F, biarkan F3 dan F6 benar-benar kosong dan masukkan rumus `=""` pada F7. Seluruh nominal dalam satuan juta rupiah, kecuali kolom unit dan jika dinyatakan lain.

| A — Proyek | B — Tagihan | C — Unit | D — Status | E — Tanggal | F — Bukti |
|---|---:|---:|---|---|---|
| P-01 | 120 | 10 | Lunas | 2026-01-03 | B-101 |
| P-02 | 150 | 12 | Terbuka | 2026-01-15 | |
| P-01 | 180 | 12 | Lunas | 2026-01-28 | B-103 |
| P-03 | 90 | 9 | Lunas | 2026-02-02 | B-104 |
| P-02 | 210 | 15 | Terbuka | 2026-02-16 | |
| P-01 | 150 | 12 | Terbuka | 2026-02-28 | `=""` |

Buat tabel proyek di H1:J4 dengan kolom Kode, Nama, dan Manajer.

| Kode | Nama | Manajer |
|---|---|---|
| P-01 | Renovasi | Tim A |
| P-02 | Infrastruktur | Tim B |
| P-03 | Interior | Tim C |

Untuk contoh pencarian horizontal, isi H7:J7 dengan `P-01`, `P-02`, `P-03` dan H8:J8 dengan `Renovasi`, `Infrastruktur`, `Interior`.

- `B2` bergeser saat disalin. `$B$2` mengunci baris dan kolom. `$B2` mengunci kolom. `B$2` mengunci baris.
- Contoh memakai koma antarargumen dan titik desimal. Jika Excel memakai titik koma antarargumen dan koma desimal, `=ROUNDUP(12.341,2)` ditulis `=ROUNDUP(12,341;2)`.
- Tulis kriteria teks dengan tanda kutip. Untuk operator yang memakai nilai sel, gabungkan operator dan sel, misalnya `">="&H12`.
- Gunakan tanggal Excel atau `DATE(2026,1,1)` untuk batas periode agar hasil konsisten dengan pengaturan regional.

## 2. Katalog 31 fungsi

### Agregasi, statistik, dan kelengkapan data

| Fungsi dan sintaks | Contoh | Hasil | Penerapan dan pemeriksaan |
|---|---|---|---|
| `SUM(number1,[number2],…)` | `=SUM(B2:B7)` | 900 | Menjumlahkan nilai tagihan. Rekonsiliasi ke buku pembantu dan periksa angka yang tersimpan sebagai teks. |
| `AVERAGE(number1,[number2],…)` | `=AVERAGE(B2:B7)` | 150 | Menghitung rata-rata per transaksi. Nol numerik ikut dihitung. Untuk harga rata-rata per unit, gunakan total nilai dibagi total unit. |
| `MEDIAN(number1,[number2],…)` | `=MEDIAN(B2:B7)` | 150 | Mengukur nilai tengah. Dapat membantu menilai tagihan tipikal atau kelipatan valuasi setelah sampel disaring. |
| `MODE.SNGL(number1,[number2],…)` | `=MODE.SNGL(C2:C7)` | 12 | Menemukan jumlah unit yang paling sering muncul. Fungsi lama bernama `MODE`. Jika semua nilai unik, hasilnya `#N/A`. |
| `COUNT(value1,[value2],…)` | `=COUNT(E2:E7)` | 6 | Menghitung entri numerik. Tanggal yang valid dihitung karena Excel menyimpannya sebagai angka. |
| `COUNTA(value1,[value2],…)` | `=COUNTA(F2:F7)` | 4 | Menghitung sel berisi nilai, termasuk galat dan hasil rumus berupa teks kosong. |
| `COUNTBLANK(range)` | `=COUNTBLANK(F2:F7)` | 3 | Menghitung sel kosong dan sel dengan hasil rumus `""`. Nol numerik tetap dianggap terisi. |
| `MAX(number1,[number2],…)` | `=MAX(B2:B7)` | 210 | Menunjukkan eksposur terbesar per baris. Tambahkan pemeriksaan jumlah data jika rentang bisa kosong. |
| `MAXIFS(max_range,criteria_range1,criteria1,…)` | `=MAXIFS(B2:B7,D2:D7,"Lunas")` | 180 | Menemukan tagihan terbesar yang lunas. Periksa jumlah kecocokan sebelum mengartikan hasil nol. |
| `MIN(number1,[number2],…)` | `=MIN(B2:B7)` | 90 | Menunjukkan transaksi terkecil. Untuk menilai anomali, identifikasi terlebih dahulu retur atau koreksi bertanda negatif. |
| `MINIFS(min_range,criteria_range1,criteria1,…)` | `=MINIFS(B2:B7,A2:A7,"P-02")` | 150 | Menemukan nilai terendah untuk P-02. Pastikan rentang nilai dan kriteria berdimensi sama. |

F7 dihitung oleh `COUNTA` dan `COUNTBLANK` sekaligus. Untuk memeriksa bukti yang benar-benar tersedia, sesuaikan aturan dengan kebutuhan model, termasuk perlakuan terhadap spasi, nomor bukti duplikat, dan galat formula.

### Logika, kondisi, dan pembulatan

| Fungsi dan sintaks | Contoh | Hasil | Penerapan dan pemeriksaan |
|---|---|---|---|
| `IF(logical_test,value_if_true,[value_if_false])` | `=IF(B2>=150,"Tinjau","Normal")` | Normal | Menandai transaksi yang mencapai ambang review. Letakkan ambang pada sel asumsi untuk model yang digunakan berulang. |
| `SUMIF(range,criteria,[sum_range])` | `=SUMIF(A2:A7,"P-01",B2:B7)` | 450 | Menjumlahkan tagihan per proyek. Seluruh rentang harus mulai pada baris data yang sama. |
| `COUNTIF(range,criteria)` | `=COUNTIF(D2:D7,"Terbuka")` | 3 | Menghitung tagihan terbuka. Untuk kode yang harus unik, cek `COUNTIF(kolom_kode,kode)=1`. |
| `COUNTIFS(criteria_range1,criteria1,…)` | `=COUNTIFS(A2:A7,"P-01",D2:D7,"Lunas")` | 2 | Menghitung baris yang memenuhi semua syarat. Gunakan untuk memeriksa pasangan kunci seperti proyek dan nomor invoice. |
| `AVERAGEIF(range,criteria,[average_range])` | `=AVERAGEIF(A2:A7,"P-02",B2:B7)` | 180 | Rata-rata tagihan satu proyek. Periksa apakah ada angka yang memenuhi syarat sebelum memakai hasilnya. |
| `AVERAGEIFS(average_range,criteria_range1,criteria1,…)` | `=AVERAGEIFS(B2:B7,A2:A7,"P-01",D2:D7,"Lunas")` | 150 | Rata-rata dengan banyak syarat. Rentang nilai berada di argumen pertama. |
| `IFERROR(value,value_if_error)` | `=IFERROR(B2/0,"Periksa pembagi")` | Periksa pembagi | Memberi pesan pada keluaran laporan. Gunakan pemeriksaan input agar galat sumber seperti `#REF!` tetap dapat ditelusuri. |
| `ROUNDUP(number,num_digits)` | `=ROUNDUP(12.341,2)` | 12,35 | Membulatkan menjauhi nol. Untuk kebutuhan kapasitas, misalnya 10,1 rit menjadi 11 rit. Angka negatif makin jauh dari nol. |
| `ROUNDDOWN(number,num_digits)` | `=ROUNDDOWN(12.349,2)` | 12,34 | Membulatkan menuju nol. Untuk alokasi unit penuh, gunakan digit 0. Digit negatif membulatkan di kiri tanda desimal. |

Simpan presisi penuh sepanjang proyeksi. Terapkan pembulatan pada keluaran atau pada tahap yang diwajibkan aturan transaksi. Uji kembali total setelah setiap baris dibulatkan.

### Tanggal dan jadwal

| Fungsi dan sintaks | Contoh | Hasil | Penerapan dan pemeriksaan |
|---|---|---|---|
| `TODAY()` | `=TODAY()` | Tanggal saat dihitung | Cocok untuk laporan umur piutang yang bergerak. Untuk tutup buku, simpan tanggal cut-off sebagai input tetap. |
| `DAY(serial_number)` | `=DAY(E2)` | 3 | Mengambil hari dalam bulan, misalnya untuk mengecek jadwal penagihan. |
| `MONTH(serial_number)` | `=MONTH(E2)` | 1 | Mengambil nomor bulan. Gabungkan dengan tahun atau gunakan tanggal awal bulan saat merangkum data lintas tahun. |
| `YEAR(serial_number)` | `=YEAR(E2)` | 2026 | Mengambil tahun kalender. Tahun buku yang mulai di bulan lain memerlukan aturan tambahan. |
| `NOW()` | `=NOW()` | Tanggal dan jam saat dihitung | Berguna untuk penanda kalkulasi terkini. Untuk cap waktu audit yang tetap, simpan nilai tanggal dan jam saat peristiwa terjadi. |
| `EOMONTH(start_date,months)` | `=EOMONTH(E2,1)` | 28 Februari 2026 | Membentuk kalender akhir bulan. Offset 0 memakai bulan berjalan dan offset negatif kembali ke bulan sebelumnya. |

### Pencarian dan referensi dinamis

| Fungsi dan sintaks | Contoh | Hasil | Penerapan dan pemeriksaan |
|---|---|---|---|
| `VLOOKUP(lookup_value,table_array,col_index_num,[range_lookup])` | `=VLOOKUP("P-02",$H$2:$J$4,2,FALSE)` | Infrastruktur | Kunci berada pada kolom pertama. Gunakan `FALSE` untuk kode dan cek indeks kolom setelah struktur tabel berubah. |
| `HLOOKUP(lookup_value,table_array,row_index_num,[range_lookup])` | `=HLOOKUP("P-03",$H$7:$J$8,2,FALSE)` | Interior | Mencari kode pada baris pertama. Untuk periode, gunakan tanggal yang konsisten di header dan nilai pencarian. |
| `INDEX(array,row_num,[column_num])` | `=INDEX($I$2:$I$4,3)` | Interior | Mengambil nilai berdasarkan posisi relatif dalam rentang. Indeks 1 menunjuk elemen pertama. |
| `MATCH(lookup_value,lookup_array,[match_type])` | `=MATCH("P-02",$H$2:$H$4,0)` | 2 | Mengembalikan posisi relatif. Mode 0 cocok persis dan mengembalikan kecocokan pertama bila ada duplikasi. |
| `OFFSET(reference,rows,cols,[height],[width])` | `=SUM(OFFSET($B$2,0,0,3,1))` | 450 | Menjumlahkan tiga baris pertama dari B2. Untuk ukuran jendela yang berubah, validasi tinggi dan batas rentang. |

Gabungkan `INDEX` dan `MATCH` untuk menarik atribut proyek tanpa bergantung pada posisi kolom relatif terhadap kunci.

```excel
=INDEX($J$2:$J$4,MATCH(A2,$H$2:$H$4,0))
```

Hasilnya **Tim A**. Bila kunci hilang, Excel mengembalikan `#N/A`. Jika kode harus unik, cek tabel master terlebih dahulu karena pencarian yang berhasil juga bisa berasal dari kunci duplikat. `OFFSET` bersifat volatil. Pada model besar, Excel Table atau rentang dengan batas `INDEX` dapat mengurangi kalkulasi ulang yang tidak perlu.

## 3. Dari transaksi ke proyeksi

### Rekap aktual per bulan

Dengan H12 berisi tanggal **1 Januari 2026**, rekap total tagihan Januari menggunakan `SUMIFS` sebagai fungsi tambahan.

```excel
=SUMIFS($B$2:$B$7,$E$2:$E$7,">="&H12,$E$2:$E$7,"<"&(EOMONTH(H12,0)+1))
```

Hasil Januari **450** dan Februari **450**. Batas akhir eksklusif juga mencakup transaksi di hari terakhir yang memuat jam. Total tagihan **900**. Tagihan berstatus terbuka **510** dan berstatus lunas **390**. Gunakan tanggal penerimaan dan nominal pembayaran aktual untuk menyusun arus kas, terutama jika ada cicilan. Tetapkan periode pengakuan pendapatan dengan data operasional dan kebijakan akuntansi yang berlaku pada entitas.

### Proyeksi berbasis penggerak bisnis

| Pos | Rumus model | Contoh satu periode |
|---|---|---:|
| Pendapatan | Volume × harga per unit | 1.200 × 1,5 = 1.800 |
| Biaya variabel | Volume × biaya per unit | 1.200 × 0,8 = 960 |
| Beban tetap | Jadwal beban operasional | 400 |
| EBITDA | Pendapatan − biaya variabel − beban tetap | 440 |
| EBIT | EBITDA − depresiasi dan amortisasi | 440 − 60 = 380 |
| NOPAT | EBIT × (1 − tarif pajak model) | 380 × (1 − 25%) = 285 |
| FCFF | NOPAT + depresiasi/amortisasi − belanja modal − kenaikan modal kerja operasi | 285 + 60 − 120 − 30 = 195 |

EBITDA adalah laba sebelum bunga, pajak, depresiasi, dan amortisasi. EBIT adalah laba sebelum bunga dan pajak. NOPAT adalah laba operasi setelah pajak dan FCFF adalah arus kas bebas untuk perusahaan. Tarif 25% adalah asumsi latihan.

Tautkan volume dan harga ke asumsi skenario, lalu rekonsiliasi perkalian ke rincian produk atau proyek. Untuk model bulanan, gunakan hari periode yang sesuai saat menerjemahkan asumsi umur piutang, persediaan, dan utang ke saldo. Hitung perubahan modal kerja operasi dari saldo akhir dikurangi saldo awal. Jika saldo operasi naik 30, dampaknya pada FCFF adalah minus 30. Definisi pos operasi harus konsisten antarperiode.

Untuk meneruskan proyeksi ke tiga laporan keuangan, hubungkan EBIT dan beban pembiayaan ke laba rugi, perubahan saldo operasi ke arus kas, serta belanja modal dan depresiasi ke jadwal aset tetap. Hitung kas akhir dari kas awal ditambah arus kas operasi, investasi, dan pendanaan. Tautkan kas akhir ke neraca dan periksa bahwa aset dikurangi liabilitas serta ekuitas menghasilkan nol.

## 4. Studi kasus valuasi DCF

Gunakan lembar terpisah. Kasus ini memiliki tiga arus kas akhir tahun. Biaya modal rata-rata tertimbang (WACC) sebesar 10%, pertumbuhan stabil terminal 3%, utang berbunga 300, dan kas berlebih 80. Seluruh angka dalam juta rupiah.

| Sel atau rentang | Input atau formula | Hasil |
|---|---|---:|
| B2:D2 | Tahun 1, 2, dan 3 | 1, 2, 3 |
| B3:D3 | FCFF tahunan | 100, 120, 140 |
| B6 | WACC | 10% |
| B7 | Pertumbuhan stabil | 3% |
| B8 | Utang berbunga | 300 |
| B9 | Kas berlebih | 80 |
| B10 | `=IF(B6>B7,D3*(1+B7)/(B6-B7),NA())` | 2.060,00 |
| B11 | `=NPV(B6,B3:D3)` | 295,27 |
| B12 | `=B10/(1+B6)^D2` | 1.547,71 |
| B13 | `=SUM(B11:B12)` | 1.842,98 |
| B14 | `=B13-B8+B9` | 1.622,98 |
| B15 | `=B12/B13` | 83,98% |

- **WACC** memakai bobot nilai pasar dari sumber pendanaan. Dalam contoh struktur utang dan ekuitas, `WACC = bobot ekuitas × biaya ekuitas + bobot utang × biaya utang sebelum pajak × (1 − tarif pajak)`. Gunakan asumsi mata uang dan basis nominal atau riil yang konsisten dengan proyeksi.
- **Nilai terminal** merepresentasikan arus kas setelah periode proyeksi. Pembilang menggunakan FCFF tahun berikutnya. Pertumbuhan jangka panjang perlu konsisten dengan investasi ulang dan imbal hasil atas modal pada fase stabil. Uji kondisi WACC lebih besar dari pertumbuhan.
- **Nilai operasi perusahaan** adalah nilai kini FCFF eksplisit dan nilai terminal. Untuk memperoleh nilai ekuitas, kurangi utang dan klaim lain yang relevan serta tambahkan kas berlebih atau aset nonoperasi. Periksa konsistensi tanggal dan hindari menghitung pos yang sama dua kali.
- **Sensitivitas** menunjukkan besarnya dampak asumsi. Dalam kasus ini, sekitar 84% nilai operasi berasal dari nilai terminal sehingga perubahan asumsi terminal berdampak besar.

Tabel sensitivitas nilai operasi dalam juta rupiah.

| WACC | Pertumbuhan 2% | Pertumbuhan 3% | Pertumbuhan 4% |
|---:|---:|---:|---:|
| 9% | 1.876,10 | 2.156,66 | 2.549,45 |
| 10% | 1.636,36 | 1.842,98 | 2.118,46 |
| 11% | 1.450,01 | 1.607,82 | 1.810,73 |

Untuk mereplikasi tabel, letakkan tingkat pertumbuhan di H19:J19, WACC di G20:G22, dan rumus berikut di H20. Salin ke seluruh area hasil.

```excel
=IF($G20>H$19,NPV($G20,$B$3:$D$3)+$D$3*(1+H$19)/($G20-H$19)/(1+$G20)^$D$2,NA())
```

## 5. NPV, XNPV, IRR, dan XIRR

Keempat fungsi di bagian ini adalah penerapan tambahan. Untuk proyek dengan investasi awal 1.000 dan penerimaan 600 pada akhir tahun pertama serta kedua, masukkan `-1000`, `600`, dan `600` di B20:B22.

| Kebutuhan | Rumus | Pemeriksaan |
|---|---|---|
| Nilai kini bersih untuk jarak periode tetap | `=B20+NPV(10%,B21:B22)` | 41,32. Investasi saat awal dinilai tanpa diskonto. |
| Tingkat pengembalian per periode | `=IRR(B20:B22)` | Sekitar 13,07% per tahun karena arus kas berjarak tahunan. |
| Nilai kini bersih memakai tanggal | `=XNPV(10%,B20:B22,A20:A22)` | Masukkan tanggal nyata pada A20:A22. Tanggal pertama menjadi tanggal dasar. |
| Tingkat pengembalian tahunan memakai tanggal | `=XIRR(B20:B22,A20:A22)` | Uji nilai hasil dengan memasukkannya sebagai tingkat diskonto pada `XNPV`. Hasilnya mendekati nol. |

Untuk mereplikasi hasil periodik dengan tanggal, isi A20:A22 dengan 1 Januari 2026, 1 Januari 2027, dan 1 Januari 2028. Kedua selang masing-masing 365 hari. Jika pembayaran maju atau mundur, nilai `XNPV` dan `XIRR` mengikuti jarak tanggal tersebut.

Pastikan arus kas bertanda positif dan negatif untuk perhitungan tingkat pengembalian. Jika tanda arus kas berubah lebih dari sekali, periksa kemungkinan beberapa tingkat pengembalian dengan menguji nilai kini pada sejumlah tingkat diskonto. Bandingkan proyek menggunakan nilai kini pada biaya modal yang relevan, sambil memperhatikan ukuran investasi dan waktu penerimaan.

## 6. Pemeriksaan model dan latihan

| Pemeriksaan | Cara menguji | Ekspektasi |
|---|---|---|
| Total dan periode | Jumlahkan rekap Januari dan Februari, lalu kurangi total tabel transaksi. | Selisih nol. |
| Pemetaan | Uji kode baru dan kode duplikat pada master proyek. | Kode baru ditandai dan duplikasi diperiksa sebelum dipakai. |
| Kualitas tanggal | Bandingkan `COUNT(E2:E7)` dengan jumlah baris transaksi. | Enam tanggal numerik pada contoh. |
| Kualitas data bukti | Bandingkan sel kosong, hasil `""`, dan nomor bukti yang benar-benar tercatat. | Tiga baris tanpa bukti yang terlihat. |
| Tanda FCFF | Naikkan belanja modal atau modal kerja masing-masing 10. | FCFF turun 10 jika asumsi lain tetap. |
| Sensitivitas | Tahan pertumbuhan 3% dan naikkan WACC dari 10% ke 11%. | Nilai operasi turun dari 1.842,98 ke 1.607,82. |
| Asumsi terminal | Samakan WACC dengan pertumbuhan. | Formula nilai terminal mengembalikan `#N/A`. |
| Konsistensi valuasi | Diskontokan setiap FCFF satu per satu dan bandingkan hasilnya dengan `NPV`. | Nilai kini FCFF eksplisit sekitar 295,27. |

Latihan tambahan dengan jawaban:

1. Berapa tagihan P-01 yang masih terbuka? **150**. Gunakan `SUMIFS` dengan kriteria proyek dan status.
2. Berapa nilai tagihan rata-rata per unit di seluruh tabel? **900 ÷ 70 = 12,8571**. Gunakan `SUM(B2:B7)/SUM(C2:C7)`.
3. Berapa nilai ekuitas bila kas berlebih naik dari 80 menjadi 100 dan komponen lain tetap? **1.642,98**.
4. Apa efek perubahan FCFF tahun terakhir dari 140 ke 150 dengan WACC dan pertumbuhan tetap? Nilai operasi naik sekitar **118,06**, karena kenaikan memengaruhi FCFF eksplisit dan nilai terminal.

## 7. Rujukan

- Nishant Sharma, [Excel Functions for Financial Modelling & Valuation](https://lnkd.in/p/gEnfb5Qz), lampiran *Excel Functions & Formulas*.
- Microsoft Support, [Daftar fungsi Excel menurut abjad](https://support.microsoft.com/id-id/excel/excel-functions-alphabetical) dan [fungsi COUNTBLANK](https://support.microsoft.com/en-us/excel/functions/countblank-function).
- Microsoft Support, [Memilih NPV, XNPV, IRR, XIRR atau MIRR di Excel](https://support.microsoft.com/en-us/excel/go-with-the-cash-flow-calculate-npv-and-irr-in-excel) dan [fungsi XNPV](https://support.microsoft.com/en-us/excel/functions/xnpv-function).
- Microsoft Learn, [Kinerja penghitungan Excel dan fungsi volatil](https://learn.microsoft.com/en-us/office/vba/excel/concepts/excel-performance/excel-improving-calculation-performance).
- Aswath Damodaran, NYU Stern, [DCF Valuation Package](https://pages.stern.nyu.edu/adamodar/pdfiles/eqnotes/dcfval.pdf).
