import json,urllib.request,urllib.parse,time
q=json.load(open('pubmed_q.json'))
def es(t):
    u='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
    d=urllib.parse.urlencode({'db':'pubmed','term':t,'retmode':'json','retmax':10000}).encode()
    r=json.load(urllib.request.urlopen(u,d))['esearchresult']; return r
r=es(q['FINAL']); ids=r['idlist']; print(len(ids), r['count']); print(r.get('querytranslation','')[:3000])
open('pubmed_final_pmids.txt','w').write('\n'.join(ids))
r2=es(q['B1+B2']+' NOT (animals[mh] NOT humans[mh])'); ids2=r2['idlist']; print('B1B2',len(ids2))
open('pubmed_b1b2_pmids.txt','w').write('\n'.join(ids2))
out=open('pubmed_final.medline','w')
for i in range(0,len(ids),200):
    d=urllib.parse.urlencode({'db':'pubmed','id':','.join(ids[i:i+200]),'rettype':'medline','retmode':'text'}).encode()
    out.write(urllib.request.urlopen('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi',d).read().decode()); time.sleep(0.4)
