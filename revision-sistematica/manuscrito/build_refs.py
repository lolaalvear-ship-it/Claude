import re,json,urllib.request,urllib.parse,sys
src=open('borrador_con_claves.md').read()
order=[]
for m in re.finditer(r'\[\[([\d,]+)\]\]',src):
    for p in m.group(1).split(','):
        if p not in order: order.append(p)
d=urllib.parse.urlencode({'db':'pubmed','id':','.join(order),'rettype':'medline','retmode':'text'}).encode()
txt=urllib.request.urlopen('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi',d).read().decode()
recs={}
for blk in txt.strip().split('\n\n'):
    r={};k=None
    for line in blk.split('\n'):
        if len(line)>4 and line[4]=='-': k=line[:4].strip(); r.setdefault(k,[]).append(line[6:])
        elif k: r[k][-1]+=' '+line.strip()
    if 'PMID' in r: recs[r['PMID'][0]]=r
def vanc(p):
    r=recs[p]; au=r.get('AU',[]) or r.get('CN',[])
    a=', '.join(au[:6])+(', et al' if len(au)>6 else '')
    ti=re.sub(r'\s+',' ',r['TI'][0]).rstrip('.'); ta=r.get('TA',[''])[0]; dp=r.get('DP',[''])[0][:4]
    vi=r.get('VI',[''])[0]; ip=r.get('IP',[''])[0]; pg=r.get('PG',[''])[0]
    doi=next((x.replace(' [doi]','') for x in r.get('AID',[]) if x.endswith('[doi]')),'')
    loc=f"{dp}" + (f";{vi}" if vi else '') + (f"({ip})" if ip else '') + (f":{pg}" if pg else '')
    if not vi and not pg: loc=f"{dp}. Epub ahead of print"
    return f"{a}. {ti}. {ta}. {loc}." + (f" doi:{doi}." if doi else '') + f" PMID: {p}."
num={p:i+1 for i,p in enumerate(order)}
def compress(ns):
    ns=sorted(set(ns)); out=[]; i=0
    while i<len(ns):
        j=i
        while j+1<len(ns) and ns[j+1]==ns[j]+1: j+=1
        out.append(f"{ns[i]}" if i==j else (f"{ns[i]},{ns[j]}" if j==i+1 else f"{ns[i]}-{ns[j]}")); i=j+1
    return ','.join(out)
out=re.sub(r'\[\[([\d,]+)\]\]',lambda m:'['+compress([num[p] for p in m.group(1).split(',')])+']',src)
refs='\n'.join(f"{num[p]}. {vanc(p)}" for p in order)
out=out.replace('{{REFERENCIAS}}',refs)
open('manuscrito_revision_sistematica.md','w').write(out)
json.dump({p:num[p] for p in order},open('mapa_referencias.json','w'),indent=0)
missing=[p for p in order if p not in recs]; print(len(order),'refs; missing',missing)
