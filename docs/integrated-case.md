# Kasus terintegrasi: operasi, kas, dan nilai

Kasus baru ini menghubungkan bab 2–5, 8–14, 16–19, 27–31, dan 35–39. Seluruh angka bersifat ilustratif dalam **juta rupiah**. Tarif pajak 25% dan biaya modal adalah asumsi latihan, bukan tarif yang dinyatakan berlaku.

## 1. Investasi dan asumsi operasi

Pada tanggal penilaian, aset tetap operasi bersih 500 dan modal kerja operasi 100, sehingga capital employed awal 600. Utang keuangan bersih 200 dan ekuitas buku 400. Tidak ada aset nonoperasi, NCI, instrumen dilutif, atau klaim tambahan.

Penjualan tahun 1–3 adalah 1.000, 1.100, dan 1.210. Biaya variabel 60% penjualan, biaya tetap operasi kas 200 per tahun, depresiasi 50 per tahun, dan capex 60 per tahun. Modal kerja akhir tahun adalah 10% penjualan. Semua arus kas ditempatkan pada akhir tahun.

## 2. Laporan laba operasi

| Komponen | Tahun 1 | Tahun 2 | Tahun 3 |
| --- | ---: | ---: | ---: |
| Penjualan | 1.000,00 | 1.100,00 | 1.210,00 |
| Biaya variabel | (600,00) | (660,00) | (726,00) |
| Biaya tetap kas | (200,00) | (200,00) | (200,00) |
| EBITDA | 200,00 | 240,00 | 284,00 |
| Depresiasi | (50,00) | (50,00) | (50,00) |
| EBIT | 150,00 | 190,00 | 234,00 |
| Pajak operasi ilustratif 25% | (37,50) | (47,50) | (58,50) |
| NOPAT | 112,50 | 142,50 | 175,50 |

Pertumbuhan penjualan 10% tidak sama dengan pertumbuhan EBIT. Biaya tetap membuat margin operasi meningkat dari 15% ke 17,27% dan 19,34%. Jangan mengekstrapolasi kenaikan margin tanpa batas: kapasitas dan biaya tetap pada akhirnya dapat berubah.

## 3. Jembatan menjadi FCFF

$$
FCFF=NOPAT+Depresiasi-Capex-\Delta WC
$$

| Komponen | Tahun 1 | Tahun 2 | Tahun 3 |
| --- | ---: | ---: | ---: |
| Modal kerja awal | 100,00 | 100,00 | 110,00 |
| Modal kerja akhir | 100,00 | 110,00 | 121,00 |
| Kenaikan modal kerja | 0,00 | 10,00 | 11,00 |
| NOPAT | 112,50 | 142,50 | 175,50 |
| Tambah depresiasi | 50,00 | 50,00 | 50,00 |
| Kurang capex | (60,00) | (60,00) | (60,00) |
| Kurang kenaikan modal kerja | 0,00 | (10,00) | (11,00) |
| **FCFF** | **102,50** | **122,50** | **154,50** |

Bunga dan pokok utang tidak dikurangkan di sini karena FCFF adalah arus kas sebelum pembagian kepada penyandang modal. Pajak yang digunakan adalah pajak operasi tanpa pengaruh bunga.

## 4. Hasil atas modal dan leverage

Untuk menunjukkan identitas leverage dengan mudah, gunakan modal **awal tahun** secara konsisten: ROCE tahun 1 = 112,5/600 = 18,75%. Bila biaya utang bersih sebelum pajak 8%, bunga bersih tahun 1 adalah 16 dan biaya setelah pajak 12.

Laba bersih sederhana = 112,5 − 12 = 100,5. ROE berbasis ekuitas awal = 100,5/400 = 25,125%. Identitas:

$$
ROE=18,75\%+(18,75\%-6\%)\times\frac{200}{400}=25,125\%
$$

Untuk menilai performa operasional, modal rata-rata sering lebih representatif. Capital employed akhir tahun 1 = 510 + 100 = 610, sehingga ROCE berbasis rata-rata = 112,5/605 = 18,595%. Jangan mencampur return berbasis awal dengan return berbasis rata-rata dalam satu identitas.

## 5. Biaya modal

Asumsi valuasi memakai **struktur target nilai pasar**: 60% ekuitas, 40% utang, kE 14%, kD 8%, dan T 25%.

$$
WACC=0,60(14\%)+0,40(8\%)(1-25\%)=10,8\%
$$

Struktur target ini merupakan asumsi kebijakan jangka panjang, bukan bobot modal buku 400:200 dan bukan hasil pembagian utang saat ini dengan EV yang nanti diperoleh. Pada model nyata, kebijakan refinancing dan leverage harus direkonsiliasikan dengan asumsi WACC; bila leverage sangat berubah, APV atau model periode dapat lebih tepat.

## 6. Terminal value yang mendanai pertumbuhan

Asumsikan mulai tahun 4 bisnis masuk kondisi stabil: pertumbuhan NOPAT 3% dan return marginal atas investasi baru 15%. NOPAT tahun 4 = 175,5 × 1,03 = 180,765.

Pertumbuhan membutuhkan reinvestasi:

$$
Reinvestment\ Rate=\frac{g}{ROIC_{new}}=\frac{3\%}{15\%}=20\%
$$

Reinvestasi bersih = 180,765 × 20% = 36,153; FCFF tahun 4 = 180,765 − 36,153 = **144,612**. Angka ini sengaja tidak diperoleh dengan sekadar menaikkan FCFF tahun 3 sebesar 3% karena kebutuhan reinvestasi normal berubah.

$$
TV_3=\frac{144,612}{10,8\%-3\%}=1.854
$$

g < WACC adalah syarat matematika; asumsi pertumbuhan, reinvestasi, dan keuntungan bersaing juga harus masuk akal secara ekonomi.

## 7. Enterprise value dan ekuitas

$$
EV_0=\frac{102,5}{1,108}+\frac{122,5}{1,108^2}+\frac{154,5+1.854}{1,108^3}=1.668,857
$$

Nilai ekuitas = EV − utang bersih = **1.468,857**. Jika membeli operasi dengan pengorbanan 600 pada awal periode, NPV ilustratif = EV − 600 = **1.068,857**. Ini contoh matematika, bukan rekomendasi harga transaksi.

Terminal value memiliki kontribusi besar terhadap nilai. Penilaian sangat bergantung pada daya tahan margin, return marginal, reinvestasi, dan biaya modal.

## 8. Sensitivitas dan kemampuan bayar

Dengan arus kas serta g yang sama tetapi WACC 12,8%, EV turun menjadi **1.322,929**. Perubahan dua poin persentase biaya modal mengubah nilai secara material.

Arus kas operasi untuk pelunasan utang tidak otomatis sama dengan EBITDA. Jika kontrak secara ilustratif memakai CFADS setara FCFF tahun 1 sebesar 102,5, bunga 16 dan pokok 40, DSCR = 102,5/56 = **1,8304×**. Pada transaksi nyata, ikuti definisi CFADS kontrak dan perbedaan pajak, cadangan, serta capex yang diperbolehkan.

## 9. Keputusan manajemen

- Uji apakah kenaikan margin membutuhkan tambahan kapasitas yang belum masuk capex.
- Pantau piutang dan persediaan; penjualan yang naik dapat menyerap kas lebih besar dari rencana.
- Pertahankan kas minimum dan fasilitas yang bisa ditarik sebelum menetapkan distribusi.
- Jelaskan sumber return di atas biaya modal; jangan hanya menunjukkan hasil spreadsheet.
- Rekonsiliasikan book capital, market value, utang aktual, dan target struktur pendanaan.
- Uji downside penjualan, margin, collection, bunga, dan refinancing secara bersamaan.

## 10. Latihan lanjutan

**Jika modal kerja akhir tahun 2 dan 3 naik menjadi 15% penjualan, apa pengaruhnya?** Saldo akhir menjadi 165 dan 181,5. Dengan saldo awal tahun 2 sebesar 100, kenaikan WC tahun 2 = 65 dan tahun 3 = 16,5. FCFF tahun 2 turun dari 122,5 menjadi 67,5; tahun 3 turun dari 154,5 menjadi 149. Jika perubahan kebijakan itu permanen, terminal reinvestment dan return marginal juga harus ditinjau ulang.

**Jika ROIC marginal terminal sama dengan WACC, apakah pertumbuhan otomatis menambah nilai?** Dalam kerangka yang konsisten, pertumbuhan pada investasi baru dengan return tepat sebesar required return tidak memberikan NPV tambahan atas investasi baru. Pertumbuhan laba tanpa memodelkan reinvestasi akan melebihkan nilai.
