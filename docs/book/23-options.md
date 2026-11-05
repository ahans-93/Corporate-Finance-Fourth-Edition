# Options

Halaman PDF 422–443. [PDF asli](../../CoreCourseFinancialAccounting.pdf#page=422).

> Ekstraksi otomatis bahasa asli. Rumus bertingkat, tabel, grafik, ligatur, urutan kolom, dan teks gambar dapat berubah atau tidak terbaca. Cocokkan dengan PDF sebagai acuan visual. Nomor PDF berbeda dari nomor cetak.

[Catatan belajar bab 23](../study/23-options.md) · [Daftar isi](../../SUMMARY.md)

## Halaman PDF 422

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=422)

~~~text
c23.indd 12:37:44:PM  09/05/2014 Page 406Trim Size: 189 X 246 mm
SECTION 2
Chapter 23
OPTIONS
The haunted house, or how to pay for being frightened!
In the previous chapters, we saw that when calculating net present value, the required
rate of return includes a risk premium that is added to the time value of money. The study
of options is useful from a purely financial point of view, as it highlights the notion of
remuneration of risk.
True, options are more complex than shares or bonds. Moreover, in their daily use
they have more to do with financial management than finance. However, we will see that
many financial assets (warrants, stock options) can be analysed as options or as the com-
bination of an option and a less risky asset. Have some fun by discovering the options
hidden in any financial product!
A convertible bond can be seen as a combination of a conventional bond and an
option. An undrawn revolving credit facility can be analysed as an option on a loan.
We will also examine how options theory can be applied to major financial strategy
decisions within a company.
Options are an effective tool of analysis whose applications are limited only by ﬁnancial
managers’ imaginations.
The purpose of this chapter is not to make you a wizard in manipulating options or to
teach you the techniques of speculation or hedging with options, but merely to show you
how they work in practice.
Section 23.1
DEFINITION AND THEORETICAL FOUNDATION OF OPTIONS
An option gives you the right to buy or sell an asset at a predetermined price during a
predetermined period.
1/ SOME BASIC DEFINITIONS
There are call (buy) options and put (sell) options. The asset that can thereby be bought
or sold is called the underlying asset. This can be either a financial asset (stock, bond,
~~~

## Halaman PDF 423

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=423)

~~~text
Chapter 23 OPTIONS 407
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 407Trim Size: 189 X 246 mm
Treasury bond, forward contract, currency, stock index, etc.) or a physical one (a raw
material or mining asset, for example).
The price at which the underlying asset can be bought or sold is called the strike
price. The holder of an option may exercise it (i.e. buy the underlying asset if he holds
a call option or sell it if he holds a put option) either at a given date ( exercise date )
or at any time during a period called the exercise period, depending on the type of
option held.
A distinction is made between US-style options (the holder can exercise his right at
any moment during the exercise period) and European-style options (the holder can only
exercise his right on the exercise date). Most listed options are US-style options, and they
are found on both sides of the Atlantic, whereas most over-the-counter (OTC) options are
European-style.
Legally speaking, call options are a promise to sell made by the seller of the call option
to the buyer of the call option.
Here are two examples:
Let’s say Peter sells Helmut a call option on the insurance company Allianz
having an €85 strike price and maturing in nine months. For nine months (US-style
option) or after nine months (European-style option), Helmut will have the right to buy
one Allianz share at a price of €85, regardless of Allianz’s share price at that moment.
Helmut is not required to buy a share of Allianz from Peter, but if Helmut wants to, Peter
must sell him one for €85.
Obviously, Helmut will exercise his option only if Allianz’s share price is above €85.
Otherwise, if he wants to buy an Allianz share, he will simply buy it on the market for
less than €85.
Now let’s say that Paul buys from Clara put options on $1m in currency at an exchange
rate of €1.1/$, exercisable six months from now. Paul may, in six months’ time (if it’s a
European-style option) sell $1m to Clara at €1.1/$, regardless of the dollar’s exchange
rate at that moment. Paul is not required to sell dollars to Clara but, if he wants to, Clara
must buy them from him at the agreed price.
Obviously, Paul will only exercise his option if the dollar is trading below €1.1.
Legally speaking, put options are a promise to buy made by the seller of the put option
to the buyer of the put option.
The above examples highlight the fundamentally asymmetric character of an option.
An option contract does not grant the same rights or obligations to each side. The buyer
of any option has the right but not the obligation, whereas the seller of any option is
obliged to follow through if the buyer requests.
The value at which an option is bought or sold is sometimes called the premium. It is
obviously paid by the buyer to the seller, who thereby obtains some financial compensa-
tion for a situation in which he has all the obligations and no rights.
Hence, a more precise definition of an option would be:
An option is a contract between two sides, under which one side gives the other side the
right (but not the obligation) to buy from him (a call option) or to sell to him (a put
option) an asset, in exchange for the payment of a premium.
~~~

## Halaman PDF 424

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=424)

~~~text
FINANCIAL  SECURITIES408
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 408Trim Size: 189 X 246 mm
This asset will be bought (or sold) at a predetermined price called the strike price,
during a period of time (the exercise period for US-style options), or at a precise date
(the exercise date for European-style options).
When the option matures, we can show the payouts for the buyer and the seller of the call
option in the following way:
Gain
Call option
Buyer
Seller
Price of the
underlying
at maturity
Premium
Strike price
At maturity, if Allianz is trading at €90, Helmut will exercise his option and buy his
Allianz share at €85. He can then sell it again if he wishes, and make €5 in profit (minus
the premium he paid for the option).
Similarly, for the put option:
Gain
Loss
Buyer
Seller
Put option
Price of the
underlying
at maturity
Premium
Strike price
This diagram highlights the asymmetry of risk involved: the buyer of the option risks
only the premium, while his potential profit is almost unlimited, while the seller’s gain is
limited, but his loss is potentially unlimited.
~~~

## Halaman PDF 425

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=425)

~~~text
Chapter 23 OPTIONS 409
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 409Trim Size: 189 X 246 mm
2/ THE THEORETICAL BASIS OF OPTIONS
In a risk-free environment, if we knew today with certainty what would happen tomorrow,
options would not exist as they would be completely unnecessary.
If the future were known with certainty there would be no risk and all financial assets
would bring in the same return, i.e. the risk-free rate. What purpose would an option have,
i.e. the right to buy or sell, if we already knew what the price would be at maturity? What
purpose would a call option on Siemens serve, at a strike price of €170, if we already
knew that Siemens’s share price would be below €160 at maturity and that the option
would therefore not be exercised? And if we knew that, at maturity, Siemens’s share price
would be €250, the price of the option would be such that it would offer the risk-free rate,
just like Siemens’s shares, since the future would be known with certainty.
Options would not exist if the future were known with certainty. In a risky environment,
options remunerate the risk of an uncertain future. The basis of an option is therefore
the remuneration of risk.
Options might therefore be called pure financial products, as they are merely remunera-
tion of risk. There is no other basis to the value of an option.
More generally, all risk premiums are a sort of option.
Section 23.2
MECHANISMS USED IN PRICING OPTIONS
Let’s suppose that Felipe buys a call option on Solvay at a €50 strike price, maturing in
nine months, and simultaneously sells a put option on the same stock at a €50 strike
maturing in nine months. Assuming the funds paid for the call option are largely offset by
the funds received for the sale of the put option, what will happen at maturity?
If Solvay is trading at above €50, Felipe will exercise his call option and pay €50. The put
option will not be exercised, as his counterparty will prefer to sell Solvay at the market price.
If Solvay is trading below €50, Felipe will not exercise his call option, but the put
option that he sold will be exercised and Felipe will have to buy Solvay at €50.
Hence, regardless of the price of the underlying asset, buying a call option and sell-
ing a put option on the same underlying asset, at the same maturity and at the same strike
price is the same thing as a forward purchase of the underlying asset at maturity at the
strike price.
In other words:
Buying a call option and selling a put option is a forward purchase of the underlying
asset; we say there is put–call parity.
Assuming fairly valued markets, we can thus deduce that at the maturity of the exercise
period:
Value at maturity of a call option – Value at maturity of a put option = Value at maturity
of the underlying asset – strike price
~~~

## Halaman PDF 426

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=426)

~~~text
FINANCIAL  SECURITIES410
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 410Trim Size: 189 X 246 mm
It looks like this on a chart:
Gain
Loss
Buying a call option
Price of
underlying
Strike price
Gain
+ Selling a put option
Buying, selling, forward
Loss
Price of
underlying
Strike price
Gain
= Forward purchase
Loss
Price of
underlying
Strike price
We can see that the profit (or loss) of this combination is indeed equal to the difference
between the price of the underlying asset at maturity and the strike price.
Let’s now consider the following transaction: Evgueni wants to buy Solvay stock, but
does not have the funds necessary at his immediate disposal. However, he will be receiv-
ing €50 in nine months, enough to make the purchase. He can thus borrow the present
value of €50, nine months out, and buy Solvay.
At maturity, the profit (or loss) on this transaction will thus be equal to the difference
between the value of the Solvay shares and the repayment of the €50 loan.
So we are back to the previous case and can thus affirm that in value terms:
Buying a call option and selling a put option on the same underlying asset, at the same
strike price, and at the same maturity, is like buying the underlying asset by borrow-
ing the present value of the strike price, as long as the two options are European-style
options and as long as there is no dividend payout in the interim.
We have used a stock for the underlying asset, but the above statement applies to any
underlying asset (currencies, bonds, raw materials, etc.).
This can be expressed in eight different ways, which are all equivalent:
 1. Buying a call option and selling a put option is like buying the underlying asset and
borrowing at the risk-free rate.
 2. Buying a call option and selling the underlying asset is like buying a put option and
borrowing at the risk-free rate.
 3. Buying a call option and investing in a risk-free asset is like buying the underlying
asset and buying the put option.
 4. Buying a put option and selling a call option is like investing in a risk-free asset and
selling the underlying asset.
 5. Buying a put option and buying the underlying asset is like buying a call option and
investing in a risk-free asset, and we are back to point 3 above.
 6. Buying a put option and borrowing at the risk-free rate is like buying a call option
and selling the underlying asset, and we are back to point 2 above.
~~~

## Halaman PDF 427

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=427)

~~~text
Chapter 23 OPTIONS 411
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 411Trim Size: 189 X 246 mm
Also:
7. Buying a put option is like buying a call option and selling the underlying asset and
investing in a risk-free asset.
8. Buying a call option is like buying a put option and buying the underlying asset and
borrowing at the risk-free rate.
Points 7 and 8 show that we can “manufacture” a synthetic call option based on a put
option and vice versa.
When we have three investment opportunities on an underlying asset, we can always
recreate the fourth, as long as we can borrow and invest in the risk-free asset!
Section 23.3
ANALYSING OPTIONS
1/ INTRINSIC VALUE
Intrinsic value is the difference (if it is positive) between the price of the underlying asset
and the option’s strike price. For a put option, it’s the opposite. In the rest of this chapter,
unless otherwise mentioned, we will use call options as examples.
By definition, intrinsic value is never negative.
Let’s take a call option on sterling, with a strike price of €1.5/£ and maturing at end-
December. Let’s say that it is now June and that the pound is trading at €1.6.
What is the option’s value? The holder of the option may buy a pound for €1.5, while
the pound is currently at €1.6.
This immediate possible gain is none other than the option’s intrinsic value, which
will be billed by the seller of the option to the buyer. The option will be worth at least
€0.1.
Technically, a call option is said to be:
t out of the money when the price of the underlying asset is below the strike price
(zero intrinsic value);
t at the money when the price of the underlying asset is equal to the strike price (zero
intrinsic value);
t in the money when the price of the underlying asset is above the strike price (positive
intrinsic value).
The reader will have understood that a put option is said to be:
t out of the money when the price of the underlying asset is above the strike price
(zero intrinsic value);
t at the money when the price of the underlying asset is equal to the strike price (zero
intrinsic value);
t in the money when the price of the underlying asset is below the strike price (posi-
tive intrinsic value).
~~~

## Halaman PDF 428

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=428)

~~~text
FINANCIAL  SECURITIES412
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 412Trim Size: 189 X 246 mm
2/ TIME  VALUE
Now let’s imagine that sterling is trading at €1.4 in October. The option would be out of
the money (€1.4 is less than the €1.5 strike price) and the holder would not exercise it.
Does this mean that the option is worthless? No, because there is still a chance, however
slight, that sterling will move over €1.5 by the end of December. This would make the
option worth exercising. So the option has some value, even though it is not worth exercis-
ing right now. This is called time value.
For an in-the-money option, i.e. whose strike price ( €1.5) is below the value of the
underlying asset (let’s now assume that £1 = €1.7), intrinsic value is €0.2. But this intrin-
sic value is not all of the option’s value. Indeed, we have to add time value, which ulti-
mately is just the anticipation that intrinsic value will be higher than it is currently. For
there is always a probability that the price of the underlying asset will rise, thus making it
more worthwhile to wait to exercise the option.
The anticipation of an even greater intrinsic value is called the time value of an option.
In more concrete terms, time value represents “everything that could happen” from now
until the option matures.
Hence:
An option’s value = intrinsic value + time value.
Value of
the option
Value of the underlying asset
Time value
Value of a call option
Intrinsic value
Strike price
Value of
the option
Underlying asset value
Time value
Value of a put option
Intrinsic value
Exercise price
~~~

## Halaman PDF 429

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=429)

~~~text
Chapter 23 OPTIONS 413
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 413Trim Size: 189 X 246 mm
Time value diminishes with the passage of time, as the closer we get to the maturity date,
the less likely it is that the price of the underlying asset will exceed the strike price by that
date. Time value vanishes on the date the option expires.
This means that an option is worth at least its intrinsic value, but is there an upper
limit on the option’s value?
In our example, the value at maturity of the call option on sterling is as follows:
t If sterling is trading above €1.5, the option is worth the current price of sterling less
€1.5, i.e. its intrinsic value, which is below the value of the underlying asset.
t If sterling is below or equal to €1.5, the option will be worthless (i.e. no intrinsic
value) and therefore even further below the price of the underlying asset.
This means that if the option’s value is equal to the price of the underlying asset, all
operators will sell the option to buy the underlying asset, as their gain will be greater in
any case.
The value of a call option is always above its intrinsic value, as it possesses time value,
but it is always below the value of the underlying asset.
Section 23.4
PARAMETERS TO VALUE OPTIONS
There are six criteria for determining the value of an option. We have already discussed
one of them, the price of the underlying asset. The other five are:
t the strike price;
t the volatility of the underlying asset;
t the option’s maturity;
t the risk-free rate;
t the dividend or coupon, if the underlying asset pays one out.
1/ PRICE OF THE UNDERLYING ASSET
As we saw earlier, all other criteria being equal, the value of a call option will be higher
with a higher price of the underlying asset.
Symmetrically, the value of a put option will be lower with a higher price of the
underlying asset.
2/ STRIKE PRICE
Assuming the same value of the underlying asset, the higher the strike price, the lower
the value of a call option.
~~~

## Halaman PDF 430

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=430)

~~~text
FINANCIAL  SECURITIES414
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 414Trim Size: 189 X 246 mm
Hence, and again assuming the same value for the underlying asset, the higher the strike
price, the greater the value of a put option.
This is just common sense: the higher a call option’s strike price, the less chance the price
of the underlying asset will exceed it. It is thus normal that the value of this call option is
lower. However, the price of the put option will rise as the underlying asset can be sold
at a higher price.
Option value
Value of the underlying
asset
K
1 K2
C2(V0)
C1(V0)
C1 C2
V0
Value of the underlying asset
Option value
Exercise price Value of the underlying
asset
Option on an asset with a
volatility of 15%
Option on an asset with a
volatility of 10%
Time value rises with the volatility
3/ VOLATILITY  IN THE  VALUE  OF  THE  UNDERLYING  ASSET
The value of both a call and a put option rises with the volatility in the value of the
underlying asset.
Here again, this is easy to understand: the more volatile the underlying asset, the more
likely it is to rise and fall sharply. In the first case, the return will be greater for the holder
of a call option; in the second, it will be greater for the holder of a put option. As an option
is nothing more than pure remuneration of risk, the greater that risk is, the greater the
remuneration must be, and thus the option’s value.
Time value rises
with the volatility
of assets
The value of a
call option (call)
is inversely
proportional to
the strike price.
~~~

## Halaman PDF 431

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=431)

~~~text
Chapter 23 O PTIONS 415
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 415Trim Size: 189 X 246 mm
4/ THE TIME  TO MATURITY
The further away maturity is, the greater the value of both a call and a put option.
You can easily see that the further away maturity is, the greater the likelihood of fluctua-
tions in the price of the underlying asset. This raises the option’s value.
Option value
Exercise price Value of the underlying
asset
Maturity 6 months
The further away maturity
Maturity 3 months
5/ THE RISK -FREE  RATE
We have seen that the passage of time has a cost: the risk-free rate. The further away the
maturity date on an option, the further away the payment of that cost. The holder of a call
(put) option will thus have a cash advantage (disadvantage) that depends on the level of
the risk-free rate.
The value of a call option increases with the risk-free rate, while the value of a put
option is an inverse function of the risk-free rate.
The buyer of the call option pays the premium, but pays the strike price only when exer-
cising the option. Everything happens as if he was buying on credit until “delivery”. The
amount borrowed is, in fact, the present value of the strike price discounted at the risk-free
rate, as we have seen previously.
Interest rates have much less influence on the value of an option than the other five
factors.
6/ DIVIDENDS  OR  COUPONS
When the underlying asset is a stock or bond, the payment of a dividend or coupon lowers
the value of the underlying asset. It thus lowers the value of a call option and raises the
value of a put option. This is why some investors prefer to exercise their calls (on US-style
options) before the payment of the dividend or coupon.
The further away
maturity is, the
greater time
value is.
~~~

## Halaman PDF 432

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=432)

~~~text
FINANCIAL  SECURITIES416
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 416Trim Size: 189 X 246 mm
We can summarise the change in price of the option depending on the change in
criterion in the following table:
Criterion Call Put
Price of the underlying asset
Strike price
Volatility of the underlying asset
Option’s maturity
The risk-free rate
Dividend or coupon
Section 23.5
METHODS  FOR  PRICING  OPTIONS
1/ REASONING  IN TERMS  OF ARBITRAGE  (BINOMIAL  METHOD )
To model the value of an option, we cannot use traditional discounting of future cash flow
at the required rate of return as we have for other financial securities, because of the risk
involved. Cash flow depends on whether or not the option will be exercised and the risk
varies constantly. Hence, the further the option is into the money, the higher its intrinsic
value and the less risky it is.
Cox et al. (1979) thus had the idea of using arbitrage logic in comparing the profit
generated with options, with a direct position on the underlying asset.
Let’s take the example of a call option with a €105 strike price on a given stock (cur-
rently trading at €100) and for a given maturity.
Let’s also assume that there are only two possibilities at the end of this period: either
the stock is at €90 or it is at €110. At maturity, our option will be worth its intrinsic value,
i.e. either €0 or €5, or €0 or €20 if we held four options instead of just one.
We can try to obtain the same result (€0 or €20) in the same conditions using another
combination of securities (a so-called replicating portfolio). If we achieve this result,
the four call options and this other combination of securities should have the same value.
If we can determine the value of this other combination of securities, we will have suc-
ceeded in valuing the call option.
To do so, let’s say you borrow (at 5%, for example) a sum whose value (principal and
interest) will be €90 at the end of the period concerned, and then buy a share for €100 today.
At the end of the period:
 t either the share is worth €110, in which case the combination of buying the share and
borrowing money is worth €110 −  €90 = €20; or
 t the share is worth €90, in which case the replicating portfolio is worth 90 −  90 = 0.
~~~

## Halaman PDF 433

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=433)

~~~text
Chapter 23 O PTIONS 417
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 417Trim Size: 189 X 246 mm
Since the two combinations – the purchase of four call options on the one hand, and
borrowing funds and buying the share directly – produce the same cash flows, regardless
of what happens to the share price, their values are identical. Otherwise, arbitrage traders
would quickly intervene to re-establish the balance. So what is the original value of this
combination? Let’s look at it this way: €14.3 corresponds also to the value of the four
call options. We thus deduce that the call option at a €105 strike is worth €3.58. We have
valued the option using arbitrage theory.
Purchase of a share: €100
− borrowing of a sum that at maturity would be worth €90, hence, at 5%, 90/1.05
= €85.7
= Value: €14.3
“Delta” is the number of shares that must be bought to duplicate an option. In our
example, four calls produce a profit equivalent to the purchase of one share. The option’s
delta is therefore 1/4, or 0.25.
More generally, delta is deﬁned as the ratio between the variation in the option’s value,
and the variation in the price of the underlying asset.
Hence:
δ = −
− =50
110 90 02 5.
We can therefore conclude that:
Value of a call option = δ × (Price of the underlying asset −  PV of capital borrowed)
Our example above obviously oversimplifies in assuming that the underlying asset can
only have two values at the end of the period. However, now that we have understood
the mechanism, we can go ahead and reproduce the model in backing up two peri-
ods (and not just one) before the option matures. This is called the binomial method,
because there are two possible states at each step. By multiplying the number of peri-
ods or subdividing each period into subperiods, we can obtain a very large number
of very small subperiods until we have a very large number of values for the stock at
the option’s maturity date, which is more realistic than the simplified schema that we
developed above.
~~~

## Halaman PDF 434

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=434)

~~~text
FINANCIAL  SECURITIES418
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 418Trim Size: 189 X 246 mm
Value of underlying asset
130
25
δ = 1
δ = 0.82
δ = 0.25
δ = 0.18
δ = 0
δ = 0.65
120
20
110
15.53
100
3.58
80
0
70
0
100
11.68
110
5
90
0
90
2.47
Value of the underlying asset
Option value2/ THE BLACK –SCHOLES  MODEL
In a now famous article, Fisher Black and Myron Scholes (1972) presented a model for
pricing European-style options that is now very widely used. It is based on the construc-
tion of a portfolio composed of the underlying asset and a certain number of options such
that the portfolio is insensitive to fluctuations in the price of the underlying asset. It can
therefore return only the risk-free rate.
The Black–Scholes model is the continuous-time (the period approaches 0) version
of the discrete-time binomial model. The model calculates the possible prices for the
underlying asset at maturity, as well as their respective probabilities of occurrence,
based on the fundamental assumption that this is a random variable with a log-normal
distribution.
For a call option, the Black–Scholes formula is as follows:
Value of the call option ( ) ( )=× −× ×
×Nd V Nd K e Tr F12
−
with
d
V
K rT
T
dd T1
2
21
2=
⎛
⎝
⎜
⎜
⎜
⎞
⎠
⎟
⎟
⎟
⎟++⎛
⎝
⎜
⎜
⎜
⎞
⎠
⎟
⎟
⎟
⎟×
×
=− ×
ln
F
and
σ
σ
σ
Here is what it looks like graphically:
~~~

## Halaman PDF 435

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=435)

~~~text
Chapter 23 O PTIONS 419
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 419Trim Size: 189 X 246 mm
where V is the current price of the underlying asset, N(d) is a cumulative standard normal
distribution (average = 0, standard deviation = 1), K is the option’s strike price, e is the
exponential function, rF is the continual annual risk-free rate, σ the instantaneous standard
deviation of the return on the underlying asset, T the time remaining until maturity (in
years), and ln the Naperian logarithm.
In practice, the instantaneous return is equal to the difference between the logarithm
of the share price today and of yesterday’s share price.
r VV o=−ln ln1
To cite an example: the value of a European-style nine-month call, with a strike price
of €100, share price today of €90, a 3.2% risk-free rate and a 20% standard deviation of
instantaneous return, is €3.3.
Comparing the model equation formula from page 417, you will see that N(d1) is the
option’s delta, while KeTÅ~rF represents the present value of the strike price.
Hence:
Call option’ s value Present value of the strike =× − ×VN dδ () 2 pprice.
The model confirms that the value of a call option:
 t rises with the current price of the underlying asset (V);
 t falls with the strike price’s net present value, which depends on the risk-free rate (rF)
and the time remaining till maturity T ;
 t rises with the volatility σ, multiplied by the amount of time remaining till maturity.
The Black–Scholes model was initially designed for European-style stock options. The
developers of the model used the following assumptions:
 t no dividend payout throughout the option’s life;
 t constant volatility in the underlying asset over the life of the option, as well as the
interest rate;
 t liquidity of the underlying asset so that it can be bought and sold continuously, with
no intermediation costs;
 t that market participants behave rationally!
More complex models have been derived from Black and Scholes to surmount these prac-
tical constraints. The main ones are those of Garman and Kohlhagen (1983) for currency
options and Merton (1976), which reflects the impact of the payment of a coupon during
the life of a European-style option.
US-style options are more difficult to analyse and depend on whether or not the
underlying share pays out a dividend:
 t If the share pays no dividend, the holder of the option has no reason to exercise it
before it matures. He will sell his option rather than exercise it, as exercising it will
make it lose its time value. In this case, the value of the US-style call option is thus
identical to the value of a European-style call option.
 t If the share does pay a dividend, the holder of the call may find it worthwhile to
exercise his option the day before the dividend is paid. To determine the precise value
of such an option, we have to use an iterative method requiring some calculations
developed by Roll (1977). However, we can simplify for a European-style call option
~~~

## Halaman PDF 436

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=436)

~~~text
FINANCIAL  SECURITIES420
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 420Trim Size: 189 X 246 mm
on an underlying share that pays a dividend: the Black–Scholes model is applied to
the share price minus the discounted dividend.
The formula for valuing the put option is as follows:
Value of the put option =−× × − ×
−Nd Ke N d V Tr F() ( )21
×
Of the six criteria of an option’s value, five are “given” (price of the underlying asset,
strike price, maturity date, risk-free rate and, where applicable, the dividend); only one is
unknown: volatility.
From a theoretical point of view, volatility would have to be constant for the Black–
Scholes model to be applied with no risk of error, i.e. historical volatility (which is
observed) and anticipated volatility would have to be equal. In practice, this is rarely the
case: market operators adjust upward and downward the historical volatility that they
calculated (over 20 days, one month, six months, etc.) to reflect their anticipation of the
future stability or instability of the underlying asset. However, several classes of options
(same underlying, but different maturity or strike price) can be listed for the same under-
lying asset. This allows us to observe the implied volatility of their quoted prices and thus
value the options of another class.
This is how anticipated volatility is obtained and is used to value options. This prac-
tice is so entrenched that options market traders trade anticipation of volatility directly.
Anticipated volatility is then applied to models to calculate the value of the premium.
The Black–Scholes model can thus be used “backwards”, i.e. by taking the option’s
market price as a given and calculating implied volatility. The operator can then price
options by tweaking the price on the basis of his own anticipation. He buys options whose
volatility looks too low and sells those whose implied volatility looks too high.
It is interesting to note that, despite these simplifying assumptions, the Black–Scho-
les model has been de facto adopted by market operators, each of them adapting it to the
underlying asset concerned.
Section 23.6
TOOLS  FOR  MANAGING  AN OPTIONS  POSITION
Managing a portfolio of options (which can also be composed of underlying assets or
the risk-free asset) requires some knowledge of four parameters of sensitivity that help
us measure precisely the risks assumed and develop speculative, hedging and arbitrage
strategies.
1/ THE IMPACT  OF FLUCTUATIONS  IN THE  UNDERLYING  ASSET : DELTA  AND  GAMMA
We have already discussed the delta, which measures the sensitivity of an option’s value
to fluctuations in the value of the underlying asset. For calls and puts that are significantly
out of the money, the value of the option may not change much when the underlying asset
moves up or down. As the price of the underlying asset moves to a level substantially
above the strike for calls or below the strike for puts, the option becomes more valuable
and more sensitive to changes in the underlying asset.
~~~

## Halaman PDF 437

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=437)

~~~text
Chapter 23 OPTIONS 421
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 421Trim Size: 189 X 246 mm
Mathematically, the delta is derived from the option’s theoretical value vis-à-vis the
price of the underlying asset and is thus always between 0 and 1, either positive or nega-
tive. Whether it is positive or negative depends on the type of option.
The delta of a call option is positive, since an increase in the price of the underlying
asset increases the option’s value.
The delta of a put option is negative, since an increase in the price of the underlying
asset lowers the option’s value.
We have seen that, when using the Black–Scholes formula, the delta of a call option is
equal to N(d
1). The delta of a put option is equal to N(d1) −  1. This relationship is prized
by managers of options portfolios, as it links the option’s value and the value of the
underlying asset directly. Indeed, we have seen that the delta is, above all, an underlying
equivalent: a delta of 0.25 tells us that a share is equivalent to 4 options. But above all,
managers use the delta as an indicator of sensitivity: how much does the option’s value
vary in euros when the underlying asset varies by one euro?
The delta of a call option far in-the-money is very close to 1, as any variation in the
underlying asset will show up directly in the option’s value, which is essentially made up
of intrinsic value.
Similarly, a call option that is far out-of-the-money is composed solely of its time
value and a variation in the underlying asset has little influence on its value. Its delta is
thus close to 0.
The delta of an at-the-money call option is close to 0.5, indicating that the option has
as much chance as not of being exercised.
This is expressed in the following table:
Out-of-the-money At-the-money In-the-money
Call option 0 < delta < 0.5 delta = 0.5 0.5 < delta < 1
Put option − 0.5 < delta < 0 delta =− 0.5 − 1 < delta <− 0.5
The delta can also express probability of expiration in-the-money for options close to
maturity and whose underlying asset is not too volatile: a delta of 0.80 means that there is
an 80% probability that the option will expire in-the-money.
Unfortunately, the delta itself varies with fluctuations in the underlying asset and with
the passing of time.
Changes in the delta of an option create either a risk or an opportunity for investors and
traders. Hence, the idea of measuring the sensitivity of delta to variations in the value of the
underlying asset: this is what gamma does. Mathematically, it is none other than a deriva-
tive of the delta vis-à-vis the underlying asset, and is often called the delta of the delta!
The gamma of an option is largest near the strike price. A zero-gamma options posi-
tion is completely immune to fluctuations in the value of the underlying asset.
2/ THE IMPACT OF TIME : THETA
Options are like people: they run down with time. Even if there is no change in the underly-
ing asset price, the passage of time alone shows up in gains or losses for the option’s holder.
~~~

## Halaman PDF 438

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=438)

~~~text
FINANCIAL  SECURITIES422
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 422Trim Size: 189 X 246 mm
Mathematically speaking, the theta is equal to the opposite of the derivative of the
theoretical value of the option with respect to time. Theta measures how much an option
loses in value if no other factors change.
3/ THE IMPACT  OF VOLATILITY : VEGA
The vega can be defined as the rate of change in the derivative of the theoretical value
of the option vis-à-vis implied volatility. Vega is always positive for a call option, as for
a put option, as we have seen that the time value of an option is an increasing function
of volatility.
All other factors being equal, the closer an option is to being in the money (with
maximum time value), the greater the impact of an increase in volatility.
While each of the tools presented here is highly useful in and of itself, combining
them tells us even more. In practice, it is impossible to create a position that is neutral on
all criteria at once. No return is possible when taking no risk. No pain, no gain! Hence,
a delta-neutral position and a gamma-negative position must necessarily have a positive
theta in order to be profitable.
4/ IMPLICIT  VOLATILITY
From 1990, the CBOE (Chicago Board Options Exchange) has calculated the VIX, an
index of the implicit volatility of the Standard & Poor’s 100, using at-the-money options
with a maturity shorter than one month. The options on the S&P 100 are sufficiently
liquid to consider this index representative of the implicit volatility on the market.
The following graph shows the evolution of VIX from its initial launch.
50
60
70
80
90
Volatility on US stocks (VIX on S&P 500)%
0
1990199119921993199419951996199719981999200020012002200320042005200620072008200920102011201220132014
10
20
30
40
Source: Datastream (CBOE volatility Index on S&P 100 until 31/2/2006, on S&P 500 since)
If returns
actually followed
a Gaussian
distribution, the
Dow Jones would
change daily
by more than
7% only once in
300 000 years. In
the 20th century,
there were 48
such changes, and
there have been
two since 2000.
Recent studies
have shown that
the distribution
of return has a
conﬁguration
something like
this.
~~~

## Halaman PDF 439

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=439)

~~~text
Chapter 23 O PTIONS 423
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 423Trim Size: 189 X 246 mm
5/ MODEL  RISK
Options markets, whether organised (listed) or not (over-the-counter), have developed
considerably since the mid-1970s, as a result of the need for hedging (of currency risks,
interest rates, share prices, etc.), an appetite for speculation (an option allows its holder to
take a position without having to advance big sums), and the increase in arbitrage trading.
In these conditions, a new type of approach to risk has developed on trading floors:
model risk. The notion of model risk arose when some researchers noticed that the Black–
Scholes model was biased, since (like many other models) it models share prices on the
basis of a log-normal distribution. We have seen empirically that this type of distribution
significantly minimises the impact of extreme price swings.
Gaussian distribution
Real distribution versus Gaussian
Probability
Real distribution?
Returns
To simplify, we can say that the Black–Scholes model does not reﬂect the risk of a market
crash.
This has given rise to the notion of model risk, as almost all banks use the Black–
Scholes model (or a model derived from it). Financial research has uncovered risks that
had hitherto been ignored.
An anomaly in the options market highlights the problems of the Black–Scholes
model. When we determine the implied volatility of an underlying asset (the only fac-
tor not likely to be observed directly) based on the price of various options having the
same underlying asset, we can see that we do not find a single figure. Hence, the implied
volatility on options far out-of-the-money or far in-the-money is higher than the implied
volatility recalculated on the basis of at-the-money options. This phenomenon is called
the volatility smile (because when we draw volatility on a chart as a function of strike
price, it looks like a smile).
We will see in the following chapters the many applications of options in corporate
finance:
 t to raise financing (see Chapter 25);
 t to resolve conflicts between management and ownership or between ownership and
lenders (see Chapter 34);
~~~

## Halaman PDF 440

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=440)

~~~text
FINANCIAL SECURITIES424
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 424Trim Size: 189 X 246 mm
t to hedge risks and invest (see Chapter 50);
t to choose investments (see Chapter 30);
t to value assets (see Chapter 31);
t to value the equity of a company (see Chapter 34);
t to take over a company (see Chapter 44).
This gives you an idea of the importance of options.
The summary of this chapter can be downloaded from www.vernimmen.com.
Options are very useful ﬁnancial products to analyse complex corporate ﬁnance problems.
You will soon see that the number of ways in which they can be used continues to grow! This
is why this chapter is so important.
An option is a contract between two sides, under which one side gives the other the right
(but not the obligation) to buy from him (a call option) or sell to him (a put option) an
asset, in exchange for the payment of a premium. This asset will be bought (or sold) at a
predetermined price called the strike price, during a period of time (the exercise period for
US-style options), or at a precise date (the exercise date for European-style options). The
basis of an option is the remuneration of risk. The option cannot exist in a risk-free environ-
ment and it thrives on risk.
The value of an option (call or put) can be broken down into an intrinsic value and a time
value. The intrinsic value is the difference between the price of the underlying asset and the
option’s strike price. It can only be zero or positive. The time value is the premium on the
intrinsic value, which remunerates passing time.
There are six criteria for determining the value of an option:
t the price of the underlying asset;
t the strike price;
t the volatility of the underlying asset;
t the option’s maturity;
t the risk-free rate; and, if applicable,
t the dividend or the coupon if the underlying asset is a share or a bond that pays one or
the other during the life of the option.
Models have been developed for valuing options, the main ones being the Black–Scholes
and binomial models. They have been adapted over time to make them less restrictive and
capable of factoring in speciﬁc features.
Lastly we looked at tools for managing an options position.
SUMMARY
1/Define a call or put option.
2/What are the six criteria for determining the value of an option?
3/What does the delta of an option indicate?
QUESTIONS
~~~

## Halaman PDF 441

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=441)

~~~text
Chapter 23 OPTIONS 425
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 425Trim Size: 189 X 246 mm
4/What impact will a rise in volatility have on the value of a call option? And a drop in
interest rates? And payment of a dividend? And the extension of the maturity of an
option? And an upward revision of the strike price? And on the value of a put option?
5/Can you set the sale of a call option off against the purchase of a put option on the same
underlying asset at the same maturity?
6/How would this investor find counterparties?
7/Show how, in the end, the investor always pays too much for the option. Why is this
statement absurd?
8/Of the following four transactions, which carries the most risk?
◦ purchase of a call option;
◦ sale of a call option;
◦ purchase of a put option;
◦ sale of a put option.
  Why?
9/Time value is the anticipation of intrinsic value being stronger than it is now. However,
intrinsic value can drop. Why, then, can time value not be negative?
10/In concrete terms, what does the difficulty in valuing an option boil down to?
11/Why are options particularly well suited to arbitrage strategies? And speculation?
12/Show how the purchase of an option and the sale of another option can protect you against
the risk of a drop in the value of the underlying share, without costing you anything if
you give up the profit on a possible rise in the value of the underlying asset over a given
threshold.
13/If you hold stock options on the shares in your company, would you be pleased to see the
company paying out large dividends? Why?
14/In your view, what is the main contribution of the Black–Scholes model?
More questions are waiting for you at www.vernimmen.com.
1/The Konzerthaus in Berlin sells tickets known as Nacheinlasskarten, thirty minutes before
the start of every concert that has been sold out.
Buyers of these tickets wait at the doors giving access to the various categories of seats
in the concert hall. Thirty seconds before the concert starts, they are allowed in and can
occupy any free seat. If there are no free seats they have to leave the hall and are not
allowed to try again for a different category of seat (in any event, the co nductor has
already raised his baton). If the legitimate ticket holder for the seat arrives before the con-
cert starts, the holder of the Nacheinlasskart must give up his/her seat and leave the hall.
What is your view of this type of ticket? Be as speciﬁc as possible. Careful! This is a lot
more complicated than you probably think it is.
EXERCISES
~~~

## Halaman PDF 442

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=442)

~~~text
FINANCIAL SECURITIES426
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 426Trim Size: 189 X 246 mm
Questions
1/An option is a promise to buy for a call and to sell for a put.
2/The strike price, the value of the underlying share, volatility, the interest rate, the maturity
of the option and any dividend or coupon.
3/The hedge ratio and the probability that the option will expire in the money.
4/Rise, fall, fall, rise, fall. Rise, rise, rise, rise, rise.
5/No. The position obtained in this way would correspond to the sale, on maturity of the
option, of the underlying asset.
6/By going onto the futures market.
7/See Section 23.1.
8/Sale of a call option (unlimited losses as the potential value of the asset is unlimited). The
sale of a put option is also very risky (but the loss is limited to the value of the underlying
share minus the strike price).
9/Because, in this case, the value of the option would be lower than the intrinsic value, result-
ing automatically in arbitrage (purchase of the option, exercise of the option, sale of the
underlying share obtained).
10/Determining the volatility to be used.
11/Because, by combining them, you can reconstitute an underlying asset; as a result
of their strong leverage effect.
12/Sale of a call option with a strike price of 120, and using the price obtained on this option
to purchase a put option at, say, 100. You will then be protected against a drop below 100,
but will not benefit from a rise above 120.
13/No, not at all, as this would reduce the value of the stock options.
14/The method for calculating the value of conditional assets, which enabled the “industriali-
sation” of options.
ANSWERS
Exercises
A detailed Excel version of the solutions is available at www.vernimmen.com.
1/This is a call option at a zero strike price combined with a put option at a zero
strike price, the value of which depends on how many people arrive in time for the concert.
2/29%, $53.2.
3/$124.0, $4.5, the risk! Because a 17% rise in the value of Google’s share will lead to a
133% rise in the value of the option, and a 25% drop in the value of the share will lead to
a 92% fall in the value of the option.
2/You wish to value a call option on Google shares (which do not pay dividends) with a
strike price of $600 and a six-month duration. You do not know what volatility to factor
in. Fortunately, four-month options are listed at $30 for a strike price of $630. What is the
implicit volatility of these options? The interest rate is 3% and Google shares are trading
at $600. What is the value of this first option?
3/Redo the exercise above, assuming in the first case that Google shares rise to $700 or fall
to $450. What is the impact on the value of the option? What basic feature of the option
have you highlighted?
~~~

## Halaman PDF 443

[Lihat halaman asli](../../CoreCourseFinancialAccounting.pdf#page=443)

~~~text
Chapter 23 OPTIONS 427
SECTION 2
c23.indd 12:37:44:PM  09/05/2014 Page 427Trim Size: 189 X 246 mm
Read the articles written by the founders of option valuation:
F. Black, M. Scholes, The valuation of option contracts and a test of market efﬁciency, Journal of Finance,
27, 399–417, May 1972.
F. Black, M. Scholes, The pricing of options and corporate liabilities, Journal of Political Economy, 18,
637–654, May–June 1973.
J. Cox, S. Ross, M. Rubinstein, Option pricing: A simpliﬁed approach, Journal of Financial Economics, 7,
229–263, September 1979.
M. Garman, S. Kohlhagen, Foreign currency option values, Journal of International Money and Finance ,
December 1983.
R. Merton, Options pricing when underlying stock returns are discontinuous, Journal of Financial
Economics, 3, 125–144, January–March 1973.
R. Merton, Theory of rational option pricing, Bell Journal of Economics and Management Services , 4,
637–654, Summer 1976.
R. Roll, An analytic valuation formula for unprotected American call options on stocks with known divi-
dends, Journal of Financial Economics, 251–258, November 1977.
To ﬁnd out more about options:
J. Hull, Options, Futures and Other Derivatives, 9th edn, Prentice Hall, 2014.
J. Hull, Fundamentals of Futures and Options Markets, 8th edn, Prentice Hall, 2013.
To learn more about the mechanics of option trading:
S. Bossu, P. Henrotte, An introduction to equity derivatives, 2nd edn, Wiley, 2012.
L. McMillan, Options as a Strategic Investment, 5th edn, Prentice Hall, 2012.
L. McMillan, McMillan on Options, 2nd edn, John Wiley & Sons, Inc., 2004.
To learn more about volatility:
L. Calvet, A. Fisher, Multifractal Volatility, Theory, Forecasting, and Pricing, Academic Press, 2008.
S. Gerlach, S. Ramaswamy, M. Scatigna, 150 years of ﬁnancial markets volatility, BIS Quarterly Review,
77–91, September 2006.
J. Gatheral, The Volatility Surface, John Wiley & Sons, Inc., 2006.
For valuing stock options:
J. Hull, A. White, How to value employee stock options? Financial Analysts Journal , 1(60), 114–119,
January–February 2004.
BIBLIOGRAPHY
~~~
