# Indeks rumus dan kerangka analisis

Lima puluh rumus/kerangka utama catatan pendamping ditulis ulang dalam LaTeX. Ini bukan inventaris setiap persamaan buku. Rumus lainnya berada dalam teks sumber; gunakan PDF bila simbol berubah. Periksa asumsi sebelum menggunakan formula.

## Bab 1: Peran keuangan perusahaan

$$
V_0 = \sum_{t=1}^{N}\frac{\mathbb{E}[CF_t]}{(1+k)^t}
$$

V₀ = nilai sekarang; CF = arus kas yang relevan bagi pemegang klaim; k = tingkat imbal hasil yang sesuai risiko klaim; t = periode.

[Penjelasan dan contoh](study/01-what-is-corporate-finance.md)

## Bab 2: Empat siklus dan arus kas

$$
\Delta Cash = CFO + CFI + CFF
$$

CFO = arus kas operasi; CFI = investasi; CFF = pendanaan. Semua menggunakan tanda positif untuk kas masuk dan negatif untuk kas keluar. Dampak kurs terhadap saldo kas dianalisis terpisah jika ada.

[Penjelasan dan contoh](study/02-cash-flow.md)

## Bab 3: Laba dan perubahan kekayaan

$$
EBIT = EBITDA - D\&A \qquad NI = EBIT - I - Tax
$$

D&A = depresiasi dan amortisasi; NI = laba bersih; I = beban bunga bersih. Bentuk sederhana mengabaikan pos nonoperasi lain.

[Penjelasan dan contoh](study/03-earnings.md)

## Bab 4: Modal yang digunakan dan sumber pendanaan

$$
CE = NFA + WC = E + D_{net} \qquad D_{net}=D_{gross}-Cash_{eligible}
$$

CE = capital employed; NFA = aset tetap operasi bersih; WC = modal kerja operasi dan penyesuaian relevan; E = ekuitas; D = utang keuangan. Kas yang dibatasi penggunaannya tidak otomatis menjadi pengurang utang.

[Penjelasan dan contoh](study/04-capital-employed-and-invested-capital.md)

## Bab 5: Jembatan laba menjadi arus kas

$$
FCFF = EBIT(1-T)+D\&A-Capex-\Delta WC
$$

FCFF = kas bebas untuk seluruh penyandang modal; T = tarif pajak ilustratif atas laba operasi; capex = investasi operasi bersih sesuai definisi model; ΔWC = WC akhir dikurangi WC awal. Ini bukan rumus universal klasifikasi CFO laporan keuangan.

[Penjelasan dan contoh](study/05-walking-through-from-earnings-to-cash-flow.md)

## Bab 6: Laporan keuangan konsolidasian

$$
NI_{parent}=NI_{group}-NI_{NCI}
$$

NI = laba bersih; NCI = kepentingan nonpengendali. Formula mengasumsikan angka konsolidasian sudah memuat eliminasi dan penyesuaian yang relevan.

[Penjelasan dan contoh](study/06-getting-to-grips-with-consolidated-accounts.md)

## Bab 7: Pos akuntansi yang memerlukan penyesuaian analitis

$$
Metric_{adjusted}=Metric_{reported}+\sum Adjustments
$$

Setiap adjustment harus memiliki akun sumber, alasan ekonomi, pengaruh laba, neraca, kas, pajak, dan penjelasan apakah berulang. Tanda penyesuaian mengikuti metrik yang dihitung.

[Penjelasan dan contoh](study/07-how-to-cope-with-the-most-complex-points-in-financial-accounts.md)

## Bab 8: Metode analisis keuangan yang runtut

$$
Growth = \frac{S_t}{S_{t-1}}-1 \qquad CAGR=\left(\frac{S_N}{S_0}\right)^{1/N}-1
$$

S = penjualan sebanding; N = jumlah interval tahun, bukan jumlah observasi. Perubahan mata uang dan perimeter perlu dijelaskan.

[Penjelasan dan contoh](study/08-how-to-perform-a-financial-analysis.md)

## Bab 9: Struktur margin dan sumber pertumbuhan

$$
EBIT\ Margin=\frac{EBIT}{Sales} \qquad 1+g_S=(1+g_Q)(1+g_P)
$$

gS = pertumbuhan pendapatan; gQ = pertumbuhan volume; gP = perubahan harga pada produk homogen. Rumus kedua mengabaikan perubahan bauran, kurs, dan perimeter.

[Penjelasan dan contoh](study/09-margin-analysis-structure.md)

## Bab 10: Titik impas dan risiko operasi

$$
Q_{BE}=\frac{FC}{P-v} \qquad S_{BE}=\frac{FC}{CM\%} \qquad DOL=\frac{S-VC}{EBIT}
$$

FC = biaya tetap operasi; P = harga per unit; v = biaya variabel per unit; CM% = (S−VC)/S; DOL = sensitivitas EBIT terhadap penjualan pada struktur biaya konstan.

[Penjelasan dan contoh](study/10-margin-analysis-risks.md)

## Bab 11: Investasi modal kerja dan aset tetap

$$
DSO=\frac{AR_{avg}}{Credit\ Sales}\times365 \quad DIO=\frac{Inv_{avg}}{COGS}\times365 \quad DPO=\frac{AP_{avg}}{Credit\ Purchases}\times365
$$

AR = piutang usaha; Inv = persediaan; AP = utang usaha. Gunakan penjualan dan pembelian dengan basis pajak yang konsisten dengan saldo. Buku juga menampilkan indikator persediaan terhadap penjualan; rasio berbasis HPP di sini diberi definisi tersendiri.

[Penjelasan dan contoh](study/11-working-capital-and-capital-expenditures.md)

## Bab 12: Kemampuan membiayai dan membayar utang

$$
Net\ Leverage=\frac{D_{net}}{EBITDA} \qquad DSCR=\frac{CFADS}{Interest+Principal\ Due}
$$

CFADS = arus kas tersedia untuk layanan utang sesuai definisi kontrak; DSCR harus dihitung menggunakan periode pembayaran yang sesuai. Definisi covenant dapat berbeda dari model analitis.

[Penjelasan dan contoh](study/12-financing.md)

## Bab 13: ROCE, ROE, dan efek leverage

$$
ROCE=\frac{NOPAT}{CE}=\frac{NOPAT}{Sales}\frac{Sales}{CE} \qquad ROE=ROCE+(ROCE-i)\frac{D}{E}
$$

NOPAT = EBIT setelah pajak operasi normal; i = biaya utang setelah pajak. Persamaan leverage memerlukan definisi modal dan laba yang selaras serta asumsi struktur sederhana.

[Penjelasan dan contoh](study/13-return-on-capital-employed-and-return-on-equity.md)

## Bab 14: Kesimpulan analisis keuangan

$$
Economic\ Profit = NOPAT - WACC\times CE
$$

CE adalah modal operasi pada basis yang dipilih secara konsisten; WACC merupakan tingkat imbal hasil penyandang modal sesuai risiko, bukan sekadar bunga bank.

[Penjelasan dan contoh](study/14-conclusion-of-financial-analysis.md)

## Bab 15: Pasar keuangan dan informasi

$$
R=\frac{P_1-P_0+Distribution}{P_0}
$$

P₀ = harga pembelian; P₁ = harga akhir; distribution = arus kas yang diterima investor selama horizon. Biaya transaksi dan pajak belum dimasukkan.

[Penjelasan dan contoh](study/15-the-financial-markets.md)

## Bab 16: Nilai waktu uang dan NPV

$$
FV=PV(1+k)^n \qquad NPV=-I_0+\sum_{t=1}^{N}\frac{FCF_t}{(1+k)^t}
$$

I₀ = investasi awal positif yang dikurangkan; k = tingkat diskonto per periode; N = jumlah periode. FCF diasumsikan diterima pada akhir setiap periode.

[Penjelasan dan contoh](study/16-the-time-value-of-money-and-net-present-value.md)

## Bab 17: IRR dan tingkat bunga efektif

$$
0=\sum_{t=0}^{N}\frac{CF_t}{(1+IRR)^t} \qquad EAR=\left(1+\frac{j}{m}\right)^m-1
$$

j = tingkat nominal tahunan; m = frekuensi compounding per tahun; EAR = tingkat efektif tahunan. IRR memerlukan cash flow dengan tanda yang konsisten.

[Penjelasan dan contoh](study/17-the-internal-rate-of-return.md)

## Bab 18: Risiko, portofolio, dan diversifikasi

$$
E[R_p]=\sum w_iE[R_i] \qquad \sigma_p^2=\sum_i\sum_jw_iw_jCov(R_i,R_j) \qquad \beta_i=\frac{Cov(R_i,R_M)}{Var(R_M)}
$$

w = bobot portofolio; σ = simpangan baku; Cov = kovarians; M = portofolio pasar. Bobot dan return harus memakai horizon yang sama.

[Penjelasan dan contoh](study/18-risk-and-return.md)

## Bab 19: Imbal hasil yang disyaratkan dan kurva bunga

$$
k_E=r_f+\beta_E(E[R_M]-r_f) \qquad (1+s_2)^2=(1+s_1)(1+f_{1,2})
$$

rf = tingkat bebas risiko yang konsisten mata uang; premi pasar = return pasar yang diharapkan dikurangi rf; s = spot rate; f = forward rate dengan compounding tahunan.

[Penjelasan dan contoh](study/19-the-required-rate-of-return.md)

## Bab 20: Obligasi, yield, duration, dan convexity

$$
P=\sum_{t=1}^{N}\frac{C}{(1+y)^t}+\frac{F}{(1+y)^N} \qquad D_{mod}=\frac{D_{Mac}}{1+y} \qquad \frac{\Delta P}{P}\approx-D_{mod}\Delta y
$$

C = kupon tahunan; F = pokok; y = yield per tahun; Macaulay duration = jumlah t×PV(CFt) dibagi P. Bentuk ini untuk pembayaran tahunan tanpa opsi.

[Penjelasan dan contoh](study/20-bonds.md)

## Bab 21: Produk utang dan pembiayaan berbasis aset

$$
Funding\ Gap=Peak\ Cash\ Need-Committed\ Internal\ Liquidity
$$

Kebutuhan puncak kas dihitung dari proyeksi bertanggal. Fasilitas belum committed atau fasilitas yang tidak dapat ditarik karena covenant tidak dihitung sebagai dana pasti tersedia.

[Penjelasan dan contoh](study/21-other-debt-products.md)

## Bab 22: Analisis saham dan multiple pasar

$$
EPS=\frac{NI_{ordinary}}{Weighted\ Average\ Shares} \quad P/E=\frac{Price}{EPS} \quad Dividend\ Yield=\frac{DPS}{Price}
$$

NIordinary = laba yang dapat diatribusikan kepada pemegang saham biasa; DPS = dividen per saham. Untuk diluted EPS, sesuaikan laba dan jumlah saham menurut sifat instrumen.

[Penjelasan dan contoh](study/22-shares.md)

## Bab 23: Opsi sebagai hak dan cara berpikir

$$
Call_T=\max(S_T-K,0) \quad Put_T=\max(K-S_T,0) \quad C-P=S_0-Ke^{-rT}
$$

S = harga aset; K = strike; T = tenor; r = bunga kontinu. Put-call parity ini berlaku untuk opsi Eropa tanpa dividen dengan tenor dan strike sama, dalam pasar tanpa arbitrase.

[Penjelasan dan contoh](study/23-options.md)

## Bab 24: Sekuritas hibrida dan biaya yang tersembunyi

$$
Conversion\ Value=qS \qquad Conversion\ Price=\frac{Face\ Value}{q}
$$

q = jumlah saham yang diperoleh untuk satu obligasi; S = harga saham. Pendekatan obligasi biasa ditambah opsi merupakan kerangka awal, bukan formula akurat untuk semua struktur yang mengandung interaksi kredit, dilusi, dan early exercise.

[Penjelasan dan contoh](study/24-hybrid-securities.md)

## Bab 25: Penempatan dan penerbitan sekuritas

$$
TERP=\frac{N_oP_o+N_nP_s}{N_o+N_n} \qquad Right\ Value=P_o-TERP
$$

No = saham lama; Nn = saham baru; Po = harga sebelum hak; Ps = harga subscription. Nilai hak dinyatakan per saham lama pada struktur satu hak untuk tiap saham lama dan tanpa biaya.

[Penjelasan dan contoh](study/25-selling-securities.md)

## Bab 26: Sumber penciptaan nilai

$$
Value\ Created=PV(Incremental\ Cash\ Flows)-Investment
$$

Arus kas harus benar-benar tambahan terhadap kondisi tanpa keputusan, termasuk biaya peluang, pajak, serta pengaruh terhadap produk atau aset lain.

[Penjelasan dan contoh](study/26-value-and-corporate-finance.md)

## Bab 27: Mengukur nilai dengan NPV, EVA, MVA, dan TSR

$$
EVA=NOPAT-WACC\times CE \quad MVA=EV-CE \quad TSR=\frac{P_1-P_0+D}{P_0}
$$

CE dan EV harus konsisten perimeter serta definisinya. TSR sederhana untuk satu horizon mengasumsikan dividen tanpa reinvestasi di tengah periode; untuk banyak periode gunakan return dengan tanggal dan reinvestasi yang jelas.

[Penjelasan dan contoh](study/27-measuring-value-creation.md)

## Bab 28: Memilih investasi berdasarkan arus kas tambahan

$$
FCFF=EBIT(1-T)+D\&A-Capex-\Delta WC \qquad PI=\frac{PV(Future\ Inflows)}{Initial\ Outlay}
$$

PI = profitability index untuk bentuk sederhana arus kas dengan investasi awal tunggal. Penjatahan modal dengan proyek tak terbagi membutuhkan pemilihan kombinasi, bukan hanya ranking PI.

[Penjelasan dan contoh](study/28-investment-criteria.md)

## Bab 29: Biaya modal dan kecocokan risiko

$$
WACC=\frac{E}{D+E}k_E+\frac{D}{D+E}k_D(1-T) \quad \beta_U=\frac{\beta_L}{1+(1-T)D/E}
$$

D dan E = nilai pasar utang dan ekuitas; kD = biaya utang sebelum pajak; formula beta adalah pendekatan dengan beta utang diabaikan dan asumsi tax shield tertentu. Pajak ilustratif harus sesuai kemampuan penggunaan tax shield.

[Penjelasan dan contoh](study/29-the-cost-of-capital.md)

## Bab 30: Risiko investasi dan opsi riil

$$
ENPV=NPV_{static}+Value_{flexibility}
$$

ENPV = expanded NPV; nilai fleksibilitas adalah peningkatan nilai terhadap strategi statis pada asumsi yang konsisten. Bukan setiap ketidakpastian otomatis menjadi opsi yang dapat dimonetisasi.

[Penjelasan dan contoh](study/30-risk-and-investment-analysis.md)

## Bab 31: DCF, multiples, dan rekonsiliasi nilai

$$
EV=\sum_{t=1}^{N}\frac{FCFF_t}{(1+WACC)^t}+\frac{TV_N}{(1+WACC)^N} \quad TV_N=\frac{FCFF_{N+1}}{WACC-g}
$$

g harus lebih kecil dari WACC; FCFF terminal perlu memuat investasi yang mendukung pertumbuhan. Bentuk dasar Equity = EV − net debt berlaku ketika tidak ada klaim atau aset penyesuaian lain.

[Penjelasan dan contoh](study/31-valuation-techniques.md)

## Bab 32: Struktur modal dalam pasar sempurna

$$
V_L=V_U \qquad k_E=k_U+(k_U-k_D)\frac{D}{E}
$$

VL = nilai perusahaan levered; VU = unlevered; kU = required return aset operasi. Formula ini untuk dunia tanpa pajak dengan asumsi dasar pasar sempurna.

[Penjelasan dan contoh](study/32-capital-structure-and-the-theory-of-perfect-capital-markets.md)

## Bab 33: Pajak, distress, sinyal, dan keagenan

$$
V_L=V_U+PV(Tax\ Shields)-PV(Distress\ Costs)-Other\ Net\ Costs
$$

Tax shield tahunan sederhana = T×interest yang deductible dan dapat digunakan. PV(Tax shield)=T×D hanya berlaku pada asumsi khusus utang permanen dan tingkat diskonto tax shield yang sesuai.

[Penjelasan dan contoh](study/33-capital-structure-taxes-and-organisation-theories.md)

## Bab 34: Ekuitas dan utang sebagai posisi opsi

$$
E_T=\max(V_T-F,0) \qquad D_T=\min(V_T,F)=F-\max(F-V_T,0)
$$

VT = nilai aset pada jatuh tempo; F = pembayaran utang yang dijanjikan. Model satu utang, satu jatuh tempo, dan tanpa biaya kebangkrutan menyederhanakan struktur nyata.

[Penjelasan dan contoh](study/34-debt-equity-and-options-theory.md)

## Bab 35: Merancang struktur modal yang tahan keadaan buruk

$$
Liquidity\ Headroom=Unrestricted\ Cash+Available\ Committed\ Lines-Stress\ Cash\ Needs
$$

Available berarti fasilitas dapat ditarik setelah memperhitungkan covenant, batas tujuan, jaminan, dan expiry. Kebutuhan stres dihitung pada horizon yang ditentukan.

[Penjelasan dan contoh](study/35-working-out-details-the-design-of-the-capital-structure.md)

## Bab 36: Mengembalikan kas kepada pemegang saham

$$
g\approx ROE\times(1-Payout)
$$

Payout = dividen/laba; rumus menggambarkan hubungan pertumbuhan ekuitas dengan laba ditahan pada konvensi modal dan ROE yang selaras. Asumsi termasuk kebijakan struktur modal dan profitabilitas yang stabil.

[Penjelasan dan contoh](study/36-returning-cash-to-shareholders.md)

## Bab 37: Dividen dan pembelian kembali saham

$$
P_{ex}\approx P_{cum}-DPS \qquad EPS_{new}=\frac{NI-AfterTax\ Financing\ Cost}{Shares-Shares\ Repurchased}
$$

Hubungan harga ex-dividend bersifat teoritis sebelum pajak, informasi baru, dan pergerakan pasar. Untuk buyback, perhatikan kapan transaksi terjadi jika menghitung EPS periode berjalan.

[Penjelasan dan contoh](study/37-distribution-in-practice-dividends-and-share-buybacks.md)

## Bab 38: Penerbitan saham dan jenis dilusi

$$
Ownership_{new}=\frac{Shares_{held}}{N_{old}+N_{new}} \qquad PostMoney=PreMoney+New\ Cash
$$

Post-money sederhana mengasumsikan transaksi pada nilai yang disepakati, tanpa fee, opsi tambahan, atau perbedaan kelas saham. EPS memerlukan bobot waktu dan hasil atas dana yang diterima.

[Penjelasan dan contoh](study/38-share-issues.md)

## Bab 39: Pelaksanaan kebijakan utang

$$
Interest_{floating}=Principal\times(Reference\ Rate+Spread)\times YearFraction
$$

Reference rate, spread, day-count, reset date, dan floor mengikuti kontrak. Biaya efektif juga mencakup arrangement fee, commitment fee, hedging, dan biaya jaminan.

[Penjelasan dan contoh](study/39-implementing-a-debt-policy.md)

## Bab 40: Pendanaan perusahaan rintisan

$$
Runway\approx\frac{Unrestricted\ Cash}{Monthly\ Net\ Burn} \quad Investor\ Stake=\frac{Investment}{PreMoney+Investment}
$$

Net burn = pengeluaran dikurangi penerimaan kas; runway sederhana mengasumsikan burn konstan. Rumus kepemilikan mengabaikan opsi, convertible, biaya, dan hak preferensi.

[Penjelasan dan contoh](study/40-setting-up-a-company-or-financing-startups.md)

## Bab 41: Struktur pemegang saham dan kontrol

$$
Indirect\ Economic\ Ownership=\prod_{j=1}^{m}Ownership_j
$$

Formula berlaku pada satu jalur kepemilikan tanpa kepemilikan silang. Bila ada beberapa jalur, agregasi harus memeriksa tumpang tindih. Hak kontrol tidak otomatis sama dengan hasil perkalian kepemilikan ekonomis.

[Penjelasan dan contoh](study/41-choice-of-corporate-structure.md)

## Bab 42: IPO dan kesiapan menjadi perusahaan terbuka

$$
Gross\ Primary\ Proceeds=N_{new}\times Offer\ Price \quad Underpricing=\frac{First\ Market\ Price}{Offer\ Price}-1
$$

Net proceeds = gross proceeds dikurangi biaya yang ditanggung perusahaan. Underpricing perlu horizon dan harga pembanding yang jelas.

[Penjelasan dan contoh](study/42-initial-public-offerings-ipos.md)

## Bab 43: Tata kelola dan pengurangan konflik

$$
Net\ Governance\ Benefit=Expected\ Agency\ Loss\ Avoided-Governance\ Cost
$$

Ini kerangka keputusan analitis, bukan formula empiris baku dari buku. Manfaat mencakup berkurangnya kebocoran nilai, kesalahan investasi, dan risiko pelaporan; estimasi harus dijelaskan.

[Penjelasan dan contoh](study/43-corporate-governance.md)

## Bab 44: Pengambilalihan dan harga maksimum akuisisi

$$
NPV_{buyer}=V_{target,standalone}+PV(Net\ Synergies)-Price\ Paid-Other\ Deal\ Costs
$$

Gunakan basis enterprise atau equity secara konsisten. Net synergy harus sudah mempertimbangkan pajak, biaya realisasi, timing, dan probabilitas; biaya jangan dikurangkan dua kali.

[Penjelasan dan contoh](study/44-taking-control-of-a-company.md)

## Bab 45: Merger, rasio pertukaran, dan pemisahan usaha

$$
New\ Shares=qN_B \quad Ownership_B=\frac{qN_B}{N_A+qN_B} \quad EPS_{combined}=\frac{NI_A+NI_B+Net\ Earnings\ Synergy}{N_A+qN_B}
$$

q = saham A per satu saham B; NA, NB = saham masing-masing sebelum transaksi. Formula EPS sederhana mengabaikan timing, purchase accounting, pajak khusus, dan biaya transaksi.

[Penjelasan dan contoh](study/45-mergers-and-demergers.md)

## Bab 46: Leveraged buyout dan sumber return ekuitas

$$
Exit\ Equity=Exit\ EV-Exit\ Net\ Debt \quad MOIC=\frac{Total\ Equity\ Proceeds}{Initial\ Equity} \quad IRR=MOIC^{1/N}-1
$$

Rumus IRR sederhana berlaku jika hanya ada investasi awal dan satu penerimaan akhir tanpa distribusi atau investasi tambahan. Untuk banyak cash flow gunakan IRR bertanggal.

[Penjelasan dan contoh](study/46-leveraged-buyouts-lbos.md)

## Bab 47: Kesulitan keuangan dan restrukturisasi

$$
Recovery\ Rate=\frac{Value\ Allocated\ to\ Creditor}{Claim\ Amount} \quad Cash_{end}=Cash_{start}+Receipts-Payments
$$

Pembagian nilai harus mengikuti struktur klaim yang berlaku dalam skenario; unsecured, secured, dan subordinated tidak diasumsikan menerima persentase sama.

[Penjelasan dan contoh](study/47-bankruptcy-and-restructuring.md)

## Bab 48: Mengelola modal kerja tanpa merusak margin

$$
CCC=DSO+DIO-DPO \qquad Cash\ Released\ from\ DSO\ Reduction\approx\frac{Annual\ Credit\ Sales}{365}\Delta DSO
$$

Gunakan basis pajak dan penjualan yang konsisten dengan piutang. Dampak steady-state berbeda dari perubahan kas aktual pada masa transisi.

[Penjelasan dan contoh](study/48-managing-working-capital.md)

## Bab 49: Perencanaan dan pengendalian kas

$$
Ending\ Available\ Cash=Opening\ Available\ Cash+Expected\ Collections-Planned\ Disbursements+Financing
$$

Perhitungan dibuat per tanggal atau minggu, memisahkan saldo restricted, fasilitas tersedia, dan pembayaran yang belum final. Selisih kurs dianalisis tersendiri bila relevan.

[Penjelasan dan contoh](study/49-managing-cash-flows.md)

## Bab 50: Mengidentifikasi, mengukur, dan melindungi risiko

$$
Net\ Exposure=Gross\ Exposure-Natural\ Offsets-Hedge\ Notional_{effective}
$$

Notional harus dinyatakan dalam unit risiko yang sama; efektivitas memerlukan kesesuaian tenor, underlying, sensitivitas, dan kemungkinan transaksi terjadi. VaR adalah kuantil kerugian pada horizon dan confidence tertentu, bukan batas kerugian maksimum.

[Penjelasan dan contoh](study/50-managing-financial-risks.md)
