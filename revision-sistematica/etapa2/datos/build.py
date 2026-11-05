import json,urllib.request,urllib.parse,time,re,csv
from collections import Counter
# parse medline
def parse_medline(txt):
    recs=[]
    for blk in txt.strip().split('\n\n'):
        d={}; key=None
        for line in blk.split('\n'):
            if len(line)>4 and line[4]=='-' :
                key=line[:4].strip(); val=line[6:]
                d.setdefault(key,[]).append(val)
            elif key: d[key][-1]+=' '+line.strip()
        if 'PMID' in d: recs.append(d)
    return recs
def norm(d):
    g=lambda k:' '.join(d.get(k,[]))
    doi=next((x.replace(' [doi]','') for x in d.get('AID',[]) if x.endswith('[doi]')),'')
    return {'id':'PMID:'+g('PMID'),'pmid':g('PMID'),'doi':doi,'title':g('TI'),'abstract':g('AB'),'year':g('DP')[:4],'journal':g('JT'),'authors':'; '.join(d.get('AU',[])),'pubtype':'; '.join(d.get('PT',[])),'language':'; '.join(d.get('LA',[])),'mesh':'; '.join(d.get('MH',[]))}
pm=[norm(d) for d in parse_medline(open('pubmed_v2.medline').read())]
for r in pm: r['source']='PubMed'
uniq=json.load(open('epmc_unique.json'))
pmids=[r['pmid'] for r in uniq if r.get('pmid')]
txt=''
for i in range(0,len(pmids),200):
    d=urllib.parse.urlencode({'db':'pubmed','id':','.join(pmids[i:i+200]),'rettype':'medline','retmode':'text'}).encode()
    txt+=urllib.request.urlopen('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi',d).read().decode()+'\n\n'
ep=[norm(d) for d in parse_medline(txt)]
for r in ep: r['source']='Europe PMC'
for r in uniq:
    if r.get('pmid'): continue
    u='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':f'EXT_ID:{r["id"]} AND SRC:{r["source"]}','format':'json','resultType':'core'})
    c=json.load(urllib.request.urlopen(u,timeout=60))['resultList']['result'][0]
    ep.append({'id':f'{r["source"]}:{r["id"]}','pmid':'','doi':c.get('doi',''),'title':c.get('title',''),'abstract':re.sub('<[^>]+>','',c.get('abstractText','') or ''),'year':c.get('pubYear',''),'journal':((c.get('journalInfo') or {}).get('journal') or {}).get('title','') or c.get('bookOrReportDetails',{}).get('publisher',''),'authors':c.get('authorString',''),'pubtype':'; '.join((c.get('pubTypeList') or {}).get('pubType',[])),'language':c.get('language',''),'mesh':'','source':'Europe PMC ('+r['source']+')'}); time.sleep(0.2)
allr=pm+ep
print('pubmed',len(pm),'epmc unique by PMID',len(ep))
# dedupe by DOI and normalized title
nt=lambda t:re.sub(r'[^a-z0-9]','',t.lower())[:120]
seen={}; final=[]; dups=[]
for r in allr:
    keys=[k for k in [('doi',r['doi'].lower()) if r['doi'] else None,('t',nt(r['title'])+r['year'])] if k]
    hit=next((seen[k] for k in keys if k in seen),None)
    if hit: dups.append((r['id'],hit)); continue
    for k in keys: seen[k]=r['id']
    final.append(r)
print('dups by doi/title',len(dups),dups)
json.dump(final,open('registros_cribado.json','w'),ensure_ascii=False)
print('final',len(final),Counter(r['source'] for r in final))
print('no abstract',sum(1 for r in final if not r['abstract']))
print('years',min(r['year'] for r in final if r['year']),max(r['year'] for r in final))
print(Counter(r['language'] for r in final).most_common(8))
