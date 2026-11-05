# Bab 20: Obligasi, yield, duration, dan convexity

**Judul sumber:** Bonds. **Cetak mulai:** 349. **PDF:** 365–386.

[Teks sumber](../book/20-bonds.md) · [PDF](../../CoreCourseFinancialAccounting.pdf#page=365) · [Daftar isi](../../SUMMARY.md)

> Catatan pendamping Indonesia. Contoh adalah ilustrasi baru, bukan soal asli atau terjemahan resmi. Pajak dan bunga adalah asumsi latihan, bukan tarif aktual.

## Konsep dan penalaran

Obligasi adalah jadwal pembayaran kontraktual yang nilainya dipengaruhi tingkat diskonto, kredit, likuiditas, senioritas, dan opsi yang melekat. Coupon rate menentukan pembayaran nominal, sedangkan YTM adalah IRR pada harga yang dibayar dengan asumsi pembayaran sesuai kontrak. Harga obligasi bunga tetap turun ketika yield naik. Duration mengukur waktu tertimbang nilai kini dan sensitivitas orde pertama; convexity memperbaiki pendekatan untuk perubahan yield lebih besar. Floating-rate debt tetap mempunyai risiko kredit dan perubahan spread.

## Rumus atau kerangka analisis

$$
P=\sum_{t=1}^{N}\frac{C}{(1+y)^t}+\frac{F}{(1+y)^N} \qquad D_{mod}=\frac{D_{Mac}}{1+y} \qquad \frac{\Delta P}{P}\approx-D_{mod}\Delta y
$$

C = kupon tahunan; F = pokok; y = yield per tahun; Macaulay duration = jumlah t×PV(CFt) dibagi P. Bentuk ini untuk pembayaran tahunan tanpa opsi.

## Contoh dan langkah perhitungan

Pokok 100, kupon 5, tenor dua tahun, yield 6%. Harga = 5/1,06 + 105/1,06² = 98,1666. Macaulay duration ≈ 1,9520 tahun; modified duration ≈ 1,8415. Yield naik 1 poin persentase memberi estimasi harga turun sekitar 1,84%.

## Implikasi keputusan

Bandingkan total arus kas, yield, spread, risiko gagal bayar, serta ketentuan call/put, bukan hanya kupon.

## Kesalahan yang perlu dihindari

Menyamakan kupon dengan yield atau memakai duration untuk perubahan spread dan opsi tanpa meninjau asumsi.

## Uji pemahaman

**Pertanyaan:** Mengapa obligasi berkupon rendah cenderung lebih sensitif terhadap bunga?

**Pembahasan:** Lebih banyak nilai dibayarkan di masa depan sehingga waktu tertimbang dan duration cenderung lebih panjang.

## Lanjut membaca

Teks sumber memuat subbagian, soal, jawaban, dan bibliografi pada rentang halaman bab sesuai hasil ekstraksi. Cocokkan simbol, grafik, dan tabel dengan PDF asli.

[Bab sebelumnya](./19-the-required-rate-of-return.md)

[Bab berikutnya](./21-other-debt-products.md)
