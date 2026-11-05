# Kompilasi rumus corporate finance — versi telaah

Pelengkap untuk buku Vernimmen edisi keempat. Disusun dari kompilasi yang Anda berikan, dengan nomor persamaan 1–150 dipertahankan agar perubahan mudah dibandingkan. Ada 31 kelompok bahasan, penjelasan asumsi, dan contoh. Nomor persamaan ini adalah nomor kompilasi, bukan nomor persamaan asli buku.

**Cakupan:** 23 persamaan ditulis ulang untuk memperjelas definisi, asumsi, tanda, atau cakupan. Ini bukan klaim bahwa seluruh persamaan buku telah diinventaris atau bahwa seluruh rumus kompilasi adalah kutipan literal dari 50 bab. Model pelengkap umum ditandai dalam catatan.

[Berkas asli Markdown](supplements/kompilasi_rumus_corporate_finance.md) · [LaTeX asli](supplements/kompilasi_rumus_corporate_finance.tex) · [PDF asli kompilasi](supplements/kompilasi_rumus_corporate_finance.pdf) · [Daftar koreksi](54-catatan-koreksi-rumus.md) · [Daftar buku](README.md)

## Navigasi

- [S01: Arus Kas & Free Cash Flow (Bab 2 & 5)](#s01)
- [S02: Analisis Laba & Pembentukan Nilai Tambah (Bab 3)](#s02)
- [S03: Modal Kerja & Neraca Capital Employed (Bab 4 & 11)](#s03)
- [S04: Rasio Perputaran Modal Kerja & Siklus Kas (Bab 11)](#s04)
- [S05: Margin, Risiko Operasi & Titik Impas (Bab 9 & 10)](#s05)
- [S06: Solvabilitas, Likuiditas & Struktur Utang (Bab 12)](#s06)
- [S07: Profitabilitas Modal & Formula Financial Leverage Vernimmen (Bab 13)](#s07)
- [S08: Model Prediksi Kebangkrutan Altman Z-Score (Bab 14)](#s08)
- [S09: Nilai Waktu Uang, Anuitas & Perpetuitas (Bab 16)](#s09)
- [S10: Tingkat Pengembalian Internal & YTM (Bab 17)](#s10)
- [S11: Teori Portofolio Markowitz & Pengukuran Risiko (Bab 18)](#s11)
- [S12: Model Penentuan Harga Aset Modal (CAPM) (Bab 19)](#s12)
- [S13: Penilaian Obligasi, Durasi & Konveksitas (Bab 20)](#s13)
- [S14: Penilaian Saham Biasa & DDM (Bab 22)](#s14)
- [S15: Teori Opsi & Model Black-Scholes-Merton (Bab 23)](#s15)
- [S16: Sekuritas Hibrida & Obligasi Konversi (Bab 24)](#s16)
- [S17: Enterprise Value & Nilai Ekuitas (Bab 26)](#s17)
- [S18: Metrik Penciptaan Nilai: EVA, MVA & CFROI (Bab 27)](#s18)
- [S19: Kriteria Keputusan Investasi (Bab 28)](#s19)
- [S20: Biaya Modal Rata-Rata Tertimbang (WACC) (Bab 29)](#s20)
- [S21: Teknik Valuasi Lengkap: DCF & Kelipatan Pasar (Bab 31)](#s21)
- [S22: Struktur Modal Modigliani-Miller (Bab 32 & 33)](#s22)
- [S23: Formula Hamada & Harris-Pringle (Bab 33)](#s23)
- [S24: Model Opsi Struktural Merton (Bab 34)](#s24)
- [S25: Dividen & Pembelian Saham Kembali (Bab 36 & 37)](#s25)
- [S26: Penerbitan Hak Memesan Efek (Rights Issue) (Bab 38)](#s26)
- [S27: Valuasi Modal Ventura & Dilusi Pendiri (Bab 40)](#s27)
- [S28: Merger, Akuisisi & Penilaian Sinergi (Bab 44 & 45)](#s28)
- [S29: Leveraged Buyout (LBO) (Bab 46)](#s29)
- [S30: Model Manajemen Saldo Kas Optimal (Bab 49)](#s30)
- [S31: Manajemen Risiko Pasar & Derivatif (Bab 50)](#s31)

## S01

**1.1 — Arus Kas & Free Cash Flow (Bab 2 & 5)**

[Bab 2: Cash flow](./02-cash-flow.md) · [Bab 5: Walking through from earnings to cash flow](./05-walking-through-from-earnings-to-cash-flow.md)

### Asumsi dan penjelasan

Bedakan arus kas operasi analitis tanpa pendanaan dari CFO pada laporan arus kas. Pajak kas, klasifikasi bunga, laba pelepasan aset, perubahan kurs, akuisisi, dan penyesuaian nonkas dapat memerlukan rekonsiliasi tambahan. D&A mencakup depresiasi dan amortisasi; kenaikan WCR menyerap kas.

### Persamaan

$$
\Delta \text{Cash} = \text{CFO} + \text{CFI} + \text{CFF} \tag{1}
$$

di mana CFO adalah arus kas aktivitas operasi, CFI adalah arus kas investasi, dan CFF adalah arus kas pendanaan.

**Arus Kas Operasi (CFO – Metode Tidak Langsung):**

$$
\text{OCF}_{unlevered,analytical}=\text{EBITDA}-\text{Cash Operating Taxes}-\Delta\text{WCR} \tag{2}
$$

atau secara alternatif dari laba bersih:

$$
\text{CFO}=\text{Net Income}+\text{Net Noncash Adjustments}+\text{Reclassification Adjustments}-\Delta\text{Operating WC} \tag{3}
$$

**Kapasitas Autofinansial (Cash Flow / CAF):**

$$
\text{CAF}=\text{Net Income}+\text{Noncash Charges}-\text{Noncash Income excluding Disposal Gains}-\text{Net Disposal Gains} \tag{4}
$$

**Free Cash Flow to Firm (FCFF):**

$$
\text{FCFF}=\text{EBIT}(1-T_c)+D\&A-\text{Capex}-\Delta\text{WCR} \tag{5}
$$

di mana $T_c$ adalah tarif pajak korporasi marjinal, dan Capex adalah belanja modal kotor.

**Free Cash Flow to Equity (FCFE):**

$$
\text{FCFE}=\text{Net Income}+D\&A-\text{Capex}-\Delta\text{WCR}+\text{New Debt}-\text{Principal Repaid} \tag{6}
$$

### Contoh penerapan

EBIT 200, pajak operasi 25%, D&A 40, capex 70, dan kenaikan WCR 30: FCFF = 200×75%+40−70−30 = 90. Jika laba bersih 120, D&A 40, capex 70, ΔWCR 30, dan net borrowing 20, FCFE = 80.

## S02

**1.2 — Analisis Laba & Pembentukan Nilai Tambah (Bab 3)**

[Bab 3: Earnings](./03-earnings.md)

### Asumsi dan penjelasan

Dalam laporan by-nature, produksi dapat berbeda dari penjualan karena perubahan persediaan produk jadi dan produksi yang dikapitalisasi. Pembelian perlu disesuaikan menjadi konsumsi. Subsidi, pajak operasi selain pajak penghasilan, dan provisi harus diperiksa agar tidak dihitung dua kali.

### Persamaan

**Format Laba Rugi By-Nature (Vernimmen Standar):**

$$
\text{VA}=\text{Production}-\text{External Consumption} \tag{7}
$$

$$
\text{EBITDA}=\text{VA}-\text{Personnel Costs}-\text{Other Operating Taxes}+\text{Subsidies not already included} \tag{8}
$$

$$
\text{EBIT}=\text{EBITDA}-D\&A-\text{Operating Impairment not already included} \tag{9}
$$

$$
\text{NOPAT} = \text{EBIT} \times (1 - T_c) \tag{10}
$$

$$
\text{EBT} = \text{EBIT} - \text{Net Financial Expense} + \text{Non-Operating Items} \tag{11}
$$

$$
\text{Net Income} = \text{EBT} - \text{Corporate Income Tax} \tag{12}
$$

### Contoh penerapan

Produksi 1.020 dan konsumsi eksternal 600 memberi value added 420. Biaya pegawai 200, pajak operasi lain 20, dan subsidi yang belum masuk produksi 10 memberi EBITDA 210. D&A 50 tanpa adjustment lain memberi EBIT 160.

## S03

**1.3 — Modal Kerja & Neraca Capital Employed (Bab 4 & 11)**

[Bab 4: Capital employed and invested capital](./04-capital-employed-and-invested-capital.md) · [Bab 11: Working capital and capital expenditures](./11-working-capital-and-capital-expenditures.md)

### Asumsi dan penjelasan

WCR harus memasukkan semua aset dan kewajiban operasi yang relevan. Identitas CE=E+net debt hanya benar setelah perimeter dan akun nonoperasi direkonsiliasi. Restricted cash atau aset keuangan yang tidak tersedia tidak otomatis dikurangkan dari utang.

### Persamaan

$$
\text{WCR}=\text{Inventories}+\text{Trade Receivables}+\text{Other Operating Current Assets}-\text{Trade Payables}-\text{Other Operating Current Liabilities} \tag{13}
$$

**Identitas Fundamental Neraca Fungsional:**

$$
\text{Capital Employed (CE)} = \text{Fixed Assets}_{\text{net}} + \text{WCR} \tag{14}
$$

$$
\text{Invested Capital} = \text{Shareholders' Equity} + \text{Net Financial Debt} \tag{15}
$$

$$
\text{Capital Employed} \equiv \text{Invested Capital} \tag{16}
$$

**Utang Finansial Bersih (Net Debt):**

$$
\text{Net Debt}=\text{Financial Debt}_{gross}-\text{Eligible Cash and Cash-like Financial Assets} \tag{17}
$$

### Contoh penerapan

Aset tetap 600, persediaan 150, piutang 200, aset lancar operasi lain 20, utang pemasok 120, dan kewajiban operasi lain 30: WCR=220; CE=820. Ekuitas 500 dan net debt 320 merekonsiliasi jumlah tersebut.

## S04

**1.4 — Rasio Perputaran Modal Kerja & Siklus Kas (Bab 11)**

[Bab 11: Working capital and capital expenditures](./11-working-capital-and-capital-expenditures.md) · [Bab 48: Managing working capital](./48-managing-working-capital.md)

### Asumsi dan penjelasan

Gunakan saldo rata-rata dan basis VAT yang sama dengan denominator. DPO menggunakan pembelian kredit, bukan selalu HPP. DIO berbasis HPP adalah konvensi operasional; buku juga menggunakan indikator persediaan terhadap penjualan yang tidak identik.

### Persamaan

$$
\text{DSO} = \frac{\text{Trade Receivables}}{\text{Sales (including VAT)}} \times 365 \tag{18}
$$

$$
\text{DIO} = \frac{\text{Inventories}}{\text{Cost of Goods Sold (COGS)}} \times 365 \tag{19}
$$

$$
\text{DPO} = \frac{\text{Trade Payables}}{\text{Purchases (including VAT)}} \times 365 \tag{20}
$$

$$
\text{CCC} = \text{DIO} + \text{DSO} - \text{DPO} \tag{21}
$$

$$
\text{Capex Intensity} = \frac{\text{Capex}}{\text{Annual Depreciation}} \tag{22}
$$

### Contoh penerapan

AR rata-rata 120 / penjualan kredit 1.200 ×365 = DSO 36,5 hari. Persediaan 80 / HPP 800 ×365 =36,5 hari. AP60 / pembelian600 ×365 =DPO36,5 hari. CCC=36,5 hari.

## S05

**1.5 — Margin, Risiko Operasi & Titik Impas (Bab 9 & 10)**

[Bab 9: Margin analysis: structure](./09-margin-analysis-structure.md) · [Bab 10: Margin analysis: risks](./10-margin-analysis-risks.md)

### Asumsi dan penjelasan

Formula titik impas dan DOL memerlukan harga, unit cost, bauran, serta biaya tetap yang stabil dalam rentang analisis. DOL tidak terdefinisi pada EBIT nol dan sensitif ketika dekat titik impas.

### Persamaan

$$
\text{Gross Margin} = \frac{\text{Sales} - \text{COGS}}{\text{Sales}}, \qquad \text{Operating Margin} = \frac{\text{EBIT}}{\text{Sales}} \tag{23}
$$

$$
\text{Contribution Margin (CM)} = \text{Sales} - \text{Variable Costs} \tag{24}
$$

$$
\text{CMR} = \frac{\text{Sales} - \text{Variable Costs}}{\text{Sales}} = \frac{\text{CM}}{\text{Sales}} \tag{25}
$$

$$
\text{BEP}_{\$} = \frac{\text{Fixed Costs}}{\text{CMR}} \tag{26}
$$

$$
\text{BEP}_{Q} = \frac{\text{Fixed Costs}}{P - \text{VC}_{\text{unit}}} \tag{27}
$$

$$
\text{Margin of Safety} = \frac{\text{Actual Sales} - \text{BEP Sales}}{\text{Actual Sales}} \tag{28}
$$

$$
\text{DOL} = \frac{\%\Delta \text{EBIT}}{\%\Delta \text{Sales}} = \frac{\text{Sales} - \text{VC}}{\text{EBIT}} = \frac{\text{CM}}{\text{EBIT}} \tag{29}
$$

### Contoh penerapan

Harga100, biaya variabel60, biaya tetap200.000: BEP5.000 unit. Pada6.000 unit, penjualan600.000, kontribusi240.000, EBIT40.000, margin of safety16,67%, DOL6.

## S06

**1.6 — Solvabilitas, Likuiditas & Struktur Utang (Bab 12)**

[Bab 12: Financing](./12-financing.md)

### Asumsi dan penjelasan

Covenant dan DSCR harus memakai definisi kontrak. Utang/EBITDA dan utang/CFO merupakan rasio ringkas, bukan jadwal pelunasan. Rasio current dan quick tidak menjamin saldo tersedia pada tanggal jatuh tempo.

### Persamaan

$$
\text{Gearing} = \frac{\text{Net Debt}}{\text{Equity}} \tag{30}
$$

$$
\text{Leverage Ratio} = \frac{\text{Net Debt}}{\text{EBITDA}} \tag{31}
$$

$$
\text{Interest Coverage Ratio (ICR)} = \frac{\text{EBIT}}{\text{Net Financial Interest Expense}} \tag{32}
$$

$$
\text{Debt Service Coverage Ratio (DSCR)} = \frac{\text{CFADS}}{\text{Principal Repayment} + \text{Interest Expense}} \tag{33}
$$

$$
\text{Debt Payback} = \frac{\text{Net Debt}}{\text{CFO}} \tag{34}
$$

$$
\text{Current Ratio} = \frac{\text{Current Assets}}{\text{Current Liabilities}} \tag{35}
$$

$$
\text{Quick Ratio} = \frac{\text{Cash} + \text{Marketable Securities} + \text{Receivables}}{\text{Current Liabilities}} \tag{36}
$$

### Contoh penerapan

Net debt600, EBITDA200 menghasilkan leverage3×. CFADS100, bunga30, pokok100 menghasilkan DSCR0,7692×. Cash shortfall tetap ada meskipun rasio leverage tidak tampak ekstrem.

## S07

**1.7 — Profitabilitas Modal & Formula Financial Leverage Vernimmen (Bab 13)**

[Bab 13: Return on capital employed and return on equity](./13-return-on-capital-employed-and-return-on-equity.md)

### Asumsi dan penjelasan

ROCE setelah pajak harus dipasangkan dengan biaya utang setelah pajak. Pilih modal awal atau rata-rata secara konsisten. NOPAT/Sales merupakan margin operasi setelah pajak, bukan EBIT margin sebelum pajak. Identitas leverage mengasumsikan struktur sederhana dan akun yang sudah direkonsiliasi.

### Persamaan

**Return on Capital Employed (ROCE):**

$$
\text{ROCE} = \frac{\text{EBIT} \times (1 - T_c)}{\text{Capital Employed}} \tag{37}
$$

**Dekomposisi DuPont ROCE:**

$$
\text{ROCE}=\underbrace{\frac{\text{EBIT}(1-T_c)}{\text{Sales}}}_{\text{NOPAT Margin}}\times\underbrace{\frac{\text{Sales}}{\text{CE}}}_{\text{Capital Turnover}} \tag{38}
$$

**Return on Equity (ROE):**

$$
\text{ROE} = \frac{\text{Net Income}}{\text{Shareholders' Equity}} \tag{39}
$$

**Formula Financial Leverage Vernimmen:**

$$
\text{ROE} = \text{ROCE} + (\text{ROCE} - i) \times \left(\frac{\text{Net Debt}}{\text{Equity}}\right) \tag{40}
$$

di mana $i$ adalah biaya utang bersih setelah pajak:

$$
i = \frac{\text{Net Financial Expense} \times (1 - T_c)}{\text{Net Debt}} \tag{41}
$$

> **Aturan Pengungkit Vernimmen:** Jika $\text{ROCE} > i$, penambahan utang mendongkrak ROE (efek pengungkit positif). Jika $\text{ROCE} < i$, utang memperberat beban keuangan dan menekan ROE di bawah ROCE (efek pengungkit negatif).

**Dekomposisi DuPont 3-Faktor Tradisional:**

$$
\text{ROE} = \underbrace{\left(\frac{\text{Net Income}}{\text{Sales}}\right)}_{\text{Net Profit Margin}} \times \underbrace{\left(\frac{\text{Sales}}{\text{Assets}}\right)}_{\text{Asset Turnover}} \times \underbrace{\left(\frac{\text{Assets}}{\text{Equity}}\right)}_{\text{Equity Multiplier}} \tag{42}
$$

### Contoh penerapan

CE1.000, E500, D500, NOPAT120, biaya utang setelah pajak6%: ROCE12%; NI90; ROE18%. Penurunan ROCE menjadi4% membuat ROE2%.

## S08

**1.8 — Model Prediksi Kebangkrutan Altman Z-Score (Bab 14)**

[Bab 8: How to perform a financial analysis](./08-how-to-perform-a-financial-analysis.md) · [Bab 14: Conclusion of financial analysis](./14-conclusion-of-financial-analysis.md)

### Asumsi dan penjelasan

Persamaan43 adalah varian Z klasik pada kompilasi, bukan persamaan Z-double-prime yang dibahas buku pada bab8. Jangan menukar koefisien, denominator, populasi, atau batas klasifikasi antarvarian. Skor bukan probabilitas gagal bayar dan tidak memberikan jaminan keamanan.

### Persamaan

$$
Z = 1.2X_1 + 1.4X_2 + 3.3X_3 + 0.6X_4 + 0.999X_5 \tag{43}
$$

dengan definisi rasio:

- $X_1 = \dfrac{\text{Working Capital}}{\text{Total Assets}}$
- $X_2 = \dfrac{\text{Retained Earnings}}{\text{Total Assets}}$
- $X_3 = \dfrac{\text{EBIT}}{\text{Total Assets}}$
- $X_4 = \dfrac{\text{Market Value of Equity}}{\text{Total Liabilities}}$
- $X_5 = \dfrac{\text{Sales}}{\text{Total Assets}}$

**Zona klasifikasi:**

| Nilai Z | Zona |
|---|---|
| $Z > 2.99$ | Zona Aman |
| $1.81 \le Z \le 2.99$ | Zona Waspada / Abu-Abu |
| $Z < 1.81$ | Zona Bahaya / Distress |

---

### Contoh penerapan

Untuk varian klasik dengan X1=.2, X2=.1, X3=.15, X4=1.5, X5=1.2, skor memakai koefisien0,999 adalah2,9738. Hasil hanya diinterpretasikan dalam konteks model dan sampel yang tepat.

### Bentuk yang dibahas buku pada bab 8

[PDF 152, halaman cetak 136](../../CoreCourseFinancialAccounting.pdf#page=152) menyajikan bentuk Z-double-prime berikut. Pertahankan definisi dan koefisien versi sumber; jangan mengganti denominator atau ambang dengan varian lain.

$$
Z''=6.6X_1+3.26X_2+6.72X_3+1.05X_4
$$

Pada uraian halaman tersebut, X₁=working capital/total assets; X₂=retained earnings/total assets; X₃=operating profit/total assets; X₄=shareholders' equity/net debt. Buku menyebut area rendah di bawah 1,1, area tinggi di atas 2,6, dan area antara keduanya. Ini adalah reproduksi konteks buku, bukan model kredit yang dikalibrasi untuk seluruh perusahaan.

## S09

**2.1 — Nilai Waktu Uang, Anuitas & Perpetuitas (Bab 16)**

[Bab 16: The time value of money and net present value](./16-the-time-value-of-money-and-net-present-value.md)

### Asumsi dan penjelasan

Tentukan apakah pembayaran akhir atau awal periode. Perpetuitas tumbuh memerlukan r>g; growing annuity ketika r=g harus memakai limit. Tingkat nominal dan efektif tidak boleh ditukar tanpa konversi.

### Persamaan

$$
\text{Future Value (FV)} = \text{PV} \times (1 + r)^n \tag{44}
$$

$$
\text{Present Value (PV)} = \frac{\text{FV}_n}{(1 + r)^n} = \text{FV}_n \times (1 + r)^{-n} \tag{45}
$$

$$
\text{Continuous Compounding}: \quad \text{FV} = \text{PV} \cdot e^{rt}, \qquad \text{PV} = \text{FV} \cdot e^{-rt} \tag{46}
$$

$$
\text{Effective Annual Rate (EAR)} = \left(1 + \frac{r_{\text{nom}}}{m}\right)^m - 1 \tag{47}
$$

**Anuitas Biasa (Ordinary Annuity):**

$$
\text{PV}_{\text{annuity}} = C \times \left[\frac{1 - (1 + r)^{-n}}{r}\right] \tag{48}
$$

$$
\text{FV}_{\text{annuity}} = C \times \left[\frac{(1 + r)^n - 1}{r}\right] \tag{49}
$$

**Perpetuitas (Perpetuity):**

$$
\text{PV}_{\text{perpetuity}} = \frac{C}{r} \tag{50}
$$

**Perpetuitas Bertumbuh (Gordon-Shapiro Perpetuity):**

$$
\text{PV}_{\text{growing perpetuity}} = \frac{C_1}{r - g} \qquad (r > g) \tag{51}
$$

**Anuitas Bertumbuh (Growing Annuity):**

$$
\text{PV} = \frac{C_1}{r - g}\left[1 - \left(\frac{1 + g}{1 + r}\right)^n\right] \tag{52}
$$

### Contoh penerapan

Anuitas100 pada akhir masing-masing3 tahun dengan r10% bernilai248,6852. Bunga nominal12% dengan compounding bulanan memberi EAR12,6825%.

## S10

**2.2 — Tingkat Pengembalian Internal & YTM (Bab 17)**

[Bab 17: The internal rate of return](./17-the-internal-rate-of-return.md)

### Asumsi dan penjelasan

Pada MIRR, denominator adalah nilai absolut present value cash flow negatif. IRR dapat memiliki beberapa akar jika tanda cash flow berubah lebih dari sekali. Untuk pilihan proyek saling meniadakan, utamakan NPV pada required return yang tepat.

### Persamaan

**Internal Rate of Return (IRR):**

$$
\sum_{t=0}^{n} \frac{\text{CF}_t}{(1 + \text{IRR})^t} = 0 \iff I_0 = \sum_{t=1}^{n} \frac{\text{CF}_t}{(1 + \text{IRR})^t} \tag{53}
$$

**Modified Internal Rate of Return (MIRR):**

$$
\text{MIRR}=\left[\frac{\text{FV of Positive Cash Flows}}{-\text{PV of Negative Cash Flows}}\right]^{1/n}-1 \tag{54}
$$

**Yield to Maturity Obligasi (YTM):**

$$
P = \sum_{t=1}^{n} \frac{C}{(1 + \text{YTM})^t} + \frac{M}{(1 + \text{YTM})^n} \tag{55}
$$

### Contoh penerapan

Cash flow−100,+230,−132 mempunyai IRR10% dan20%. Untuk MIRR−100,+60,+60 dengan reinvestment10% selama2 tahun, FV positif126 dan MIRR=sqrt(126/100)−1=12,2497%.

## S11

**2.3 — Teori Portofolio Markowitz & Pengukuran Risiko (Bab 18)**

[Bab 18: Risk and return](./18-risk-and-return.md)

### Asumsi dan penjelasan

Bobot, return, kovarians, dan horizon harus selaras. Formula varians dengan penjumlahan i≠j memang memuat dua arah pasangan. Diversifikasi mengurangi risiko spesifik, tetapi korelasi dapat berubah dalam kondisi stres.

### Persamaan

$$
E(R_p) = \sum_{i=1}^{N} w_i E(R_i) \qquad \text{dengan} \qquad \sum_{i=1}^{N} w_i = 1 \tag{56}
$$

$$
\sigma_i^2 = \sum_k p_k \left[R_{i,k} - E(R_i)\right]^2, \qquad \sigma_i = \sqrt{\sigma_i^2} \tag{57}
$$

$$
\text{Cov}(A, B) = \sigma_{AB} = \rho_{AB}\,\sigma_A\,\sigma_B \tag{58}
$$

$$
\rho_{AB} = \frac{\text{Cov}(A, B)}{\sigma_A \sigma_B}, \qquad -1 \le \rho_{AB} \le +1 \tag{59}
$$

**Varians Portofolio 2-Aset:**

$$
\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \rho_{AB} \sigma_A \sigma_B \tag{60}
$$

**Varians Portofolio N-Aset:**

$$
\sigma_p^2 = \sum_{i=1}^{N} w_i^2 \sigma_i^2 + \sum_{i=1}^{N} \sum_{j \ne i} w_i w_j \sigma_{ij} \tag{61}
$$

### Contoh penerapan

Dua aset berbobot50% dengan volatilitas20% dan korelasi0 memiliki volatilitas portofolio14,1421%, bukan rata-rata20%.

## S12

**2.4 — Model Penentuan Harga Aset Modal (CAPM) (Bab 19)**

[Bab 19: The required rate of return](./19-the-required-rate-of-return.md)

### Asumsi dan penjelasan

CAPM menghubungkan required return dengan beta, bukan volatilitas total. CML berlaku untuk portofolio efisien dalam asumsi model; bukan semua saham tunggal. Sharpe, Treynor, dan alpha memerlukan benchmark serta periode konsisten dan bukan jaminan performa.

### Persamaan

**Koefisien Beta ($\beta$):**

$$
\beta_i = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)} = \frac{\rho_{im}\,\sigma_i}{\sigma_m} \tag{62}
$$

**Persamaan Capital Asset Pricing Model (CAPM):**

$$
E(R_i) = R_f + \beta_i \left[E(R_m) - R_f\right] \tag{63}
$$

**Capital Market Line (CML):**

$$
E(R_p) = R_f + \left[\frac{E(R_m) - R_f}{\sigma_m}\right] \sigma_p \tag{64}
$$

**Ukuran Kinerja Portofolio:**

$$
\text{Sharpe Ratio} = \frac{E(R_p) - R_f}{\sigma_p} \tag{65}
$$

$$
\text{Treynor Ratio} = \frac{E(R_p) - R_f}{\beta_p} \tag{66}
$$

$$
\text{Jensen's Alpha}\ (\alpha_p) = R_p - \left[R_f + \beta_p (R_m - R_f)\right] \tag{67}
$$

### Contoh penerapan

rf4%, beta1,2, premi pasar6%: kE11,2%. Korelasi0,6, sigma saham30%, sigma pasar15% juga menghasilkan beta1,2.

## S13

**2.5 — Penilaian Obligasi, Durasi & Konveksitas (Bab 20)**

[Bab 20: Bonds](./20-bonds.md)

### Asumsi dan penjelasan

Rumus duration dan convexity yang ditampilkan menggunakan yield serta pembayaran per periode yang sama. Annualisasi dan frekuensi kupon harus dikoreksi jika bukan tahunan. Accrued interest memakai jumlah kupon per periode, bukan kupon tahunan bila ada beberapa pembayaran.

### Persamaan

$$
\text{Dirty Price} = \text{Clean Price} + \text{Accrued Interest} \tag{68}
$$

$$
\text{Accrued Interest} = C \times \left(\frac{\text{Days since last coupon}}{\text{Days in coupon period}}\right) \tag{69}
$$

**Macaulay Duration ($D$):**

$$
D = \frac{1}{P}\left[\sum_{t=1}^{n} \frac{t \cdot C}{(1 + y)^t} + \frac{n \cdot M}{(1 + y)^n}\right] \tag{70}
$$

**Modified Duration (MD):**

$$
\text{MD} = \frac{D}{1 + y} = -\frac{1}{P}\frac{dP}{dy} \tag{71}
$$

**Konveksitas (Convexity):**

$$
\text{Convexity} = \frac{1}{P(1 + y)^2} \sum_{t=1}^{n} \frac{t(t + 1) \cdot \text{CF}_t}{(1 + y)^t} \tag{72}
$$

**Aproksimasi Perubahan Harga Orde Kedua:**

$$
\frac{\Delta P}{P} \approx -\text{MD} \times \Delta y + \frac{1}{2} \times \text{Convexity} \times (\Delta y)^2 \tag{73}
$$

### Contoh penerapan

Obligasi nominal100, kupon5/tahun, tenor2 tahun, yield6%: harga98,1666. Dirty price101,25 dan accrued1,25 berarti clean price100.

## S14

**2.6 — Penilaian Saham Biasa & DDM (Bab 22)**

[Bab 22: Shares](./22-shares.md)

### Asumsi dan penjelasan

DDM harus sesuai kebijakan distribusi dan kemampuan membayar. Pertumbuhan g=b×ROE memerlukan asumsi reinvestasi serta leverage stabil. Dividen tahun depan, bukan dividen tahun lalu, dipakai dalam Gordon growth.

### Persamaan

$$
\text{Dividend Yield} = \frac{\text{DPS}_1}{P_0}, \qquad \text{Payout Ratio}\ (d) = \frac{\text{DPS}}{\text{EPS}}, \qquad b = 1 - d \tag{74}
$$

$$
g = b \times \text{ROE} = (1 - d) \times \text{ROE} \tag{75}
$$

**Model Gordon-Shapiro:**

$$
P_0 = \frac{\text{Div}_1}{k_E - g} \implies k_E = \frac{\text{Div}_1}{P_0} + g \tag{76}
$$

**Model Pertumbuhan Dua Tahap (Two-Stage DDM):**

$$
P_0 = \sum_{t=1}^{H} \frac{\text{Div}_t}{(1 + k_E)^t} + \frac{\text{Div}_{H+1}}{(k_E - g_2)(1 + k_E)^H} \tag{77}
$$

### Contoh penerapan

D1=5, kE12%, g2% memberi P0=50. Jika DPS2 dan EPS5, payout40%, retention60%; ROE15% memberi g ilustratif9%.

## S15

**2.7 — Teori Opsi & Model Black-Scholes-Merton (Bab 23)**

[Bab 23: Options](./23-options.md)

### Asumsi dan penjelasan

BSM di sini adalah opsi Eropa tanpa dividen dengan r kontinu dan volatilitas konstan. Greeks vega dan rho adalah turunan untuk perubahan1,00 pada parameter, bukan langsung per1 poin persentase. Theta perlu dibagi basis hari jika ingin ukuran harian.

### Persamaan

$$
\text{Call Payoff} = \max(0,\, S_T - K) \tag{78}
$$

$$
\text{Put Payoff} = \max(0,\, K - S_T) \tag{79}
$$

**Paritas Put-Call (Put-Call Parity):**

$$
C - P = S_0 - K e^{-rT} \tag{80}
$$

**Model Binomial Cox-Ross-Rubinstein (CRR):**

$$
u = e^{\sigma\sqrt{\Delta t}}, \qquad d = \frac{1}{u} = e^{-\sigma\sqrt{\Delta t}}, \qquad p = \frac{e^{r\Delta t} - d}{u - d} \tag{81}
$$

$$
C = e^{-r\Delta t}\left[p\, C_u + (1 - p)\, C_d\right] \tag{82}
$$

**Formula Black-Scholes-Merton (BSM):**

$$
C = S_0 N(d_1) - K e^{-rT} N(d_2) \tag{83}
$$

$$
P = K e^{-rT} N(-d_2) - S_0 N(-d_1) \tag{84}
$$

dengan parameter penentu:

$$
d_1 = \frac{\ln(S_0 / K) + \left(r + \dfrac{\sigma^2}{2}\right) T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T} \tag{85}
$$

**Turunan Greeks Opsi:**

$$
\Delta_{\text{call}} = N(d_1), \qquad \Delta_{\text{put}} = N(d_1) - 1 \tag{86}
$$

$$
\Gamma = \frac{N'(d_1)}{S_0 \sigma \sqrt{T}} \tag{87}
$$

$$
\nu = S_0 \sqrt{T}\, N'(d_1) \tag{88}
$$

$$
\Theta_{\text{call}} = -\frac{S_0 N'(d_1)\,\sigma}{2\sqrt{T}} - r K e^{-rT} N(d_2) \tag{89}
$$

$$
\rho_{\text{call}} = K T e^{-rT} N(d_2) \tag{90}
$$

### Contoh penerapan

S100,K100,r5%,sigma20%,T1: call10,4506, put5,5735. Put-call parity menghasilkan selisih4,8771. Vega≈37,5240 per1,00 sigma, atau0,37524 per1 poin persentase.

## S16

**2.8 — Sekuritas Hibrida & Obligasi Konversi (Bab 24)**

[Bab 24: Hybrid securities](./24-hybrid-securities.md)

### Asumsi dan penjelasan

Straight-bond floor memakai risiko kredit yang sebanding. Harga convertible juga dipengaruhi call, put, konversi paksa, dilusi, dan interaksi kredit dengan harga saham. Kupon rendah bukan bukti biaya pendanaan rendah.

### Persamaan

$$
\text{Conversion Ratio (CR)} = \frac{\text{Nominal Value of Convertible Bond}}{\text{Conversion Price (CP)}} \tag{91}
$$

$$
\text{Conversion Value} = \text{CR} \times S_0 \tag{92}
$$

$$
\text{Conversion Premium} = \frac{P_{\text{CB}} - \text{Conversion Value}}{\text{Conversion Value}} \times 100\% \tag{93}
$$

$$
\text{Bond Floor} = \sum_{t=1}^{n} \frac{C}{(1 + y_{\text{straight}})^t} + \frac{M}{(1 + y_{\text{straight}})^n} \tag{94}
$$

---

### Contoh penerapan

Nominal1.000 dan conversion price50 memberi rasio20 saham. Pada S60, nilai konversi1.200. Jika harga CB1.260, conversion premium5%.

## S17

**3.1 — Enterprise Value & Nilai Ekuitas (Bab 26)**

[Bab 26: Value and corporate finance](./26-value-and-corporate-finance.md) · [Bab 31: Valuation techniques](./31-valuation-techniques.md)

### Asumsi dan penjelasan

EV dan equity bridge harus sesuai perimeter cash flow. NCI, preferred equity, opsi, aset nonoperasi, dan klaim lain diperiksa satu per satu. Kas yang sudah masuk net debt tidak ditambahkan lagi sebagai aset nonoperasi.

### Persamaan

$$
\text{EV}=\text{Market Cap}+\text{Net Debt}+\text{NCI}+\text{Other Claims}-\text{Nonoperating Assets} \tag{95}
$$

$$
\text{Equity Value}=\text{EV}-\text{Net Debt}-\text{NCI}-\text{Other Claims}+\text{Nonoperating Assets} \tag{96}
$$

### Contoh penerapan

Market cap1.000+net debt300+NCI50+klaim lain20−aset nonoperasi40 memberi EV1.330. Rekonsiliasi balik menghasilkan ekuitas1.000.

## S18

**3.2 — Metrik Penciptaan Nilai: EVA, MVA & CFROI (Bab 27)**

[Bab 27: Measuring value creation](./27-measuring-value-creation.md)

### Asumsi dan penjelasan

CFROI asli dalam bab27 adalah pendekatan IRR atas gross capital employed yang disesuaikan dan arus kas umur aset, bukan sekadar gross cash flow/gross invested capital. Hubungan MVA dengan PV EVA memerlukan capital charge, reinvestasi, dan terminal yang konsisten.

### Persamaan

**Economic Value Added (EVA):**

$$
\text{EVA} = \text{NOPAT} - (\text{WACC} \times \text{Capital Employed}) = (\text{ROCE} - \text{WACC}) \times \text{Capital Employed} \tag{97}
$$

**Market Value Added (MVA):**

$$
\text{MVA} = \text{Market Value of Capital} - \text{Invested Capital} = \sum_{t=1}^{\infty} \frac{\text{EVA}_t}{(1 + \text{WACC})^t} \tag{98}
$$

**Cash Flow Return on Investment (CFROI):**

$$
\text{GCE}_0=\sum_{t=1}^{n}\frac{\text{Adjusted Aftertax Cash Flow}_t}{(1+\text{CFROI})^t}+\frac{\text{Nondepreciating Asset Recovery}_n}{(1+\text{CFROI})^n} \tag{99}
$$

**Economic Profit Ekuitas:**

$$
\text{Economic Profit} = \text{Net Income} - (k_E \times \text{Book Equity}) = (\text{ROE} - k_E) \times \text{Equity} \tag{100}
$$

### Contoh penerapan

GCE100 dengan adjusted cash flow60 pada akhir tahun1 dan60 pada akhir tahun2 menghasilkan IRR≈13,0662%. Rasio60/100=60% jelas bukan CFROI IRR tersebut. Lihat PDF513, cetak497.

**Penelusuran sumber:** [bab 27, PDF 513/cetak 497](27-measuring-value-creation.md#halaman-pdf-513) mendefinisikan CFROI sebagai pendekatan IRR dan membahas penyederhanaan yang mendekatkannya pada indikator akuntansi. Persamaan99 pada versi telaah merupakan kerangka IRR; gross cash flow/GCE tetap dapat dibaca sebagai cash yield sederhana, bukan formula CFROI asli yang lengkap.

## S19

**3.3 — Kriteria Keputusan Investasi (Bab 28)**

[Bab 28: Investment criteria](./28-investment-criteria.md)

### Asumsi dan penjelasan

PI dan EAA perlu asumsi yang tepat. EAA berguna untuk umur proyek berbeda jika layanan dan pola pengulangan sebanding. Sunk cost dikeluarkan, biaya peluang dan kebutuhan modal kerja dimasukkan.

### Persamaan

$$
\text{NPV} = -I_0 + \sum_{t=1}^{n} \frac{\text{CF}_t}{(1 + k)^t} \tag{101}
$$

$$
\text{Profitability Index (PI)} = \frac{\sum_{t=1}^{n} \frac{\text{CF}_t}{(1 + k)^t}}{I_0} = 1 + \frac{\text{NPV}}{I_0} \tag{102}
$$

$$
\text{Equivalent Annual Annuity (EAA)} = \frac{\text{NPV}}{\left[\dfrac{1 - (1 + k)^{-n}}{k}\right]} \tag{103}
$$

### Contoh penerapan

NPV30 selama3 tahun dengan k10% memiliki EAA=30/2,486852≈12,0634 per tahun. Investasi100 dengan PV inflow130 memiliki PI1,3.

## S20

**3.4 — Biaya Modal Rata-Rata Tertimbang (WACC) (Bab 29)**

[Bab 29: The cost of capital](./29-the-cost-of-capital.md)

### Asumsi dan penjelasan

Gunakan bobot nilai pasar/target. Jangan mempertahankan kE konstan saat leverage berubah. Tax shield memerlukan deductibility dan kapasitas pemanfaatan. Perpetual preferred cost=dividen/harga hanya untuk struktur preferen sederhana.

### Persamaan

$$
\text{WACC} = k_E\left(\frac{E}{D + E}\right) + k_D (1 - T_c)\left(\frac{D}{D + E}\right) \tag{104}
$$

dengan saham preferen:

$$
\text{WACC} = k_E\left(\frac{E}{V}\right) + k_p\left(\frac{P}{V}\right) + k_D (1 - T_c)\left(\frac{D}{V}\right) \tag{105}
$$

di mana $k_E = R_f + \beta_E\left[E(R_m) - R_f\right]$, dan $k_p = \dfrac{\text{Div}_p}{P_{\text{pref}}}$.

### Contoh penerapan

E/V60%,D/V40%,kE14%,kD8%,T25% memberi WACC10,8%. Nilai buku utang dan ekuitas tidak otomatis menjadi bobot pasar.

## S21

**3.5 — Teknik Valuasi Lengkap: DCF & Kelipatan Pasar (Bab 31)**

[Bab 31: Valuation techniques](./31-valuation-techniques.md)

### Asumsi dan penjelasan

FCFF dipasangkan WACC dan FCFE dipasangkan kE. Equity=EV−net debt adalah bentuk sederhana tanpa klaim/aset tambahan. P/E harus menggunakan earnings yang sebanding dengan EPS yang dipilih; PEG sensitif unit growth.

### Persamaan

**Enterprise DCF (Model FCFF):**

$$
\text{EV} = \sum_{t=1}^{N} \frac{\text{FCFF}_t}{(1 + \text{WACC})^t} + \frac{\text{TV}_N}{(1 + \text{WACC})^N} \tag{106}
$$

$$
\text{Terminal Value}\ (\text{TV}_N) = \frac{\text{FCFF}_{N+1}}{\text{WACC} - g} \tag{107}
$$

$$
\text{Equity Value} = \text{EV} - \text{Net Debt} \tag{108}
$$

**Equity DCF (Model FCFE):**

$$
\text{Equity Value} = \sum_{t=1}^{N} \frac{\text{FCFE}_t}{(1 + k_E)^t} + \frac{\text{TV}_{E,N}}{(1 + k_E)^N}, \qquad \text{TV}_{E,N} = \frac{\text{FCFE}_{N+1}}{k_E - g} \tag{109}
$$

**Adjusted Present Value (APV):**

$$
\text{APV} = \text{EV}_{\text{unlevered}} + \text{PV(Tax Shield)} - \text{PV(Bankruptcy Costs)} \tag{110}
$$

**Kelipatan Valuasi (Valuation Multiples):**

$$
\text{Forward P/E}=\frac{P_0}{\text{EPS}_1}=\frac{\text{Market Cap}_0}{\text{Forward Net Income attributable to the same shares}} \tag{111}
$$

$$
\text{PEG Ratio} = \frac{\text{P/E}}{\text{Annual EPS Growth Rate} \times 100} \tag{112}
$$

$$
\text{EV/EBITDA} = \frac{\text{Enterprise Value}}{\text{EBITDA}}, \qquad \text{EV/Sales} = \frac{\text{Enterprise Value}}{\text{Sales}} \tag{113}
$$

$$
\text{EV/CE} = \frac{\text{Enterprise Value}}{\text{Capital Employed}} \tag{114}
$$

---

### Contoh penerapan

FCFF tahun depan100, WACC10%,g3% memberi EV1.428,5714. Net debt350 tanpa adjustment lain memberi ekuitas1.078,5714. P/E15 dan growth10%=0,10 menghasilkan PEG1,5.

## S22

**4.1 — Struktur Modal Modigliani-Miller (Bab 32 & 33)**

[Bab 32: Capital structure and the theory of perfect capital markets](./32-capital-structure-and-the-theory-of-perfect-capital-markets.md) · [Bab 33: Capital structure, taxes and organisation theories](./33-capital-structure-taxes-and-organisation-theories.md)

### Asumsi dan penjelasan

VL=VU+TcD memerlukan asumsi tax shield utang permanen yang spesifik. Friksi distress, biaya transaksi, informasi, dan insentif tidak tercakup dalam formula MM sederhana. Utang murah menaikkan required return ekuitas.

### Persamaan

**Dunia Tanpa Pajak (MM 1958):**

$$
\text{Proposisi I}: \quad V_L = V_U \tag{115}
$$

$$
\text{Proposisi II}: \quad k_E = k_0 + (k_0 - k_D)\left(\frac{D}{E}\right) \tag{116}
$$

$$
\text{Asset Beta}: \quad \beta_A = \beta_E\left(\frac{E}{D + E}\right) + \beta_D\left(\frac{D}{D + E}\right) \tag{117}
$$

**Dunia Dengan Pajak Korporasi (MM 1963):**

$$
\text{Proposisi I}: \quad V_L = V_U + T_c \cdot D \tag{118}
$$

$$
\text{Proposisi II}: \quad k_E = k_0 + (k_0 - k_D)(1 - T_c)\left(\frac{D}{E}\right) \tag{119}
$$

### Contoh penerapan

Tanpa pajak, k0=10%,kD5%,D/E=2/3 memberi kE13,3333%. Dengan bobot60/40, WACC tetap10%.

## S23

**4.2 — Formula Hamada & Harris-Pringle (Bab 33)**

[Bab 29: The cost of capital](./29-the-cost-of-capital.md) · [Bab 33: Capital structure, taxes and organisation theories](./33-capital-structure-taxes-and-organisation-theories.md)

### Asumsi dan penjelasan

Hamada dan Harris-Pringle memakai asumsi berbeda mengenai kebijakan utang dan risiko tax shield. Label target leverage stabil saja belum cukup: cara dan frekuensi rebalancing harus dijelaskan. Jangan mencampur kedua formula dalam satu valuasi tanpa rekonsiliasi.

### Persamaan

**Formula Hamada (Relevering Beta, $\beta_D = 0$):**

$$
\beta_E = \beta_U\left[1 + (1 - T_c)\left(\frac{D}{E}\right)\right] \tag{120}
$$

$$
\beta_U = \frac{\beta_E}{1 + (1 - T_c)\left(\dfrac{D}{E}\right)} \tag{121}
$$

**Formula Harris-Pringle (Target Debt Ratio Stabil):**

$$
\beta_E = \beta_U + (\beta_U - \beta_D)\left(\frac{D}{E}\right) \tag{122}
$$

### Contoh penerapan

BetaU0,8,T25%,D/E0,5 memberi betaE Hamada1,1. Dalam pendekatan Harris-Pringle dengan betaD0,1, betaE=0,8+(0,8−0,1)×0,5=1,15.

## S24

**4.3 — Model Opsi Struktural Merton (Bab 34)**

[Bab 34: Debt, equity and options theory](./34-debt-equity-and-options-theory.md)

### Asumsi dan penjelasan

Merton sederhana memodelkan satu utang zero-coupon yang jatuh tempo T, aset mengikuti proses model, dan tanpa pembayaran antara. K adalah pembayaran utang pada jatuh tempo, bukan nilai pasar utang hari ini. Volatilitas aset berbeda dari volatilitas saham.

### Persamaan

$$
\text{Equity Value} = \text{Call}(V, K, T, \sigma_V, r) = V N(d_1) - K e^{-rT} N(d_2) \tag{123}
$$

$$
\text{Debt Value} = V - \text{Equity} = K e^{-rT} - \text{Put}(V, K, T, \sigma_V, r) \tag{124}
$$

### Contoh penerapan

Pada jatuh tempo, V130 dan K100 memberi equity30,debt100; V70 memberi equity0,debt70. Harga hari ini memerlukan diskonto dan distribusi risiko model.

## S25

**4.4 — Dividen & Pembelian Saham Kembali (Bab 36 & 37)**

[Bab 36: Returning cash to shareholders](./36-returning-cash-to-shareholders.md) · [Bab 37: Distribution in practice: dividends and share buy-backs](./37-distribution-in-practice-dividends-and-share-buybacks.md)

### Asumsi dan penjelasan

Jumlah saham dikurangi dana buyback dibagi harga pembelian kembali. EPS perlu laba yang sudah dikurangi biaya pendanaan setelah pajak. Ambang akresi berlaku dalam struktur sederhana dengan earnings positif dan parameter lain tetap; bukan uji penciptaan nilai.

### Persamaan

$$
N_{\text{new}}=N_{\text{old}}-\frac{\text{Buyback Funds}}{P_{\text{repurchase}}} \tag{125}
$$

$$
\text{EPS}_{\text{new}} = \frac{\text{Net Income} - \text{Foregone Cash Interest} \times (1 - T_c)}{N_{\text{new}}} \tag{126}
$$

> **Ambang Batas Akresi Buyback:** Pembelian kembali saham meningkatkan EPS jika dan hanya jika

$$
\text{P/E} < \frac{1}{r_{\text{cash}}(1 - T_c)}
$$

### Contoh penerapan

NI100,100 saham,harga10,dana buyback100,kehilangan bunga setelah pajak3 memberi saham90,NI97,EPS1,0778. Meskipun EPS naik, harga beli dapat terlalu mahal.

## S26

**4.5 — Penerbitan Hak Memesan Efek (Rights Issue) (Bab 38)**

[Bab 25: Selling securities](./25-selling-securities.md) · [Bab 38: Share issues](./38-share-issues.md)

### Asumsi dan penjelasan

Nilai hak dinyatakan per saham lama pada struktur tertentu. Investor yang menjual hak perlu memasukkan hasilnya ketika menilai dilusi ekonomi. Potensi opsi, kelas saham, fee, dan kondisi pasar dapat mengubah realisasi.

### Persamaan

$$
\text{TERP} = \frac{N \times P_0 + M \times S}{N + M} \tag{127}
$$

$$
R = P_0 - \text{TERP} = \frac{M \times (P_0 - S)}{N + M} = \frac{P_0 - S}{\dfrac{N}{M} + 1} \tag{128}
$$

$$
\text{Issue Discount} = \frac{P_0 - S}{P_0} \times 100\% \tag{129}
$$

---

### Contoh penerapan

Empat saham lama pada100 memperoleh hak membeli satu saham baru pada80. TERP96; hak per saham lama4; empat hak16 ditambah kas80 setara saham baru96.

## S27

**5.1 — Valuasi Modal Ventura & Dilusi Pendiri (Bab 40)**

[Bab 40: Setting up a company or financing start-ups](./40-setting-up-a-company-or-financing-startups.md)

### Asumsi dan penjelasan

Persentase dinyatakan sebagai fraksi dalam formula:20%=0,20. Post-money sederhana tidak memasukkan option-pool top-up, convertible, fee, dan liquidation preference. Nilai headline yang tinggi belum menjamin hak ekonomi yang lebih baik.

### Persamaan

$$
\text{Post-Money Valuation} = \text{Pre-Money Valuation} + \text{New Investment} \tag{130}
$$

$$
\text{Investor Ownership \%} = \frac{\text{New Investment}}{\text{Post-Money Valuation}} \tag{131}
$$

$$
\text{Founder Ownership \%}_{\text{new}} = \text{Founder Ownership \%}_{\text{old}} \times (1 - \text{Investor Ownership \%}) \tag{132}
$$

### Contoh penerapan

Pre-money8 miliar+investasi2 miliar=post-money10 miliar. Investor20%. Founder yang semula80% memegang80%×80%=64%, sebelum opsi atau konversi.

## S28

**5.2 — Merger, Akuisisi & Penilaian Sinergi (Bab 44 & 45)**

[Bab 44: Taking control of a company](./44-taking-control-of-a-company.md) · [Bab 45: Mergers and demergers](./45-mergers-and-demergers.md)

### Asumsi dan penjelasan

Sinergi harus berupa PV arus kas tambahan setelah pajak dan biaya realisasi. Manfaat pendanaan tidak otomatis merupakan nilai tambahan; periksa MM, pajak, dan friksi. Nilai sinergi berbeda dari premi yang diserahkan kepada penjual.

### Persamaan

$$
\text{Control Premium} = \frac{P_{\text{offer}} - P_{\text{unaffected}}}{P_{\text{unaffected}}} \times 100\% \tag{133}
$$

$$
\text{Exchange Ratio (ER)} = \frac{P_{\text{offer per target share}}}{P_{\text{acquirer share}}} \tag{134}
$$

$$
N_{\text{combined}} = N_{\text{acquirer}} + (N_{\text{target}} \times \text{ER}) \tag{135}
$$

$$
\text{Net Synergy}=\text{PV of Incremental Operating Cash Flows}+\text{PV of Justified Financing Benefits}-\text{PV of Integration Costs} \tag{136}
$$

### Contoh penerapan

Target standalone500,PV sinergi bersih100,harga570,biaya transaksi10 memberi NPV pembeli20. Harga impas maksimum590.

## S29

**5.3 — Leveraged Buyout (LBO) (Bab 46)**

[Bab 46: Leveraged buyouts (LBOs)](./46-leveraged-buyouts-lbos.md)

### Asumsi dan penjelasan

Jangan menambah seluruh refinancing ke EV tanpa menjembatani utang yang sudah tercermin di EV. Gunakan equity purchase price+utang yang dibayar/refinance+fees+funding lain. MoIC dan IRR sederhana hanya berlaku tanpa distribusi interim atau setoran tambahan.

### Persamaan

$$
\text{Equity Purchase Price}+\text{Debt Repaid or Refinanced}+\text{Fees}+\text{Other Funding Uses}=\text{New Debt}+\text{Sponsor Equity}+\text{Other Sources} \tag{137}
$$

$$
\text{MoIC}=\frac{\text{Total Equity Proceeds, including Distributions}}{\text{Total Equity Contributions}} \tag{138}
$$

$$
\text{Sponsor IRR} = (\text{MoIC})^{1/n} - 1 \tag{139}
$$

$$
\text{DSCR} = \frac{\text{CFADS}}{\text{Debt Service (Principal + Interest)}} \tag{140}
$$

### Contoh penerapan

EV1.000,target debt300,cash0 memberi harga ekuitas700. Uses=700+refinance300+fees20=1.020. Senior600+mezzanine100+sponsor320=1.020. EV+refinance+fee akan menghitung utang target dua kali.

## S30

**5.4 — Model Manajemen Saldo Kas Optimal (Bab 49)**

[Bab 49: Managing cash flows](./49-managing-cash-flows.md)

### Asumsi dan penjelasan

Baumol mengasumsikan penggunaan kas yang deterministik, sedangkan Miller–Orr model stokastik dengan batas bawah yang ditentukan. K dan varians harus memakai periode yang sama; varians harian tidak boleh dipasangkan rate tahunan. Formula ini pelengkap manajemen kas; jangan menyebut setiap persamaannya kutipan literal buku.

### Persamaan

**Model Baumol-Allais-Tobin (BAT):**

$$
C^* = \sqrt{\frac{2 \cdot T \cdot F}{K}} \tag{141}
$$

$$
\text{Total Cash Cost} = \left(\frac{T}{C}\right) F + \left(\frac{C}{2}\right) K \tag{142}
$$

di mana $T$ adalah total kebutuhan kas periode, $F$ adalah biaya transaksi tetap per transfer, dan $K$ adalah biaya peluang suku bunga.

**Model Miller-Orr (Ketidakpastian Stokastik):**

$$
Z^* = L + \sqrt[3]{\frac{3 \cdot F \cdot \sigma^2}{4 \cdot K}} \tag{143}
$$

$$
H^* = 3Z^* - 2L, \qquad \text{Average Cash Balance} = \frac{4Z^* - L}{3} \tag{144}
$$

di mana $L$ adalah batas bawah kas, dan $\sigma^2$ adalah varians arus kas harian.

### Contoh penerapan

Baumol T1.000.000,F100,K10%/tahun memberi C*=44.721,3595. Miller–Orr L1.000,F10,varians harian10.000,Kharian0,001 memberi return point1.421,7163 dan batas atas2.265,1490.

## S31

**5.5 — Manajemen Risiko Pasar & Derivatif (Bab 50)**

[Bab 50: Managing financial risks](./50-managing-financial-risks.md)

### Asumsi dan penjelasan

CIP memerlukan konvensi quote yang eksplisit dan tenor. PPP adalah relasi/model jangka panjang, bukan harga forward yang dapat dieksekusi. Formula swap sederhana memakai satu kurva dan floating leg par. VaR bukan maksimum kerugian. Delta hedge memerlukan arah posisi dan multiplier kontrak.

### Persamaan

**Covered Interest Rate Parity (CIP):**

$$
F_{0,T}=S_0\frac{1+r_{\text{domestic}}T}{1+r_{\text{foreign}}T}\quad\text{(simple rates; domestic per foreign unit)} \tag{145}
$$

$$
\text{Forward Premium/Discount} = \left(\frac{F - S}{S}\right) \times \left(\frac{360}{t}\right) \tag{146}
$$

**Purchasing Power Parity (PPP):**

$$
E[S_t]_{\text{relative PPP}}=S_0\left(\frac{1+\pi_{\text{domestic}}}{1+\pi_{\text{foreign}}}\right)^t \tag{147}
$$

**Interest Rate Swap (IRS) Rate:**

$$
R_{\text{swap}} = \frac{1 - P(0, T_n)}{\sum_{i=1}^{n} P(0, T_i) \times \tau_i} \tag{148}
$$

**Parametric Value at Risk (VaR):**

$$
\text{VaR}_{\alpha} = -(\mu - z_{\alpha} \cdot \sigma) \times \text{Portfolio Value} \tag{149}
$$

dengan $z_{95\%} = 1.645$ dan $z_{99\%} = 2.326$.

**Delta Hedging:**

$$
N_{\text{shares,hedge}}=-n_{\text{options,signed}}\times\text{Contract Multiplier}\times\Delta_{\text{option}} \tag{150}
$$

---

### Contoh penerapan

Quote IDR/USD: S16.000,rIDR6%,rUSD4%,T0,25 dengan simple rates memberi F=16.000×1,015/1,01=16.079,2079. Short10 call,delta0,6,multiplier100 memerlukan long600 saham untuk hedge delta.

## Cara menjalankan ulang

Jalankan scripts/build_formula_supplement.py setelah generator buku. Data asumsi dan perubahan tersedia pada data/formula-supplement-review.json. Originals dipertahankan byte demi byte; PDF dan LaTeX lampiran tetap versi awal, sehingga koreksi berlaku pada Markdown versi telaah ini.
