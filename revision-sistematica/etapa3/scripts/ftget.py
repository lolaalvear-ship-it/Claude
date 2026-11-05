import json,urllib.request,urllib.parse,time,os
oa=json.load(open('oa.json')); dec=json.load(open('abs_decisions.json'))
res={}
for n,v in oa.items():
    if not v['pmcid']: continue
    p=v['pmcid']; fn=f'ft/{n}.xml'
    if os.path.exists(fn) and os.path.getsize(fn)>2000: res[n]='ok'; continue
    txt=''
    try: txt=urllib.request.urlopen(f'https://www.ebi.ac.uk/europepmc/webservices/rest/{p}/fullTextXML',timeout=60).read().decode()
    except Exception as e: pass
    if '<body' not in txt:
        try:
            d=urllib.parse.urlencode({'db':'pmc','id':p.replace('PMC',''),'retmode':'xml'}).encode()
            txt=urllib.request.urlopen('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi',d,timeout=60).read().decode()
        except Exception as e: txt=''
    open(fn,'w').write(txt); res[n]='ok' if '<body' in txt else 'nobody'
    time.sleep(0.3)
json.dump(res,open('ftres.json','w'))
from collections import Counter
print(Counter(res.values()), Counter((dec[n][0],r) for n,r in res.items()))
