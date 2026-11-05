import json,urllib.request,urllib.parse,time
B1='(TITLE_ABS:"acute leukemia" OR TITLE_ABS:"acute leukaemia" OR TITLE_ABS:"acute leukemias" OR TITLE_ABS:"acute myeloid leukemia" OR TITLE_ABS:"acute myeloid leukaemia" OR TITLE_ABS:"acute myelogenous leukemia" OR TITLE_ABS:"acute lymphoblastic leukemia" OR TITLE_ABS:"acute lymphoblastic leukaemia" OR TITLE_ABS:"acute lymphocytic leukemia" OR TITLE_ABS:"acute promyelocytic leukemia" OR TITLE_ABS:"acute nonlymphocytic leukemia")'
B2='(TITLE_ABS:"complete blood count" OR TITLE_ABS:"full blood count" OR TITLE_ABS:"blood count" OR TITLE_ABS:"blood counts" OR TITLE_ABS:CBC OR TITLE_ABS:hemogram* OR TITLE_ABS:haemogram* OR TITLE_ABS:"hematological parameters" OR TITLE_ABS:"haematological parameters" OR TITLE_ABS:"peripheral blood smear" OR TITLE_ABS:"peripheral blood film" OR TITLE_ABS:"blood film" OR TITLE_ABS:"blood smear" OR TITLE_ABS:"peripheral smear" OR TITLE_ABS:"circulating blasts" OR TITLE_ABS:"peripheral blood blasts" OR TITLE_ABS:"blast flag" OR TITLE_ABS:"blast flags" OR TITLE_ABS:"hematology analyzer" OR TITLE_ABS:"haematology analyser")'
B3='(TITLE_ABS:"presenting features" OR TITLE_ABS:"presenting signs" OR TITLE_ABS:"presenting symptoms" OR TITLE_ABS:"clinical presentation" OR TITLE_ABS:"initial presentation" OR TITLE_ABS:"at presentation" OR TITLE_ABS:"at diagnosis" OR TITLE_ABS:"early diagnosis" OR TITLE_ABS:"diagnostic accuracy" OR TITLE_ABS:sensitivity OR TITLE_ABS:specificity OR TITLE_ABS:"predictive value" OR TITLE_ABS:"primary care" OR TITLE_ABS:"general practice" OR TITLE_ABS:suspicion OR TITLE_ABS:pancytopeni* OR TITLE_ABS:cytopeni* OR TITLE_ABS:aleuk* OR TITLE_ABS:subleuk* OR TITLE_ABS:"clinical features" OR TITLE_ABS:"hematological features" OR TITLE_ABS:"haematological features" OR TITLE_ABS:"hematological findings" OR TITLE_ABS:"haematological findings" OR TITLE_ABS:"hematological abnormalities" OR TITLE_ABS:"laboratory findings" OR TITLE_ABS:"laboratory features" OR TITLE_ABS:"diagnostic delay" OR TITLE_ABS:characteristic* OR TITLE_ABS:profile* OR TITLE_ABS:morpholog* OR TITLE_ABS:epidemiolog*)'
Q=f'{B1} AND {B2} AND {B3}'
open('epmc_q.txt','w').write(Q)
base='https://www.ebi.ac.uk/europepmc/webservices/rest/search'
cur='*'; recs=[]
while True:
    u=base+'?'+urllib.parse.urlencode({'query':Q,'format':'json','pageSize':1000,'cursorMark':cur,'resultType':'lite'})
    j=json.load(urllib.request.urlopen(u,timeout=90))
    if not recs: print('hitCount',j['hitCount'],flush=True)
    rl=j['resultList']['result']; recs+=rl; print(len(recs),flush=True)
    if not rl or j.get('nextCursorMark')==cur: break
    cur=j['nextCursorMark']; time.sleep(0.3)
json.dump(recs,open('epmc_lite.json','w'))
pm=set(open('pubmed_v2_pmids.txt').read().split())
from collections import Counter
print(len(recs),Counter(r['source'] for r in recs))
nop=[r for r in recs if not r.get('pmid') or r['pmid'] not in pm]
print('not in PubMed set',len(nop),Counter(r['source'] for r in nop)); print('with pmid',sum(1 for r in nop if r.get('pmid')))
json.dump(nop,open('epmc_unique.json','w'))
