"""Genera la clave de respuestas (Word) del ejercicio de 50 biometrías simuladas."""
import csv
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

R=list(csv.DictReader(open("base_50_biometrias_completa.csv",encoding="utf-8-sig")))
for r in R:
    for k in ["Edad","Hb","VCM","Leucocitos","Neut_pct","Linf_pct","Mono_pct","Eos_pct","Blastos_pct","Otras_pct","Neut_abs","Plaquetas"]:
        r[k]=float(r[k])
LA=lambda r:r["Es_LA"]=="Sí"
def inmaduras_ec(r):  # blastos o promielocitos anómalos en SP
    return r["Blastos_pct"]>0 or "Promielocitos anómalos" in r["Frotis"]
def fmt(x): return (f"{x:g}").replace(".",",")

def linaje(r):
    d=r["Diagnostico"]
    if not LA(r): return "No aplica (no es leucemia aguda)."
    if not inmaduras_ec(r): return "No es posible orientar el linaje: no hay blastos en sangre periférica. Se define en médula ósea con citometría de flujo."
    if d.startswith("LLA-T"): return "Linfoide T. Apoyan: blastos de aspecto linfoide con núcleo irregular y masa mediastínica. Limitación: la morfología sola falla en ~1 de cada 10 casos; lo confirma la citometría (CD3 citoplasmático, CD7)."
    if d.startswith("LLA"): return "Linfoide. Apoyan: blastos pequeños-medianos con relación N/C alta, cromatina fina y nucléolos poco evidentes, sin gránulos ni bastones de Auer. Limitación: la morfología no es definitiva; lo confirma la citometría (CD19, CD10, TdT)."
    if d.startswith("LPA"): return "Mieloide, promielocítica. Apoyan: promielocitos anómalos" + (" microgranulares de núcleo bilobulado (pueden imitar monocitos)" if "micro" in d else ", bastones de Auer en haces") + ". Se confirma con PML::RARA."
    if "fenotipo mixto" in d: return "No se puede asignar por morfología: blastos heterogéneos. Solo la citometría demuestra marcadores de dos linajes (B y mieloide)."
    if "M5" in d: return "Mieloide, monocítica. Apoyan: monoblastos y promonocitos de núcleo plegado, monocitosis e hipertrofia gingival."
    extra=" y bastones de Auer" if "Auer" in r["Frotis"] else ""
    return f"Mieloide. Apoyan: mieloblastos{extra}" + (", con displasia asociada" if "displasia" in r["Frotis"] else "") + ". Limitación: si no hay bastones de Auer, la morfología no basta; lo confirma la citometría (MPO, CD13, CD33, CD117)."

def sospecha(r):
    d=r["Diagnostico"]; a=r["Alteraciones_BH"]
    if LA(r):
        if d.startswith("LPA"): return "SÍ, URGENCIA INMEDIATA: hay sospecha de LPA con riesgo de CID y hemorragia. Se pide coagulación (fibrinógeno, TP, dímero D) y se inicia ATRA ante la sospecha, sin esperar la genética."
        if r["Leucocitos"]>100: return "SÍ, URGENTE: hiperleucocitosis con riesgo de leucostasis y lisis tumoral. Requiere derivación inmediata a hematología."
        if not inmaduras_ec(r): return "SÍ. El frotis no muestra blastos, pero la clínica y las citopenias (o el dolor óseo persistente) justifican sospechar LA. Un frotis sin blastos NO la descarta, así que hay que derivar y valorar la médula ósea."
        return "SÍ, con prioridad: hay blastos circulantes junto con citopenias. Derivar el mismo día a hematología."
    if "PANCITOPENIA" in a or r["Blastos_pct"]>0 or r["Leucocitos"]>100:
        return "La LA debe DESCARTARSE: " + ("hay pancitopenia" if "PANCITOPENIA" in a else "hay blastos o leucocitosis extrema") + ". El frotis y el resto de datos orientan a otra causa, pero hay que estudiar la médula o hacer pruebas específicas."
    return "NO. El patrón de la BH y del frotis no sugiere LA; hay una explicación alternativa clara. Basta con vigilar la evolución."

def diferencial(r):
    if LA(r): return "No aplica: es leucemia aguda. Diferenciales a considerar: " + ("AIJ y otras causas de dolor osteoarticular" if "dolor" in r["Cuadro_clinico"].lower() and r["Edad"]<15 else "anemia aplásica, anemia megaloblástica, SMD e infecciones con citopenias" if "PANCITOPENIA" in r["Alteraciones_BH"] else "reacción leucemoide, infección y leucemias crónicas" if r["Leucocitos"]>11 else "otras causas de citopenias") + "."
    return f"{r['Diagnostico']}. {r['Razonamiento']}"

doc=Document()
st=doc.styles["Normal"]; st.font.name="Calibri"; st.font.size=Pt(10.5)
for s in doc.sections: s.left_margin=s.right_margin=Cm(2)
doc.add_heading("Clave de respuestas: ejercicio de 50 biometrías hemáticas",0)
p=doc.add_paragraph(); run=p.add_run("Material docente. Pacientes, nombres y valores FICTICIOS, construidos con los patrones de los 38 artículos de la revisión sistemática. No corresponden a personas reales."); run.bold=True; run.font.color.rgb=RGBColor(0xC0,0,0)

doc.add_heading("1. Cómo calificar",1)
doc.add_paragraph("Cada paciente vale 6 puntos (1 por pregunta), así que los 50 pacientes suman 300 puntos. Las 6 preguntas de síntesis (A–F) valen 5 puntos cada una, 30 en total. El total es de 330 puntos.")
doc.add_paragraph("Nota sobre 10 = puntos obtenidos ÷ 33. Se sugiere aprobar con 6,0 (198 puntos).")
t=doc.add_table(rows=1,cols=3); t.style="Light Grid Accent 1"
h=t.rows[0].cells; h[0].text="Pregunta"; h[1].text="1 punto (completa)"; h[2].text="0,5 puntos (parcial)"
for q,cc,pa in [
 ("1. Alteraciones de la BH","Identifica todas las alteraciones de la clave (anemia, leucopenia o leucocitosis, trombocitopenia, neutropenia, pancitopenia)","Omite una alteración o no nombra la pancitopenia"),
 ("2. Hallazgo del frotis","Señala el hallazgo clave (blastos, promielocitos anómalos, bastones de Auer, células reactivas, hipersegmentación…) o reconoce que el frotis no tiene blastos","Lo describe de forma vaga («células raras»)"),
 ("3. ¿Sospecha de LA?","Responde correctamente sí o no Y la urgencia (LPA e hiperleucocitosis son urgencias)","Acierta en sí o no, pero sin la urgencia o sin justificarlo"),
 ("4. Linaje","Orienta bien el linaje con un dato de apoyo Y menciona que se confirma con citometría (o dice «no aplica» o «no es posible» cuando corresponde)","Acierta el linaje sin dato de apoyo"),
 ("5. Diferencial","Da el diagnóstico (o el diferencial principal) con el dato que lo distingue","Diagnóstico aproximado (por ejemplo, «una infección» en lugar de mononucleosis)"),
 ("6. Confirmación","Nombra el estudio confirmatorio correcto","Pide un estudio útil pero incompleto (por ejemplo, médula ósea sin citometría)")]:
    c=t.add_row().cells; c[0].text=q; c[1].text=cc; c[2].text=pa
doc.add_paragraph("Errores graves que anulan la pregunta 3: no reconocer como urgencia una LPA, o afirmar que un frotis sin blastos descarta la leucemia aguda.")

doc.add_heading("2. Resumen de diagnósticos",1)
t=doc.add_table(rows=1,cols=5); t.style="Light Grid Accent 1"
for j,x in enumerate(["ID","Nombre (ficticio)","Edad/sexo","¿LA?","Diagnóstico confirmado"]): t.rows[0].cells[j].text=x
for r in R:
    c=t.add_row().cells; c[0].text=r["ID"]; c[1].text=r["Nombre"]; c[2].text=f"{fmt(r['Edad'])} a / {r['Sexo']}"; c[3].text=r["Es_LA"]; c[4].text=r["Diagnostico"]

doc.add_heading("3. Respuestas resueltas por paciente",1)
for r in R:
    doc.add_heading(f"{r['ID']} · {r['Nombre']} · {fmt(r['Edad'])} años, {r['Sexo']} · {'LEUCEMIA AGUDA' if LA(r) else 'NO es leucemia aguda'}",2)
    doc.add_paragraph(f"Cuadro: {r['Cuadro_clinico']}.").italic=True
    doc.add_paragraph(f"BH: Hb {fmt(r['Hb'])} g/dL · VCM {fmt(r['VCM'])} fL · Leucocitos {fmt(r['Leucocitos'])}×10⁹/L (N {fmt(r['Neut_pct'])} %, L {fmt(r['Linf_pct'])} %, M {fmt(r['Mono_pct'])} %, blastos {fmt(r['Blastos_pct'])} %, otras {fmt(r['Otras_pct'])} %) · Neutrófilos absolutos {fmt(r['Neut_abs'])}×10⁹/L · Plaquetas {fmt(r['Plaquetas'])}×10⁹/L")
    for n,txt in [
        ("1. Alteraciones de la BH", r["Alteraciones_BH"].capitalize()+"."),
        ("2. Hallazgo clave del frotis", r["Frotis"]+"."),
        ("3. ¿Sospecha de LA?", sospecha(r)),
        ("4. Linaje", linaje(r)),
        ("5. Diagnóstico / diferencial", diferencial(r)),
        ("6. Confirmación", r["Confirmacion"]+"."),
    ]:
        p=doc.add_paragraph(style="List Bullet"); a=p.add_run(n+": "); a.bold=True; p.add_run(txt)
    if LA(r):
        p=doc.add_paragraph(); a=p.add_run("Comentario docente: "); a.bold=True; p.add_run(r["Razonamiento"])
    p=doc.add_paragraph(); a=p.add_run(f"Evidencia (n.º de ficha de la revisión): {r['Articulos']}"); a.font.size=Pt(9); a.font.color.rgb=RGBColor(0x59,0x59,0x59)

# ----- síntesis -----
doc.add_heading("4. Respuestas a las preguntas de síntesis",1)
las=[r for r in R if LA(r)]; nos=[r for r in R if not LA(r)]
con=[r for r in las if inmaduras_ec(r)]; sin=[r for r in las if not inmaduras_ec(r)]
ids=lambda L:", ".join(r["ID"] for r in L)
doc.add_heading("A. Blastos en sangre periférica en la LA",2)
doc.add_paragraph(f"{len(con)} de {len(las)} pacientes con LA ({100*len(con)/len(las):.0f} %) tenían blastos o promielocitos anómalos en el frotis. {len(sin)} no tenían ninguno ({ids(sin)}).")
doc.add_paragraph("Implicación: el frotis es muy útil pero no infalible. Un frotis sin blastos no descarta la LA cuando hay citopenias inexplicadas, dolor óseo persistente o síntomas sistémicos. Esto concuerda con lo descrito en Mangum 2023, Dai 2021 y Singi 2026.")
doc.add_heading("B. Leucocitos en la LA",2)
bajo=[r for r in las if r["Leucocitos"]<4]; norm=[r for r in las if 4<=r["Leucocitos"]<=11]; alto=[r for r in las if r["Leucocitos"]>11]; hip=[r for r in las if r["Leucocitos"]>100]
doc.add_paragraph(f"De las {len(las)} LA:")
for txt in [f"Leucopenia (<4×10⁹/L): {len(bajo)} ({ids(bajo)}).",
            f"Leucocitos normales (4–11×10⁹/L): {len(norm)} ({ids(norm)}).",
            f"Leucocitosis (>11×10⁹/L): {len(alto)}; de ellas, {len(hip)} con hiperleucocitosis >100×10⁹/L ({ids(hip)})."]:
    doc.add_paragraph(txt,style="List Bullet")
doc.add_paragraph(f"En total, {len(bajo)+len(norm)} de {len(las)} LA ({100*(len(bajo)+len(norm))/len(las):.0f} %) NO tenían leucocitosis. La leucocitosis no es requisito para sospechar LA: lo constante son las citopenias, sobre todo la anemia y la trombocitopenia. Coincide con Shome 2026 y Ebrahim 2022.")
doc.add_heading("C. LLA con dolor osteoarticular frente a AIJ",2)
dol=[r for r in las if r["Edad"]<15 and "dolor" in r["Cuadro_clinico"].lower() and r["Diagnostico"].startswith("LLA")]
aij=[r for r in nos if "AIJ" in r["Diagnostico"]]
t=doc.add_table(rows=1,cols=6); t.style="Light Grid Accent 1"
for j,x in enumerate(["ID","Diagnóstico","Hb","Neutrófilos abs","Plaquetas","Blastos %"]): t.rows[0].cells[j].text=x
for r in dol+aij:
    c=t.add_row().cells; c[0].text=r["ID"]; c[1].text=r["Diagnostico"]; c[2].text=fmt(r["Hb"]); c[3].text=fmt(r["Neut_abs"]); c[4].text=fmt(r["Plaquetas"]); c[5].text=fmt(r["Blastos_pct"])
doc.add_paragraph("Respuesta esperada: los niños con LLA tienen neutrófilos más bajos y plaquetas normales-bajas o bajas. Los niños con AIJ tienen neutrofilia y trombocitosis reactiva. Ninguno de los dos grupos tiene necesariamente blastos. Por eso, ante un dolor osteoarticular con neutrófilos o plaquetas «inapropiadamente bajos» para un cuadro inflamatorio, debe sospecharse una LLA (fichas 1, 3, 4, 5 y 7).")
doc.add_heading("D. Rasgos de la LPA y por qué es una urgencia",2)
lpa=[r for r in las if r["Diagnostico"].startswith("LPA")]
doc.add_paragraph(f"Casos: {ids(lpa)}. Rasgos:")
for txt in ["Sangrado mucocutáneo en todos.",
            "Leucopenia en la forma clásica, con leucocitosis en la variante microgranular.",
            f"Trombocitopenia grave (plaquetas de {min(fmt(r['Plaquetas']) for r in lpa)} a {max(fmt(r['Plaquetas']) for r in lpa)}×10⁹/L).",
            "Promielocitos anómalos con granulación intensa, núcleo bilobulado y bastones de Auer en haces.",
            "La variante microgranular puede confundirse con monocitos."]:
    doc.add_paragraph(txt,style="List Bullet")
doc.add_paragraph("Es una urgencia porque la coagulopatía (CID e hiperfibrinólisis) causa muerte temprana por hemorragia. El tratamiento con ATRA se inicia ante la sospecha morfológica, sin esperar al PML::RARA (Zhang 2025, Wang 2026, Haider 2020).")
doc.add_heading("E. Pancitopenia en pacientes sin LA",2)
pan=[r for r in nos if "PANCITOPENIA" in r["Alteraciones_BH"]]
for r in pan:
    doc.add_paragraph(f"{r['ID']}, {r['Diagnostico']}: VCM {fmt(r['VCM'])} fL; frotis: {r['Frotis']}.",style="List Bullet")
doc.add_paragraph("Datos que los diferencian de la LA:")
for txt in ["Ausencia de blastos.",
            "Macrocitosis con neutrófilos hipersegmentados en la anemia megaloblástica.",
            "Displasia con menos del 20 % de blastos en el SMD.",
            "Esplenomegalia con contexto infeccioso o hepático en la leishmaniasis y el hiperesplenismo.",
            "Médula hipocelular en la aplasia."]:
    doc.add_paragraph(txt,style="List Bullet")
doc.add_paragraph("Aun así, la pancitopenia sin explicación clara obliga a estudiar la médula ósea (fichas 23 a 26).")
doc.add_heading("F. Tabla 2×2: «blastos o promielocitos anómalos en SP» frente a LA confirmada",2)
VP=len(con); FN=len(sin); FP=sum(1 for r in nos if inmaduras_ec(r)); VN=len(nos)-FP
fpids=ids([r for r in nos if inmaduras_ec(r)])
t=doc.add_table(rows=4,cols=4); t.style="Light Grid Accent 1"
vals=[["","LA (sí)","LA (no)","Total"],["Prueba positiva",str(VP),str(FP),str(VP+FP)],["Prueba negativa",str(FN),str(VN),str(FN+VN)],["Total",str(VP+FN),str(FP+VN),"50"]]
for i in range(4):
    for j in range(4): t.cell(i,j).text=vals[i][j]
doc.add_paragraph("Medidas de la prueba:")
for txt in [f"Sensibilidad = {VP}/{VP+FN} = {100*VP/(VP+FN):.1f} %",
            f"Especificidad = {VN}/{VN+FP} = {100*VN/(VN+FP):.1f} %",
            f"Valor predictivo positivo (VPP) = {VP}/{VP+FP} = {100*VP/(VP+FP):.1f} %",
            f"Valor predictivo negativo (VPN) = {VN}/{VN+FN} = {100*VN/(VN+FN):.1f} %"]:
    doc.add_paragraph(txt,style="List Bullet")
doc.add_paragraph(f"Falsos positivos: {fpids}. La LMC tiene un 2 % de blastos y el SMD un 3 %, en ambos casos menos del 20 %. Los linfocitos reactivos de la mononucleosis y los mielocitos de la reacción leucemoide NO se cuentan como blastos; si el estudiante los cuenta, debe explicarlo, y se le resta 1 punto.")
doc.add_paragraph("Advertencia: estos valores reflejan la composición de esta base simulada (60 % de LA), mucho más alta que la prevalencia real. No deben interpretarse como el desempeño diagnóstico real del frotis.").runs[0].italic=True

doc.add_heading("5. Hoja de calificación",1)
t=doc.add_table(rows=1,cols=9); t.style="Light Grid Accent 1"
for j,x in enumerate(["ID","P1","P2","P3","P4","P5","P6","Total (/6)","Observaciones"]): t.rows[0].cells[j].text=x
for r in R:
    c=t.add_row().cells; c[0].text=r["ID"]
c=t.add_row().cells; c[0].text="Síntesis A–F (/30)"
c=t.add_row().cells; c[0].text="TOTAL (/330)"; c[8].text="Nota = total ÷ 33"
doc.save("clave_respuestas_ejercicio_50_biometrias.docx")
print("ok",VP,FN,FP,VN,len(bajo),len(norm),len(alto),len(pan))
