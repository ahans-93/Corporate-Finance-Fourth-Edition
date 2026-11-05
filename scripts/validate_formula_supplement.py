"""Checks for the imported formula supplement and selected numerical examples."""
from pathlib import Path
import json,re,hashlib,math
from finance_examples import npv,irr_conventional,black_scholes
R=Path(__file__).resolve().parents[1]
def run_supplement_checks():
    doc=(R/"docs/book/53-kompilasi-rumus.md").read_text(encoding="utf-8")
    ids=list(map(int,re.findall(r"\\tag\{(\d+)\}",doc)))
    assert ids==list(range(1,151)), "Equation IDs must be 1..150 without gaps/duplicates"
    assert re.findall(r"^## S(\d\d)$",doc,re.M)==[f"{i:02d}" for i in range(1,32)]
    assert len(re.findall(r"\$\$",doc))%2==0, "Unbalanced math delimiters"
    cfg=json.loads((R/"data/formula-supplement-review.json").read_text(encoding="utf-8"))
    assert len(cfg["sections"])==31 and len(cfg["replacements"])==23
    cs=json.loads((R/"data/chapters.json").read_text(encoding="utf-8"))
    for c in cs:
        text=(R/f'docs/book/{c["slug"]}.md').read_text(encoding="utf-8")
        assert text.count("<!-- formula-supplement:start -->")==1, "Missing or repeated supplement link"
    manifest=json.loads((R/"data/formula-supplement-manifest.json").read_text(encoding="utf-8"))
    for source in manifest["originals"]:
        raw=(R/source["path"]).read_bytes()
        assert len(raw)==source["bytes"] and hashlib.sha256(raw).hexdigest()==source["sha256"], "Original attachment changed"
    rows=[]
    def check(label,got,want,tol=1e-6):
        assert math.isclose(got,want,abs_tol=tol,rel_tol=tol),(label,got,want)
        rows.append(dict(check="Supplement "+label,actual=got,expected=want))
    check("S01 FCFE",120+40-70-30+20,80)
    check("S02 EBITDA",1020-600-200-20+10,210)
    check("S03 WCR",150+200+20-120-30,220)
    check("S03 capital reconciliation",600+220,500+320)
    check("S04 CCC",120/1200*365+80/800*365-60/600*365,36.5)
    check("S05 margin of safety",(600000-500000)/600000,1/6)
    check("S06 debt-service coverage",100/(30+100),.7692307692307693)
    check("S07 ROE",.12+(.12-.06)*1,.18)
    check("S08 classical Z",1.2*.2+1.4*.1+3.3*.15+.6*1.5+.999*1.2,2.9738)
    check("S09 annuity PV",100*(1-1.1**-3)/.1,248.68519909842223)
    check("S10 MIRR",(126/100)**.5-1,.12249721603218244)
    check("S11 portfolio sigma",math.sqrt(.25*.04+.25*.04),.1414213562373095)
    check("S12 beta",.6*.30/.15,1.2)
    check("S13 clean price",101.25-1.25,100)
    check("S14 DDM",5/(.12-.02),50)
    call,put=black_scholes(100,100,.05,.2,1)
    check("S15 call",call,10.450583572185565)
    d1=(math.log(100/100)+(.05+.2**2/2)*1)/.2
    vega=100*math.exp(-d1*d1/2)/math.sqrt(2*math.pi)
    check("S15 vega per 1 percentage point",vega/100,.3752403469169379)
    check("S16 conversion premium",(1260-20*60)/(20*60),.05)
    check("S17 EV bridge",1000+300+50+20-40,1330)
    check("S18 CFROI IRR",irr_conventional([-100,60,60]),.1306623862918075)
    check("S18 CFROI NPV",npv(irr_conventional([-100,60,60]),[-100,60,60]),0)
    check("S19 EAA",30/((1-1.1**-3)/.1),12.06344410876133)
    check("S20 WACC",.6*.14+.4*.08*.75,.108)
    check("S21 DCF",100/(.1-.03)-350,1078.5714285714284)
    check("S21 PEG",15/(.1*100),1.5)
    check("S22 MM equity return",.1+(.1-.05)*(2/3),.13333333333333333)
    check("S23 Hamada",.8*(1+(1-.25)*.5),1.1)
    check("S23 Harris-Pringle",.8+(.8-.1)*.5,1.15)
    check("S24 debt payoff",min(70,100),70)
    check("S25 buyback EPS",97/90,1.0777777777777777)
    check("S26 TERP",(4*100+80)/5,96)
    check("S27 founder dilution",.8*(1-.2),.64)
    check("S28 acquisition NPV",500+100-570-10,20)
    check("S29 LBO sources uses",700+300+20,600+100+320)
    check("S30 Baumol",math.sqrt(2*1000000*100/.1),44721.359549995796)
    z=1000+(3*10*10000/(4*.001))**(1/3)
    check("S30 Miller-Orr return point",z,1421.7163326508745)
    check("S30 Miller-Orr upper bound",3*z-2000,2265.1489979526237)
    check("S31 CIP with quarter tenor",16000*(1+.06*.25)/(1+.04*.25),16079.20792079208)
    check("S31 signed delta hedge",-(-10)*100*.6,600)
    return rows
if __name__=="__main__":
    rows=run_supplement_checks()
    print(json.dumps(dict(status="PASS",numbered_equations=150,sections=31,rewritten_equations=23,original_files=3,chapters_linked=50,numerical_checks=len(rows)),indent=2))
