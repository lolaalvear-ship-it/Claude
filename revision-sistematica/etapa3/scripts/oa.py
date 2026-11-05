import json,urllib.request,urllib.parse,time
sl={x['n']:x for x in json.load(open('shortlist.json'))}
dec=json.load(open('abs_decisions.json'))
todo=[sl[int(n)] for n,v in dec.items() if v[0] in ('I','A','S')]
out={}
for x in todo:
    q=f"EXT_ID:{x['pmid']} AND SRC:MED" if x['pmid'] else f"EXT_ID:{x['id'].split(':')[1]}"
    u='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':q,'format':'json','resultType':'core'})
    try:
        r=json.load(urllib.request.urlopen(u,timeout=60))['resultList']['result']
        r=r[0] if r else {}
    except Exception as e: r={'err':str(e)}
    out[x['n']]={'pmcid':r.get('pmcid'),'oa':r.get('isOpenAccess'),'inPMC':r.get('inPMC'),'inEPMC':r.get('inEPMC'),'hasPDF':r.get('hasPDF'),'doi':r.get('doi'),
      'urls':[f.get('url') for f in (r.get('fullTextUrlList') or {}).get('fullTextUrl',[]) if f.get('availabilityCode') in ('OA','F','FREE')],'affil':(r.get('affiliation') or '')[:200]}
    time.sleep(0.15)
json.dump(out,open('oa.json','w'),indent=0)
from collections import Counter
print(len(out),Counter((v['inEPMC'],v['oa']) for v in out.values()))
print('with free url',sum(1 for v in out.values() if v['urls']))
