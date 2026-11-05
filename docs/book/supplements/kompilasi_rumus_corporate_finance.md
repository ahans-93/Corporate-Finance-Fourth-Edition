# KOMPILASI RUMUS CORPORATE FINANCE

**Formulasi Matematis, Model Penilaian & Rekayasa Keuangan**

Berdasarkan E-Book: *Corporate Finance: Theory and Practice (4th Edition)*
Pierre Vernimmen, Pascal Quiry, Maurizio Dallocchio, Yann Le Fur, Antonio Salvi

> **Ringkasan Dokumen:** Kompilasi ini menyajikan seluruh rumus matematika keuangan, persamaan akuntansi manajerial, model penetapan harga aset modal, dan formula manajemen risiko dari ke-50 bab e-book *Corporate Finance: Theory and Practice* (Vernimmen et al.). Format matematis disajikan menggunakan sintaks baku LaTeX sesuai standar akademik dan notasi e-book aslinya.

---

## Daftar Isi

1. [Analisis Keuangan (Financial Analysis)](#1-analisis-keuangan-financial-analysis)
   - 1.1 Arus Kas & Free Cash Flow (Bab 2 & 5)
   - 1.2 Analisis Laba & Pembentukan Nilai Tambah (Bab 3)
   - 1.3 Modal Kerja & Neraca Capital Employed (Bab 4 & 11)
   - 1.4 Rasio Perputaran Modal Kerja & Siklus Kas (Bab 11)
   - 1.5 Margin, Risiko Operasi & Titik Impas (Bab 9 & 10)
   - 1.6 Solvabilitas, Likuiditas & Struktur Utang (Bab 12)
   - 1.7 Profitabilitas Modal & Formula Financial Leverage Vernimmen (Bab 13)
   - 1.8 Model Prediksi Kebangkrutan Altman Z-Score (Bab 14)
2. [Investor dan Pasar Keuangan (Investors and Markets)](#2-investor-dan-pasar-keuangan-investors-and-markets)
   - 2.1 Nilai Waktu Uang, Anuitas & Perpetuitas (Bab 16)
   - 2.2 Tingkat Pengembalian Internal & YTM (Bab 17)
   - 2.3 Teori Portofolio Markowitz & Pengukuran Risiko (Bab 18)
   - 2.4 Model Penentuan Harga Aset Modal (CAPM) (Bab 19)
   - 2.5 Penilaian Obligasi, Durasi & Konveksitas (Bab 20)
   - 2.6 Penilaian Saham Biasa & DDM (Bab 22)
   - 2.7 Teori Opsi & Model Black-Scholes-Merton (Bab 23)
   - 2.8 Sekuritas Hibrida & Obligasi Konversi (Bab 24)
3. [Penilaian dan Penciptaan Nilai (Value & Value Creation)](#3-penilaian-dan-penciptaan-nilai-value--value-creation)
   - 3.1 Enterprise Value & Nilai Ekuitas (Bab 26)
   - 3.2 Metrik Penciptaan Nilai: EVA, MVA & CFROI (Bab 27)
   - 3.3 Kriteria Keputusan Investasi (Bab 28)
   - 3.4 Biaya Modal Rata-Rata Tertimbang (WACC) (Bab 29)
   - 3.5 Teknik Valuasi Lengkap: DCF & Kelipatan Pasar (Bab 31)
4. [Kebijakan Keuangan Korporat (Corporate Financial Policies)](#4-kebijakan-keuangan-korporat-corporate-financial-policies)
   - 4.1 Struktur Modal Modigliani-Miller (Bab 32 & 33)
   - 4.2 Formula Hamada & Harris-Pringle (Bab 33)
   - 4.3 Model Opsi Struktural Merton (Bab 34)
   - 4.4 Dividen & Pembelian Saham Kembali (Bab 36 & 37)
   - 4.5 Penerbitan Hak Memesan Efek (Rights Issue) (Bab 38)
5. [Manajemen Keuangan & Rekayasa Finansial (Financial Management)](#5-manajemen-keuangan--rekayasa-finansial-financial-management)
   - 5.1 Valuasi Modal Ventura & Dilusi Pendiri (Bab 40)
   - 5.2 Merger, Akuisisi & Penilaian Sinergi (Bab 44 & 45)
   - 5.3 Leveraged Buyout (LBO) (Bab 46)
   - 5.4 Model Manajemen Saldo Kas Optimal (Bab 49)
   - 5.5 Manajemen Risiko Pasar & Derivatif (Bab 50)

---

# 1 Analisis Keuangan (Financial Analysis)

## 1.1 Arus Kas & Free Cash Flow (Bab 2 & 5)

$$\Delta \text{Cash} = \text{CFO} + \text{CFI} + \text{CFF} \tag{1}$$

di mana CFO adalah arus kas aktivitas operasi, CFI adalah arus kas investasi, dan CFF adalah arus kas pendanaan.

**Arus Kas Operasi (CFO – Metode Tidak Langsung):**

$$\text{CFO} = \text{EBITDA} - \text{Taxes}_{\text{operating}} - \Delta \text{WCR} \tag{2}$$

atau secara alternatif dari laba bersih:

$$\text{CFO} = \text{Net Income} + \text{Depreciation} + \text{Amortisation} + \text{Net Non-Cash Provisions} - \Delta \text{WCR} \tag{3}$$

**Kapasitas Autofinansial (Cash Flow / CAF):**

$$\text{CAF} = \text{Net Income} + \text{Depreciation} + \text{Amortisation} - \text{Net Capital Gains on Disposals} \tag{4}$$

**Free Cash Flow to Firm (FCFF):**

$$\text{FCFF} = \text{EBIT} \times (1 - T_c) + \text{Depreciation} - \text{Capex} - \Delta \text{WCR} \tag{5}$$

di mana $T_c$ adalah tarif pajak korporasi marjinal, dan Capex adalah belanja modal kotor.

**Free Cash Flow to Equity (FCFE):**

$$\text{FCFE} = \text{Net Income} + \text{Depreciation} - \text{Capex} - \Delta \text{WCR} + \text{New Debt Issued} - \text{Debt Repaid} \tag{6}$$

## 1.2 Analisis Laba & Pembentukan Nilai Tambah (Bab 3)

**Format Laba Rugi By-Nature (Vernimmen Standar):**

$$\text{Value Added (VA)} = \text{Sales} - \text{External Purchases and Services} \tag{7}$$

$$\text{EBITDA} = \text{VA} - \text{Personnel Costs} + \text{Operating Subsidies} \tag{8}$$

$$\text{EBIT} = \text{EBITDA} - \text{Depreciation and Amortisation} - \text{Operating Provisions} \tag{9}$$

$$\text{NOPAT} = \text{EBIT} \times (1 - T_c) \tag{10}$$

$$\text{EBT} = \text{EBIT} - \text{Net Financial Expense} + \text{Non-Operating Items} \tag{11}$$

$$\text{Net Income} = \text{EBT} - \text{Corporate Income Tax} \tag{12}$$

## 1.3 Modal Kerja & Neraca Capital Employed (Bab 4 & 11)

$$\text{WCR} = \text{Inventories} + \text{Trade Receivables} - \text{Trade Payables} - \text{Other Operating Working Liabilities} \tag{13}$$

**Identitas Fundamental Neraca Fungsional:**

$$\text{Capital Employed (CE)} = \text{Fixed Assets}_{\text{net}} + \text{WCR} \tag{14}$$

$$\text{Invested Capital} = \text{Shareholders' Equity} + \text{Net Financial Debt} \tag{15}$$

$$\text{Capital Employed} \equiv \text{Invested Capital} \tag{16}$$

**Utang Finansial Bersih (Net Debt):**

$$\text{Net Debt} = \text{Long-Term Debt} + \text{Short-Term Bank Debt} - (\text{Cash} + \text{Cash Equivalents} + \text{Marketable Securities}) \tag{17}$$

## 1.4 Rasio Perputaran Modal Kerja & Siklus Kas (Bab 11)

$$\text{DSO} = \frac{\text{Trade Receivables}}{\text{Sales (including VAT)}} \times 365 \tag{18}$$

$$\text{DIO} = \frac{\text{Inventories}}{\text{Cost of Goods Sold (COGS)}} \times 365 \tag{19}$$

$$\text{DPO} = \frac{\text{Trade Payables}}{\text{Purchases (including VAT)}} \times 365 \tag{20}$$

$$\text{CCC} = \text{DIO} + \text{DSO} - \text{DPO} \tag{21}$$

$$\text{Capex Intensity} = \frac{\text{Capex}}{\text{Annual Depreciation}} \tag{22}$$

## 1.5 Margin, Risiko Operasi & Titik Impas (Bab 9 & 10)

$$\text{Gross Margin} = \frac{\text{Sales} - \text{COGS}}{\text{Sales}}, \qquad \text{Operating Margin} = \frac{\text{EBIT}}{\text{Sales}} \tag{23}$$

$$\text{Contribution Margin (CM)} = \text{Sales} - \text{Variable Costs} \tag{24}$$

$$\text{CMR} = \frac{\text{Sales} - \text{Variable Costs}}{\text{Sales}} = \frac{\text{CM}}{\text{Sales}} \tag{25}$$

$$\text{BEP}_{\$} = \frac{\text{Fixed Costs}}{\text{CMR}} \tag{26}$$

$$\text{BEP}_{Q} = \frac{\text{Fixed Costs}}{P - \text{VC}_{\text{unit}}} \tag{27}$$

$$\text{Margin of Safety} = \frac{\text{Actual Sales} - \text{BEP Sales}}{\text{Actual Sales}} \tag{28}$$

$$\text{DOL} = \frac{\%\Delta \text{EBIT}}{\%\Delta \text{Sales}} = \frac{\text{Sales} - \text{VC}}{\text{EBIT}} = \frac{\text{CM}}{\text{EBIT}} \tag{29}$$

## 1.6 Solvabilitas, Likuiditas & Struktur Utang (Bab 12)

$$\text{Gearing} = \frac{\text{Net Debt}}{\text{Equity}} \tag{30}$$

$$\text{Leverage Ratio} = \frac{\text{Net Debt}}{\text{EBITDA}} \tag{31}$$

$$\text{Interest Coverage Ratio (ICR)} = \frac{\text{EBIT}}{\text{Net Financial Interest Expense}} \tag{32}$$

$$\text{Debt Service Coverage Ratio (DSCR)} = \frac{\text{CFADS}}{\text{Principal Repayment} + \text{Interest Expense}} \tag{33}$$

$$\text{Debt Payback} = \frac{\text{Net Debt}}{\text{CFO}} \tag{34}$$

$$\text{Current Ratio} = \frac{\text{Current Assets}}{\text{Current Liabilities}} \tag{35}$$

$$\text{Quick Ratio} = \frac{\text{Cash} + \text{Marketable Securities} + \text{Receivables}}{\text{Current Liabilities}} \tag{36}$$

## 1.7 Profitabilitas Modal & Formula Financial Leverage Vernimmen (Bab 13)

**Return on Capital Employed (ROCE):**

$$\text{ROCE} = \frac{\text{EBIT} \times (1 - T_c)}{\text{Capital Employed}} \tag{37}$$

**Dekomposisi DuPont ROCE:**

$$\text{ROCE} = \underbrace{\left(\frac{\text{EBIT}(1 - T_c)}{\text{Sales}}\right)}_{\text{Operating Margin}} \times \underbrace{\left(\frac{\text{Sales}}{\text{Capital Employed}}\right)}_{\text{Capital Turnover}} \tag{38}$$

**Return on Equity (ROE):**

$$\text{ROE} = \frac{\text{Net Income}}{\text{Shareholders' Equity}} \tag{39}$$

**Formula Financial Leverage Vernimmen:**

$$\text{ROE} = \text{ROCE} + (\text{ROCE} - i) \times \left(\frac{\text{Net Debt}}{\text{Equity}}\right) \tag{40}$$

di mana $i$ adalah biaya utang bersih setelah pajak:

$$i = \frac{\text{Net Financial Expense} \times (1 - T_c)}{\text{Net Debt}} \tag{41}$$

> **Aturan Pengungkit Vernimmen:** Jika $\text{ROCE} > i$, penambahan utang mendongkrak ROE (efek pengungkit positif). Jika $\text{ROCE} < i$, utang memperberat beban keuangan dan menekan ROE di bawah ROCE (efek pengungkit negatif).

**Dekomposisi DuPont 3-Faktor Tradisional:**

$$\text{ROE} = \underbrace{\left(\frac{\text{Net Income}}{\text{Sales}}\right)}_{\text{Net Profit Margin}} \times \underbrace{\left(\frac{\text{Sales}}{\text{Assets}}\right)}_{\text{Asset Turnover}} \times \underbrace{\left(\frac{\text{Assets}}{\text{Equity}}\right)}_{\text{Equity Multiplier}} \tag{42}$$

## 1.8 Model Prediksi Kebangkrutan Altman Z-Score (Bab 14)

$$Z = 1.2X_1 + 1.4X_2 + 3.3X_3 + 0.6X_4 + 0.999X_5 \tag{43}$$

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

# 2 Investor dan Pasar Keuangan (Investors and Markets)

## 2.1 Nilai Waktu Uang, Anuitas & Perpetuitas (Bab 16)

$$\text{Future Value (FV)} = \text{PV} \times (1 + r)^n \tag{44}$$

$$\text{Present Value (PV)} = \frac{\text{FV}_n}{(1 + r)^n} = \text{FV}_n \times (1 + r)^{-n} \tag{45}$$

$$\text{Continuous Compounding}: \quad \text{FV} = \text{PV} \cdot e^{rt}, \qquad \text{PV} = \text{FV} \cdot e^{-rt} \tag{46}$$

$$\text{Effective Annual Rate (EAR)} = \left(1 + \frac{r_{\text{nom}}}{m}\right)^m - 1 \tag{47}$$

**Anuitas Biasa (Ordinary Annuity):**

$$\text{PV}_{\text{annuity}} = C \times \left[\frac{1 - (1 + r)^{-n}}{r}\right] \tag{48}$$

$$\text{FV}_{\text{annuity}} = C \times \left[\frac{(1 + r)^n - 1}{r}\right] \tag{49}$$

**Perpetuitas (Perpetuity):**

$$\text{PV}_{\text{perpetuity}} = \frac{C}{r} \tag{50}$$

**Perpetuitas Bertumbuh (Gordon-Shapiro Perpetuity):**

$$\text{PV}_{\text{growing perpetuity}} = \frac{C_1}{r - g} \qquad (r > g) \tag{51}$$

**Anuitas Bertumbuh (Growing Annuity):**

$$\text{PV} = \frac{C_1}{r - g}\left[1 - \left(\frac{1 + g}{1 + r}\right)^n\right] \tag{52}$$

## 2.2 Tingkat Pengembalian Internal & YTM (Bab 17)

**Internal Rate of Return (IRR):**

$$\sum_{t=0}^{n} \frac{\text{CF}_t}{(1 + \text{IRR})^t} = 0 \iff I_0 = \sum_{t=1}^{n} \frac{\text{CF}_t}{(1 + \text{IRR})^t} \tag{53}$$

**Modified Internal Rate of Return (MIRR):**

$$\text{MIRR} = \left[\frac{\text{FV(Positive Cash Flows at Reinvestment Rate)}}{\text{PV(Negative Cash Flows at Financing Rate)}}\right]^{1/n} - 1 \tag{54}$$

**Yield to Maturity Obligasi (YTM):**

$$P = \sum_{t=1}^{n} \frac{C}{(1 + \text{YTM})^t} + \frac{M}{(1 + \text{YTM})^n} \tag{55}$$

## 2.3 Teori Portofolio Markowitz & Pengukuran Risiko (Bab 18)

$$E(R_p) = \sum_{i=1}^{N} w_i E(R_i) \qquad \text{dengan} \qquad \sum_{i=1}^{N} w_i = 1 \tag{56}$$

$$\sigma_i^2 = \sum_k p_k \left[R_{i,k} - E(R_i)\right]^2, \qquad \sigma_i = \sqrt{\sigma_i^2} \tag{57}$$

$$\text{Cov}(A, B) = \sigma_{AB} = \rho_{AB}\,\sigma_A\,\sigma_B \tag{58}$$

$$\rho_{AB} = \frac{\text{Cov}(A, B)}{\sigma_A \sigma_B}, \qquad -1 \le \rho_{AB} \le +1 \tag{59}$$

**Varians Portofolio 2-Aset:**

$$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \rho_{AB} \sigma_A \sigma_B \tag{60}$$

**Varians Portofolio N-Aset:**

$$\sigma_p^2 = \sum_{i=1}^{N} w_i^2 \sigma_i^2 + \sum_{i=1}^{N} \sum_{j \ne i} w_i w_j \sigma_{ij} \tag{61}$$

## 2.4 Model Penentuan Harga Aset Modal (CAPM) (Bab 19)

**Koefisien Beta ($\beta$):**

$$\beta_i = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)} = \frac{\rho_{im}\,\sigma_i}{\sigma_m} \tag{62}$$

**Persamaan Capital Asset Pricing Model (CAPM):**

$$E(R_i) = R_f + \beta_i \left[E(R_m) - R_f\right] \tag{63}$$

**Capital Market Line (CML):**

$$E(R_p) = R_f + \left[\frac{E(R_m) - R_f}{\sigma_m}\right] \sigma_p \tag{64}$$

**Ukuran Kinerja Portofolio:**

$$\text{Sharpe Ratio} = \frac{E(R_p) - R_f}{\sigma_p} \tag{65}$$

$$\text{Treynor Ratio} = \frac{E(R_p) - R_f}{\beta_p} \tag{66}$$

$$\text{Jensen's Alpha}\ (\alpha_p) = R_p - \left[R_f + \beta_p (R_m - R_f)\right] \tag{67}$$

## 2.5 Penilaian Obligasi, Durasi & Konveksitas (Bab 20)

$$\text{Dirty Price} = \text{Clean Price} + \text{Accrued Interest} \tag{68}$$

$$\text{Accrued Interest} = C \times \left(\frac{\text{Days since last coupon}}{\text{Days in coupon period}}\right) \tag{69}$$

**Macaulay Duration ($D$):**

$$D = \frac{1}{P}\left[\sum_{t=1}^{n} \frac{t \cdot C}{(1 + y)^t} + \frac{n \cdot M}{(1 + y)^n}\right] \tag{70}$$

**Modified Duration (MD):**

$$\text{MD} = \frac{D}{1 + y} = -\frac{1}{P}\frac{dP}{dy} \tag{71}$$

**Konveksitas (Convexity):**

$$\text{Convexity} = \frac{1}{P(1 + y)^2} \sum_{t=1}^{n} \frac{t(t + 1) \cdot \text{CF}_t}{(1 + y)^t} \tag{72}$$

**Aproksimasi Perubahan Harga Orde Kedua:**

$$\frac{\Delta P}{P} \approx -\text{MD} \times \Delta y + \frac{1}{2} \times \text{Convexity} \times (\Delta y)^2 \tag{73}$$

## 2.6 Penilaian Saham Biasa & DDM (Bab 22)

$$\text{Dividend Yield} = \frac{\text{DPS}_1}{P_0}, \qquad \text{Payout Ratio}\ (d) = \frac{\text{DPS}}{\text{EPS}}, \qquad b = 1 - d \tag{74}$$

$$g = b \times \text{ROE} = (1 - d) \times \text{ROE} \tag{75}$$

**Model Gordon-Shapiro:**

$$P_0 = \frac{\text{Div}_1}{k_E - g} \implies k_E = \frac{\text{Div}_1}{P_0} + g \tag{76}$$

**Model Pertumbuhan Dua Tahap (Two-Stage DDM):**

$$P_0 = \sum_{t=1}^{H} \frac{\text{Div}_t}{(1 + k_E)^t} + \frac{\text{Div}_{H+1}}{(k_E - g_2)(1 + k_E)^H} \tag{77}$$

## 2.7 Teori Opsi & Model Black-Scholes-Merton (Bab 23)

$$\text{Call Payoff} = \max(0,\, S_T - K) \tag{78}$$

$$\text{Put Payoff} = \max(0,\, K - S_T) \tag{79}$$

**Paritas Put-Call (Put-Call Parity):**

$$C - P = S_0 - K e^{-rT} \tag{80}$$

**Model Binomial Cox-Ross-Rubinstein (CRR):**

$$u = e^{\sigma\sqrt{\Delta t}}, \qquad d = \frac{1}{u} = e^{-\sigma\sqrt{\Delta t}}, \qquad p = \frac{e^{r\Delta t} - d}{u - d} \tag{81}$$

$$C = e^{-r\Delta t}\left[p\, C_u + (1 - p)\, C_d\right] \tag{82}$$

**Formula Black-Scholes-Merton (BSM):**

$$C = S_0 N(d_1) - K e^{-rT} N(d_2) \tag{83}$$

$$P = K e^{-rT} N(-d_2) - S_0 N(-d_1) \tag{84}$$

dengan parameter penentu:

$$d_1 = \frac{\ln(S_0 / K) + \left(r + \dfrac{\sigma^2}{2}\right) T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T} \tag{85}$$

**Turunan Greeks Opsi:**

$$\Delta_{\text{call}} = N(d_1), \qquad \Delta_{\text{put}} = N(d_1) - 1 \tag{86}$$

$$\Gamma = \frac{N'(d_1)}{S_0 \sigma \sqrt{T}} \tag{87}$$

$$\nu = S_0 \sqrt{T}\, N'(d_1) \tag{88}$$

$$\Theta_{\text{call}} = -\frac{S_0 N'(d_1)\,\sigma}{2\sqrt{T}} - r K e^{-rT} N(d_2) \tag{89}$$

$$\rho_{\text{call}} = K T e^{-rT} N(d_2) \tag{90}$$

## 2.8 Sekuritas Hibrida & Obligasi Konversi (Bab 24)

$$\text{Conversion Ratio (CR)} = \frac{\text{Nominal Value of Convertible Bond}}{\text{Conversion Price (CP)}} \tag{91}$$

$$\text{Conversion Value} = \text{CR} \times S_0 \tag{92}$$

$$\text{Conversion Premium} = \frac{P_{\text{CB}} - \text{Conversion Value}}{\text{Conversion Value}} \times 100\% \tag{93}$$

$$\text{Bond Floor} = \sum_{t=1}^{n} \frac{C}{(1 + y_{\text{straight}})^t} + \frac{M}{(1 + y_{\text{straight}})^n} \tag{94}$$

---

# 3 Penilaian dan Penciptaan Nilai (Value & Value Creation)

## 3.1 Enterprise Value & Nilai Ekuitas (Bab 26)

$$\text{EV} = \text{Market Cap} + \text{Net Debt} + \text{Minority Interests} - \text{Non-Operating Assets} \tag{95}$$

$$\text{Equity Value} = \text{EV} - \text{Net Debt} - \text{Minority Interests} + \text{Non-Operating Assets} \tag{96}$$

## 3.2 Metrik Penciptaan Nilai: EVA, MVA & CFROI (Bab 27)

**Economic Value Added (EVA):**

$$\text{EVA} = \text{NOPAT} - (\text{WACC} \times \text{Capital Employed}) = (\text{ROCE} - \text{WACC}) \times \text{Capital Employed} \tag{97}$$

**Market Value Added (MVA):**

$$\text{MVA} = \text{Market Value of Capital} - \text{Invested Capital} = \sum_{t=1}^{\infty} \frac{\text{EVA}_t}{(1 + \text{WACC})^t} \tag{98}$$

**Cash Flow Return on Investment (CFROI):**

$$\text{CFROI} = \frac{\text{Gross Cash Flow}}{\text{Gross Invested Capital}} \tag{99}$$

**Economic Profit Ekuitas:**

$$\text{Economic Profit} = \text{Net Income} - (k_E \times \text{Book Equity}) = (\text{ROE} - k_E) \times \text{Equity} \tag{100}$$

## 3.3 Kriteria Keputusan Investasi (Bab 28)

$$\text{NPV} = -I_0 + \sum_{t=1}^{n} \frac{\text{CF}_t}{(1 + k)^t} \tag{101}$$

$$\text{Profitability Index (PI)} = \frac{\sum_{t=1}^{n} \frac{\text{CF}_t}{(1 + k)^t}}{I_0} = 1 + \frac{\text{NPV}}{I_0} \tag{102}$$

$$\text{Equivalent Annual Annuity (EAA)} = \frac{\text{NPV}}{\left[\dfrac{1 - (1 + k)^{-n}}{k}\right]} \tag{103}$$

## 3.4 Biaya Modal Rata-Rata Tertimbang (WACC) (Bab 29)

$$\text{WACC} = k_E\left(\frac{E}{D + E}\right) + k_D (1 - T_c)\left(\frac{D}{D + E}\right) \tag{104}$$

dengan saham preferen:

$$\text{WACC} = k_E\left(\frac{E}{V}\right) + k_p\left(\frac{P}{V}\right) + k_D (1 - T_c)\left(\frac{D}{V}\right) \tag{105}$$

di mana $k_E = R_f + \beta_E\left[E(R_m) - R_f\right]$, dan $k_p = \dfrac{\text{Div}_p}{P_{\text{pref}}}$.

## 3.5 Teknik Valuasi Lengkap: DCF & Kelipatan Pasar (Bab 31)

**Enterprise DCF (Model FCFF):**

$$\text{EV} = \sum_{t=1}^{N} \frac{\text{FCFF}_t}{(1 + \text{WACC})^t} + \frac{\text{TV}_N}{(1 + \text{WACC})^N} \tag{106}$$

$$\text{Terminal Value}\ (\text{TV}_N) = \frac{\text{FCFF}_{N+1}}{\text{WACC} - g} \tag{107}$$

$$\text{Equity Value} = \text{EV} - \text{Net Debt} \tag{108}$$

**Equity DCF (Model FCFE):**

$$\text{Equity Value} = \sum_{t=1}^{N} \frac{\text{FCFE}_t}{(1 + k_E)^t} + \frac{\text{TV}_{E,N}}{(1 + k_E)^N}, \qquad \text{TV}_{E,N} = \frac{\text{FCFE}_{N+1}}{k_E - g} \tag{109}$$

**Adjusted Present Value (APV):**

$$\text{APV} = \text{EV}_{\text{unlevered}} + \text{PV(Tax Shield)} - \text{PV(Bankruptcy Costs)} \tag{110}$$

**Kelipatan Valuasi (Valuation Multiples):**

$$\text{P/E} = \frac{P_0}{\text{EPS}_1} = \frac{\text{Market Cap}}{\text{Net Income}} \tag{111}$$

$$\text{PEG Ratio} = \frac{\text{P/E}}{\text{Annual EPS Growth Rate} \times 100} \tag{112}$$

$$\text{EV/EBITDA} = \frac{\text{Enterprise Value}}{\text{EBITDA}}, \qquad \text{EV/Sales} = \frac{\text{Enterprise Value}}{\text{Sales}} \tag{113}$$

$$\text{EV/CE} = \frac{\text{Enterprise Value}}{\text{Capital Employed}} \tag{114}$$

---

# 4 Kebijakan Keuangan Korporat (Corporate Financial Policies)

## 4.1 Struktur Modal Modigliani-Miller (Bab 32 & 33)

**Dunia Tanpa Pajak (MM 1958):**

$$\text{Proposisi I}: \quad V_L = V_U \tag{115}$$

$$\text{Proposisi II}: \quad k_E = k_0 + (k_0 - k_D)\left(\frac{D}{E}\right) \tag{116}$$

$$\text{Asset Beta}: \quad \beta_A = \beta_E\left(\frac{E}{D + E}\right) + \beta_D\left(\frac{D}{D + E}\right) \tag{117}$$

**Dunia Dengan Pajak Korporasi (MM 1963):**

$$\text{Proposisi I}: \quad V_L = V_U + T_c \cdot D \tag{118}$$

$$\text{Proposisi II}: \quad k_E = k_0 + (k_0 - k_D)(1 - T_c)\left(\frac{D}{E}\right) \tag{119}$$

## 4.2 Formula Hamada & Harris-Pringle (Bab 33)

**Formula Hamada (Relevering Beta, $\beta_D = 0$):**

$$\beta_E = \beta_U\left[1 + (1 - T_c)\left(\frac{D}{E}\right)\right] \tag{120}$$

$$\beta_U = \frac{\beta_E}{1 + (1 - T_c)\left(\dfrac{D}{E}\right)} \tag{121}$$

**Formula Harris-Pringle (Target Debt Ratio Stabil):**

$$\beta_E = \beta_U + (\beta_U - \beta_D)\left(\frac{D}{E}\right) \tag{122}$$

## 4.3 Model Opsi Struktural Merton (Bab 34)

$$\text{Equity Value} = \text{Call}(V, K, T, \sigma_V, r) = V N(d_1) - K e^{-rT} N(d_2) \tag{123}$$

$$\text{Debt Value} = V - \text{Equity} = K e^{-rT} - \text{Put}(V, K, T, \sigma_V, r) \tag{124}$$

## 4.4 Dividen & Pembelian Saham Kembali (Bab 36 & 37)

$$N_{\text{new}} = N_{\text{old}} - \frac{\text{Buyback Funds}}{\text{Prepurchase Price}} \tag{125}$$

$$\text{EPS}_{\text{new}} = \frac{\text{Net Income} - \text{Foregone Cash Interest} \times (1 - T_c)}{N_{\text{new}}} \tag{126}$$

> **Ambang Batas Akresi Buyback:** Pembelian kembali saham meningkatkan EPS jika dan hanya jika
> $$\text{P/E} < \frac{1}{r_{\text{cash}}(1 - T_c)}$$

## 4.5 Penerbitan Hak Memesan Efek (Rights Issue) (Bab 38)

$$\text{TERP} = \frac{N \times P_0 + M \times S}{N + M} \tag{127}$$

$$R = P_0 - \text{TERP} = \frac{M \times (P_0 - S)}{N + M} = \frac{P_0 - S}{\dfrac{N}{M} + 1} \tag{128}$$

$$\text{Issue Discount} = \frac{P_0 - S}{P_0} \times 100\% \tag{129}$$

---

# 5 Manajemen Keuangan & Rekayasa Finansial (Financial Management)

## 5.1 Valuasi Modal Ventura & Dilusi Pendiri (Bab 40)

$$\text{Post-Money Valuation} = \text{Pre-Money Valuation} + \text{New Investment} \tag{130}$$

$$\text{Investor Ownership \%} = \frac{\text{New Investment}}{\text{Post-Money Valuation}} \tag{131}$$

$$\text{Founder Ownership \%}_{\text{new}} = \text{Founder Ownership \%}_{\text{old}} \times (1 - \text{Investor Ownership \%}) \tag{132}$$

## 5.2 Merger, Akuisisi & Penilaian Sinergi (Bab 44 & 45)

$$\text{Control Premium} = \frac{P_{\text{offer}} - P_{\text{unaffected}}}{P_{\text{unaffected}}} \times 100\% \tag{133}$$

$$\text{Exchange Ratio (ER)} = \frac{P_{\text{offer per target share}}}{P_{\text{acquirer share}}} \tag{134}$$

$$N_{\text{combined}} = N_{\text{acquirer}} + (N_{\text{target}} \times \text{ER}) \tag{135}$$

$$\text{Net Synergy} = \text{PV(Operating Synergies)} + \text{PV(Financial Synergies)} - \text{Integration Costs} \tag{136}$$

## 5.3 Leveraged Buyout (LBO) (Bab 46)

$$\text{Total Uses (EV + Refinancing + Fees)} \equiv \text{Total Sources (Senior Debt + Mezzanine + Sponsor Equity)} \tag{137}$$

$$\text{MoIC} = \frac{\text{Exit Equity Value}}{\text{Entry Sponsor Equity}} \tag{138}$$

$$\text{Sponsor IRR} = (\text{MoIC})^{1/n} - 1 \tag{139}$$

$$\text{DSCR} = \frac{\text{CFADS}}{\text{Debt Service (Principal + Interest)}} \tag{140}$$

## 5.4 Model Manajemen Saldo Kas Optimal (Bab 49)

**Model Baumol-Allais-Tobin (BAT):**

$$C^* = \sqrt{\frac{2 \cdot T \cdot F}{K}} \tag{141}$$

$$\text{Total Cash Cost} = \left(\frac{T}{C}\right) F + \left(\frac{C}{2}\right) K \tag{142}$$

di mana $T$ adalah total kebutuhan kas periode, $F$ adalah biaya transaksi tetap per transfer, dan $K$ adalah biaya peluang suku bunga.

**Model Miller-Orr (Ketidakpastian Stokastik):**

$$Z^* = L + \sqrt[3]{\frac{3 \cdot F \cdot \sigma^2}{4 \cdot K}} \tag{143}$$

$$H^* = 3Z^* - 2L, \qquad \text{Average Cash Balance} = \frac{4Z^* - L}{3} \tag{144}$$

di mana $L$ adalah batas bawah kas, dan $\sigma^2$ adalah varians arus kas harian.

## 5.5 Manajemen Risiko Pasar & Derivatif (Bab 50)

**Covered Interest Rate Parity (CIP):**

$$F = S \times \left(\frac{1 + r_{\text{domestic}}}{1 + r_{\text{foreign}}}\right) \tag{145}$$

$$\text{Forward Premium/Discount} = \left(\frac{F - S}{S}\right) \times \left(\frac{360}{t}\right) \tag{146}$$

**Purchasing Power Parity (PPP):**

$$S_t = S_0 \times \left(\frac{1 + i_{\text{domestic}}}{1 + i_{\text{foreign}}}\right)^t \tag{147}$$

**Interest Rate Swap (IRS) Rate:**

$$R_{\text{swap}} = \frac{1 - P(0, T_n)}{\sum_{i=1}^{n} P(0, T_i) \times \tau_i} \tag{148}$$

**Parametric Value at Risk (VaR):**

$$\text{VaR}_{\alpha} = -(\mu - z_{\alpha} \cdot \sigma) \times \text{Portfolio Value} \tag{149}$$

dengan $z_{95\%} = 1.645$ dan $z_{99\%} = 2.326$.

**Delta Hedging:**

$$N_{\text{shares}} = N_{\text{options}} \times \Delta_{\text{call}} = N_{\text{options}} \times N(d_1) \tag{150}$$

---

*Dokumen Kompilasi Formula Vernimmen Corporate Finance • Notasi Matematis Versi E-Book*
