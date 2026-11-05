# Rumus lanjutan dan asumsi pemakaian

Dokumen ini melengkapi [indeks per bab](formulas.md). Semua tingkat bunga dinyatakan sebagai desimal dalam perhitungan. Periode bunga, arus kas, dan waktu harus konsisten. Formula adalah alat analisis dengan asumsi, bukan pengganti pemahaman transaksi.

## 1. Anuitas dan perpetuitas — bab 16

Untuk pembayaran tetap A pada akhir setiap periode:

$$
PV=A\frac{1-(1+k)^{-N}}{k}
$$

Untuk pembayaran awal periode, kalikan nilai tersebut dengan (1+k). Untuk perpetuitas tetap, PV=A/k. Untuk perpetuitas tumbuh dengan arus kas pertama F₁:

$$
PV=\frac{F_1}{k-g},\quad k>g
$$

Anuitas tumbuh terbatas:

$$
PV=\frac{F_1}{k-g}\left[1-\left(\frac{1+g}{1+k}\right)^N\right]
$$

Jika k=g, gunakan limit PV=N×F₁/(1+k), bukan pembagian nol. Contoh anuitas 100 selama tiga tahun pada 10% memberi PV 248,6852. Perpetuitas yang membayar 10 mulai tahun depan pada 10% bernilai 100.

## 2. Bunga nominal, efektif, dan riil — bab 17

$$
EAR=(1+j/m)^m-1
$$

$$
1+r_{nominal}=(1+r_{real})(1+\pi)
$$

π adalah inflasi yang selaras dengan horizon. Bunga nominal 10% dan inflasi 4% memberi bunga riil 1,10/1,04−1 = 5,7692%. Selisih 6% hanya pendekatan.

Untuk continuous compounding, FV=PV×exp(rT). Bunga kontinu dan bunga efektif tidak boleh ditukar tanpa konversi.

## 3. IRR, MIRR, dan penjatahan modal — bab 17 dan 28

IRR menyelesaikan NPV=0. Pada cash flow konvensional dengan satu pengeluaran awal dan seluruh penerimaan setelahnya, NPV turun saat discount rate naik sehingga akar positif, bila ada, bersifat unik. Cash flow nonkonvensional dapat memiliki lebih dari satu akar.

$$
MIRR=\left(\frac{FV(\text{positive cash flows at reinvestment rate})}{-PV(\text{negative cash flows at finance rate})}\right)^{1/N}-1
$$

MIRR menetapkan asumsi pendanaan dan reinvestasi secara eksplisit, tetapi NPV tetap menjadi ukuran nilai absolut. PI dapat membantu ketika dana dibatasi; untuk proyek yang tidak dapat dibagi dan saling bergantung, pilih kombinasi yang memaksimalkan NPV total dengan kendala yang sesuai.

## 4. Covariance, korelasi, dan beta — bab 18–19

$$
Cov(R_i,R_j)=E[(R_i-E[R_i])(R_j-E[R_j])]
$$

$$
\rho_{ij}=\frac{Cov(R_i,R_j)}{\sigma_i\sigma_j}
\qquad
\beta_i=\rho_{iM}\frac{\sigma_i}{\sigma_M}
$$

Jadi beta bukan korelasi saja. Dengan korelasi 0,6, volatilitas saham 30%, dan volatilitas pasar 15%, beta = 1,2. Portofolio dua aset:

$$
\sigma_p^2=w_A^2\sigma_A^2+w_B^2\sigma_B^2+2w_Aw_B\rho_{AB}\sigma_A\sigma_B
$$

Hubungan ini tidak menjamin korelasi historis bertahan saat krisis.

## 5. Spot rate dan forward rate — bab 19

Dengan compounding tahunan dan tanpa risiko kredit:

$$
(1+s_N)^N=(1+s_m)^m(1+f_{m,N})^{N-m}
$$

$$
f_{m,N}=\left(\frac{(1+s_N)^N}{(1+s_m)^m}\right)^{1/(N-m)}-1
$$

YTM tunggal bukan spot curve. Untuk valuasi arus kas bebas risiko yang tepat per tenor, gunakan faktor diskonto tiap tanggal. Forward merupakan tingkat impas yang diturunkan dari harga, bukan kepastian suku bunga yang kelak terjadi.

## 6. Duration dan convexity — bab 20

$$
D_{Mac}=\frac{\sum_t t\,PV(CF_t)}{P}
\qquad
D_{mod}=\frac{D_{Mac}}{1+y}
$$

Untuk pembayaran tahunan:

$$
Convexity=\frac{1}{P}\sum_t\frac{t(t+1)CF_t}{(1+y)^{t+2}}
$$

$$
\frac{\Delta P}{P}\approx-D_{mod}\Delta y+\frac{1}{2}Convexity(\Delta y)^2
$$

Ini pendekatan perubahan yield paralel untuk cash flow tetap tanpa opsi. Opsi call dapat mengubah convexity dan membuat pendekatan sederhana tidak memadai. Perubahan yield satu poin persentase dimasukkan sebagai 0,01, bukan 1.

## 7. Nilai saham berbasis dividen — bab 22 dan 31

$$
P_0=\sum_{t=1}^N\frac{D_t}{(1+k_E)^t}+\frac{P_N}{(1+k_E)^N}
$$

Untuk dividen tumbuh stabil:

$$
P_0=\frac{D_1}{k_E-g}
$$

Hubungan pertumbuhan sederhana g=b×ROE mengasumsikan retention b serta hasil reinvestasi stabil. Dividen yang rendah dapat mencerminkan reinvestasi bernilai, bukan nilai saham yang rendah. Jika kebijakan payout tidak menggambarkan kapasitas kas, FCFE dapat lebih berguna.

## 8. Payoff, profit, dan parity opsi — bab 23

$$
\Pi_{call,long}=\max(S_T-K,0)-Premium
$$

Ini profit nominal sederhana; untuk evaluasi ekonomi pada tanggal yang sama, nilai waktu premi perlu diperhitungkan.

Opsi Eropa dengan dividend yield kontinu q:

$$
C-P=S_0e^{-qT}-Ke^{-rT}
$$

Untuk q=0, rumus kembali ke parity tanpa dividen. Harga call Eropa Black–Scholes dengan q=0:

$$
C=S_0N(d_1)-Ke^{-rT}N(d_2)
$$

$$
d_1=\frac{\ln(S_0/K)+(r+\sigma^2/2)T}{\sigma\sqrt{T}},
\qquad d_2=d_1-\sigma\sqrt{T}
$$

N adalah fungsi distribusi normal baku; σ merupakan volatilitas tahunan. Asumsi utama meliputi volatilitas dan bunga konstan, perdagangan kontinu, pasar tanpa friksi, serta opsi Eropa. Ini bukan model serbaguna untuk warrant dilutif, opsi Amerika, atau convertible dengan risiko kredit.

Untuk S=100, K=100, r=5% kontinu, σ=20%, T=1, call ≈10,4506 dan put ≈5,5735. Harga-harga tersebut memenuhi parity.

## 9. Model binomial satu periode — bab 23

Jika aset naik menjadi Su atau turun menjadi Sd:

$$
p^*=\frac{e^{r\Delta t}-d}{u-d}
$$

$$
C_0=e^{-r\Delta t}[p^*C_u+(1-p^*)C_d]
$$

p* adalah probabilitas risk-neutral, bukan ramalan peluang naik. Syarat tanpa arbitrase adalah d < exp(rΔt) < u. Jika syarat tidak terpenuhi, model input perlu diperiksa, bukan menerima probabilitas negatif.

## 10. FCFF, FCFE, dan APV — bab 28–31

$$
FCFF=EBIT(1-T)+D\&A-Capex-\Delta WC
$$

$$
FCFE=NI+D\&A-Capex-\Delta WC+Net\ Borrowing
$$

FCFF didiskonto dengan WACC; FCFE dengan kE. Net borrowing adalah pinjaman baru dikurangi pelunasan pokok. Jangan mengurangkan bunga dua kali: NI sudah mencakup pengaruh bunga.

$$
APV=V_{unlevered}+PV(Tax\ Shields)+PV(Other\ Financing\ Benefits)-PV(Financing\ Costs)
$$

Metode APV memisahkan nilai operasi dan dampak pendanaan. Risiko tax shield dan kebijakan jumlah utang menentukan discount rate yang tepat. Tidak ada alasan universal untuk selalu mendiskonto semua tax shield dengan risk-free rate.

## 11. Reinvestasi dan terminal value — bab 27–31

$$
Reinvestment\ Rate=\frac{g}{ROIC_{new}}
$$

$$
FCFF_{N+1}=NOPAT_{N+1}\left(1-\frac{g}{ROIC_{new}}\right)
$$

$$
TV_N=\frac{FCFF_{N+1}}{WACC-g}
$$

ROICnew adalah return marginal atas investasi tambahan pada keadaan stabil, bukan otomatis ROCE historis. Memproyeksikan pertumbuhan tanpa capex dan modal kerja yang mendukungnya akan membesar-besarkan nilai. Jika NOPAT tahun depan 120, g=3%, ROICnew=15%, FCFF=96. Pada WACC 10%, terminal value=1.371,4286.

## 12. Enterprise value ke ekuitas — bab 31

$$
Equity=EV-Net\ Debt-NCI-Other\ Claims+Nonoperating\ Assets
$$

Rumus ini mengasumsikan EV mencakup seluruh operasi konsolidasian. Jika arus kas hanya mencakup bagian tertentu, adjustment harus berubah. Hindari mengurangi NCI dua kali, memasukkan kas operasi minimum sebagai kas surplus, atau mengabaikan klaim opsi dan pensiun.

Harga per saham = nilai ekuitas biasa dibagi jumlah saham relevan. Jika instrumen dilutif dimodelkan lewat treasury stock method, jangan sekaligus mengurangkan nilai yang sama sebagai klaim terpisah.

## 13. Residual income dan economic profit — bab 27

$$
EP_t=NOPAT_t-k\,CE_{t-1}
$$

$$
EV_0=CE_0+\sum_{t=1}^{\infty}\frac{EP_t}{(1+k)^t}
$$

Kesetaraan dengan DCF memerlukan hubungan akuntansi modal, reinvestasi, arus kas, serta kondisi terminal yang konsisten. Jangan menjumlahkan EVA tanpa mendiskonto atau menghitung capital charge pada modal yang tidak sesuai periode.

## 14. Beta unlevered dan relevered — bab 29 dan 32–33

Dengan pendekatan beta utang nol dan asumsi pajak yang sesuai:

$$
\beta_U=\frac{\beta_L}{1+(1-T)D/E}
\qquad
\beta_{L,target}=\beta_U[1+(1-T)D/E_{target}]
$$

Jika beta utang tidak dapat diabaikan, gunakan hubungan risiko aset dan klaim yang lebih lengkap. Perusahaan net cash dan portofolio beberapa bisnis memerlukan pemisahan aset operasi serta kas, bukan penerapan mekanis leverage negatif.

## 15. Rights issue dan nilai hak — bab 25 dan 38

Untuk n saham lama berharga P yang memberikan hak membeli satu saham baru pada Ps:

$$
TERP=\frac{nP+P_s}{n+1}
\qquad
Right_{per\ old\ share}=P-TERP
$$

Hak-hak itu bernilai jika dapat digunakan atau diperdagangkan. Biaya transaksi, perubahan informasi, dan keterbatasan penjualan dapat membuat realisasi berbeda dari formula teoritis.

## 16. Akresi EPS akibat buyback — bab 37

Pada harga pembelian P dan biaya pendanaan setelah pajak i, buyback cenderung menaikkan EPS jika earnings yield melebihi biaya tersebut:

$$
\frac{EPS}{P}>i
$$

Ini syarat mekanis sederhana, bukan syarat penciptaan nilai. Untuk nilai, periksa harga terhadap nilai wajar, risiko, covenant, dan opportunity cost penggunaan kas.

## 17. Nilai sinergi dan return pembeli — bab 44–45

$$
V_{combined}=V_A+V_B+PV(Net\ Synergies)
$$

$$
NPV_A=PV(Net\ Synergies)-Premium-Deal\ Costs
$$

Bila biaya integrasi sudah termasuk net synergies, jangan dikurangkan lagi. Sinergi pendapatan harus memakai margin tambahan dan probabilitas realisasi, bukan menyamakan tambahan penjualan dengan kas bebas.

## 18. Return LBO — bab 46

$$
MOIC=\frac{\text{seluruh penerimaan ekuitas}}{\text{seluruh modal ekuitas yang ditanam}}
$$

MOIC tidak memperhitungkan waktu. Untuk satu investasi awal dan satu penerimaan akhir:

$$
IRR=MOIC^{1/N}-1
$$

MOIC 2× dalam tiga tahun memberi IRR 25,9921%, sedangkan 2× dalam lima tahun memberi 14,8698%. Distribusi interim dan modal tambahan mengharuskan IRR berdasarkan tanggal arus kas.

## 19. Diskon pemasok dan biaya kredit dagang — bab 48

Jika diskon d diberikan untuk pembayaran pada hari a, sedangkan pembayaran penuh jatuh tempo hari b:

$$
Annualized\ Simple\ Cost\approx\frac{d}{1-d}\frac{365}{b-a}
$$

Syarat 2/10 net 30 memberi biaya sederhana kehilangan diskon sekitar 37,2449% per tahun. Jika memakai compounding untuk perbandingan efektif, gunakan (1+d/(1−d))^(365/(b−a))−1. Definisi hari dan kemampuan mengakses dana perlu dijelaskan.

## 20. Hedge kurs dan interest rate swap — bab 50

Untuk importir dengan kewajiban mata uang asing Q dan forward K dalam IDR per unit valuta:

$$
Locked\ IDR=QK
$$

Forward menukar kepastian dengan hilangnya keuntungan dari spot yang lebih menguntungkan. Swap pembayar fixed dan penerima floating memberi pembayaran bersih sederhana pada reset yang sesuai:

$$
Net\ Payment=Notional(Fixed-Floating)\Delta t
$$

Tanda, reset, day-count, dan collateral mengikuti kontrak. Notional bukan biaya transaksi dan tidak selalu dipertukarkan.

## 21. VaR, expected shortfall, dan risiko ekor — bab 50

$$
VaR_{\alpha}(L)=Quantile_{\alpha}(L)
$$

Untuk distribusi kontinu, expected shortfall adalah ekspektasi kerugian pada ekor di atas kuantil tersebut. VaR 99% tidak berarti hanya dapat rugi sebesar VaR; sisa 1% skenario dapat jauh lebih buruk. Model harus menyatakan horizon, confidence, metode, asumsi korelasi, dan perlakuan posisi tidak likuid.

## 22. Aturan konsistensi sebelum menghitung

| Pilihan arus kas | Pasangan tingkat diskonto |
| --- | --- |
| FCFF sesudah pajak, sebelum pendanaan | WACC sesudah pajak dengan risiko operasi yang sesuai |
| FCFE sesudah bunga dan net borrowing | Cost of equity |
| Arus kas nominal | Tingkat nominal mata uang yang sama |
| Arus kas riil | Tingkat riil |
| Arus kas bebas risiko per tenor | Spot discount factor yang sesuai |
| Cash flow bertanggal tidak beraturan | Diskonto berdasarkan tanggal aktual |

Sebelum menyimpulkan, pastikan formula menggunakan satuan yang benar, tanda arus kas konsisten, data sumber dapat ditelusuri, dan hasil numerik masuk akal secara ekonomi.
