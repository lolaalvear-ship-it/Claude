import json,re,html,sys
from xml.etree import ElementTree as ET
dec=json.load(open('abs_decisions.json')); res=json.load(open('ftres.json'))
sl={str(x['n']):x for x in json.load(open('shortlist.json'))}
def txt(e): return re.sub(r'\s+',' ',''.join(e.itertext())).strip() if e is not None else ''
KW=re.compile(r'(an(a)?emi|thrombocytop|leuk(o)?cyt|leucocyt|neutrop|pancytop|blast|smear|film|haemoglobin|hemoglobin|platelet|sensitiv|specific|flag|WBC|normal (blood|CBC|count)|Auer|predictive|AUC|kappa|agreement)',re.I)
out=[]
for n,r in res.items():
    if r!='ok' or dec[n][0]!='I': continue
    s=open(f'ft/{n}.xml').read()
    s=re.sub(r'<!DOCTYPE[^>]*>','',s)
    try: root=ET.fromstring(s)
    except Exception as e:
        out.append(f"## {n} PARSE_ERR"); continue
    body=root.find('.//body')
    secs=body.findall('.//sec') if body is not None else []
    meth=' '.join(txt(x) for x in secs if re.search(r'method|patient|material|design',txt(x.find('title')) if x.find('title') is not None else '',re.I))[:1300]
    restxt=' '.join(txt(x) for x in secs if re.search(r'result',txt(x.find('title')) if x.find('title') is not None else '',re.I))
    if not restxt: restxt=txt(body)
    sents=[z for z in re.split(r'(?<=[.;])\s+',restxt) if KW.search(z) and re.search(r'\d',z)]
    tabs=' | '.join(txt(t.find('caption')) for t in root.findall('.//table-wrap') if t.find('caption') is not None)[:300]
    out.append(f"## {n} | {sl[n]['year']} | {sl[n]['title'][:110]}\nMET: {meth}\nRES: {' '.join(sents)[:1500]}\nTAB: {tabs}")
open('ftsum.txt','w').write('\n'.join(out)); print(len(out))
