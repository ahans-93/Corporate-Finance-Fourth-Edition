"""Independent numerical checks for selected companion examples.
No network or credentials are required. Values are illustrative, not advice.
"""
import json, math
def npv(rate, flows):
    if rate <= -1: raise ValueError("rate must exceed -100%")
    return sum(cf/(1+rate)**t for t,cf in enumerate(flows))
def irr_conventional(flows, low=0.0, high=1.0):
    if flows[0]>=0 or any(x<0 for x in flows[1:]):
        raise ValueError("This solver only supports one initial outflow and nonnegative subsequent flows")
    if npv(low,flows)*npv(high,flows)>0:
        raise ValueError("Root not bracketed")
    for _ in range(150):
        mid=(low+high)/2
        if npv(mid,flows)>0: low=mid
        else: high=mid
    return (low+high)/2
def bond_price(face,coupon,y,years):
    return sum(coupon/(1+y)**t for t in range(1,years+1))+face/(1+y)**years
def normal_cdf(x): return .5*(1+math.erf(x/math.sqrt(2)))
def black_scholes(s,k,r,sigma,t):
    d1=(math.log(s/k)+(r+sigma*sigma/2)*t)/(sigma*math.sqrt(t))
    d2=d1-sigma*math.sqrt(t)
    call=s*normal_cdf(d1)-k*math.exp(-r*t)*normal_cdf(d2)
    put=k*math.exp(-r*t)*normal_cdf(-d2)-s*normal_cdf(-d1)
    return call,put
def run_checks():
    rows=[]
    def check(label,actual,expected,tol=1e-7):
        if not math.isclose(actual,expected,rel_tol=tol,abs_tol=tol):
            raise AssertionError(f"{label}: got {actual}, expected {expected}")
        rows.append(dict(check=label,actual=actual,expected=expected))
    check("01 PV of single claim",110/1.10,100)
    check("02 Cash movement",500-380-150+50-10,10)
    check("03 Net income",(1000-700-80-20)*.75,150)
    check("04 Capital employed",600+150+200-120,830)
    check("05 FCFF",200*.75+40-70-30,90)
    check("06 NCI",100*.20,20)
    check("08 CAGR",(121/100)**.5-1,.10)
    check("09 Price-volume growth",1.10*.95-1,.045)
    check("10 Break-even units",200000/(100-60),5000)
    check("10 DOL",240000/40000,6)
    check("11 DSO",120/1200*365,36.5)
    check("12 DSCR",100/(30+100),.7692307692307693)
    check("13 ROE positive spread",.12+(.12-.06)*1,.18)
    check("13 ROE negative spread",.04+(.04-.06)*1,.02)
    check("14 Economic profit",100-.12*1000,-20)
    check("15 Holding return",(106-100+4)/100,.10)
    check("16 NPV at 10%",npv(.10,[-100,60,60]),4.132231404958674)
    check("16 NPV at 15%",npv(.15,[-100,60,60]),-2.45746691871455)
    check("17 Conventional IRR",irr_conventional([-100,0,121]),.10)
    check("17 Effective annual rate",1.01**12-1,.12682503013196977)
    check("17 Multiple IRR first root",npv(.10,[-100,230,-132]),0)
    check("17 Multiple IRR second root",npv(.20,[-100,230,-132]),0)
    check("18 Diversified volatility",math.sqrt(.5**2*.2**2+.5**2*.2**2),.1414213562373095)
    check("19 CAPM",.04+1.2*.06,.112)
    check("19 Forward rate",1.05**2/1.04-1,.06009615384615384)
    price=bond_price(100,5,.06,2)
    check("20 Bond price",price,98.16660733357066)
    mac=(5/1.06+2*105/1.06**2)/price
    check("20 Macaulay duration",mac,1.951950271996858,1e-6)
    check("21 Factoring annualized simple cost",(3/97)*365/60,.1881443298969072)
    check("22 P/E",30/(100/50),15)
    check("23 Call profit",max(120-100,0)-8,12)
    check("24 Conversion value",20*60,1200)
    check("25 TERP",(4*100+80)/5,96)
    check("25 Right value",100-96,4)
    check("26 Perpetual NPV",12/.10-100,20)
    check("27 EVA",150-.12*1000,30)
    check("28 Investment NPV",npv(.10,[-120,42.5,62.5]),-29.710743801652896)
    check("29 WACC",.6*.14+.4*.08*.75,.108)
    check("30 Value of contingent investment",.5*max(140-90,0)+.5*max(60-90,0),25)
    check("31 Enterprise value",100/(.10-.03),1428.5714285714284)
    ke=.10+(.10-.05)*400/600
    check("32 Levered equity cost",ke,.13333333333333333)
    check("32 MM WACC",.6*ke+.4*.05,.10)
    check("33 PV tax shield",100*.06*.25/.06,25)
    check("34 Default equity payoff",max(70-100,0),0)
    check("35 Liquidity headroom",50+80-110,20)
    check("36 Retained growth",.15*(1-.40),.09)
    check("37 Buyback EPS",97/90,1.0777777777777777)
    check("38 Ownership after issuance",10/125,.08)
    check("39 Quarterly interest",100*.07*90/360,1.75)
    check("40 Runway",600/100,6)
    check("40 Post-money ownership",2/(8+2),.20)
    check("41 Indirect economic ownership",.6*.7,.42)
    check("42 Primary proceeds",10_000_000*1000,10_000_000_000)
    check("44 Acquisition buyer NPV",500+100-570-10,20)
    check("45 Combined EPS",125/120,1.0416666666666667)
    check("46 LBO MOIC",700/400,1.75)
    check("46 LBO IRR",1.75**.2-1,.118426914720144,1e-6)
    check("47 Junior recovery",(80-60)/40,.50)
    check("48 Working-capital cash release",3650/365*5,50)
    check("49 Required draw",20-(100+80-210),50)
    check("50 Locked IDR",100000*16000,1600000000)
    check("Advanced annuity",100*(1-1.1**-3)/.1,248.68519909842223)
    check("Advanced real rate",1.10/1.04-1,.05769230769230771)
    call,put=black_scholes(100,100,.05,.2,1)
    check("Advanced Black-Scholes call",call,10.450583572185565)
    check("Advanced Black-Scholes put",put,5.573526022256971)
    check("Advanced put-call parity",call-put,100-100*math.exp(-.05))
    check("Advanced terminal FCFF",120*(1-.03/.15),96)
    check("Advanced supplier discount cost",.02/.98*365/20,.37244897959183676)
    fcf=[102.5,122.5,154.5]
    k=.108; tv=144.612/(k-.03)
    ev=npv(k,[0]+fcf)+tv/(1+k)**3
    check("Integrated terminal value",tv,1854)
    check("Integrated EV",ev,1668.8569769651572)
    check("Integrated equity value",ev-200,1468.8569769651572)
    check("Integrated ROE beginning capital",100.5/400,.25125)
    check("Integrated DSCR",102.5/56,1.8303571428571428)
    stress=npv(.128,[0]+fcf)+(144.612/(.128-.03))/(1.128)**3
    check("Integrated WACC sensitivity",stress,1322.92850367852)
    return rows
if __name__=="__main__":
    result=run_checks()
    print(json.dumps(dict(status="PASS",numerical_checks=len(result),results=result),indent=2))
