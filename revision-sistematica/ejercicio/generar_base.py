"""Base de datos SIMULADA de 50 biometrías hemáticas para un ejercicio docente.
Pacientes, nombres y valores son ficticios. Los patrones se basan en los hallazgos
extraídos de los 38 artículos de la revisión (ver hoja 'Fundamento')."""
import random, csv
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

# (dx_grupo, dx_final, confirmacion, edad, sexo, sintomas, Hb, VCM, WBC, N, L, M, Bl, Otras, plt, frotis, articulos, razonamiento)
C = [
# ---- LLA pediátrica ----
("LA","LLA-B","Aspirado de médula ósea + citometría de flujo",4,"M","Fiebre 10 días, palidez, petequias, hepatoesplenomegalia",7.2,82,48.5,3,35,2,60,0,28,"Linfoblastos 60 %: células pequeñas-medianas, relación N/C alta, cromatina fina, nucléolos poco evidentes, citoplasma escaso basófilo","8, 12, 17","Bicitopenia (anemia + trombocitopenia) con leucocitosis y blastos circulantes: patrón clásico de LLA pediátrica."),
("LA","LLA-B","Aspirado de médula ósea + citometría de flujo",6,"F","Dolor óseo y cojera de 6 semanas, febrícula; sin petequias",10.8,80,4.2,22,74,4,0,0,142,"Sin blastos. Linfocitos de aspecto maduro. Leve anemia normocítica","3, 4, 5, 7, 16","LLA que imita artritis: BH casi normal, sin blastos. La neutropenia relativa (neutrófilos bajos) y la trombocitopenia leve (plaquetas 'normal-bajas' para la inflamación) orientan a LLA frente a AIJ."),
("LA","LLA-B","Aspirado de médula ósea + citometría de flujo",3,"M","Palidez intensa, equimosis, fiebre",6.1,84,2.1,8,84,2,6,0,18,"Pancitopenia; escasos blastos (6 %)","8, 14, 23, 25","Pancitopenia pediátrica con pocos blastos: obliga a médula ósea; la LA es causa frecuente de pancitopenia en niños."),
("LA","LLA-T","Aspirado de médula ósea + citometría de flujo",9,"M","Disnea, tos, masa mediastínica en Rx, adenopatías cervicales",8.5,85,152.0,2,8,1,89,0,35,"Hiperleucocitosis con 89 % de blastos de núcleo irregular/convoluto","22","Hiperleucocitosis (>100×10⁹/L) + masa mediastínica: sospecha de LLA-T."),
("LA","LLA-B","Aspirado de médula ósea + citometría de flujo",2,"F","Irritabilidad, palidez, fiebre",7.8,81,12.3,10,55,3,32,0,41,"Blastos 32 % de tipo linfoide","12, 17","Anemia y trombocitopenia con blastos: LA."),
("LA","LLA-B","Aspirado de médula ósea + citometría de flujo",12,"M","Astenia, epistaxis",9.4,86,6.8,15,50,3,32,0,62,"Blastos 32 %; algunos con nucléolo visible","12, 21","Leucocitos normales no excluyen LA: los blastos en el frotis son la clave."),
("LA","LLA-B","Aspirado de médula ósea + citometría de flujo",5,"F","Dolor articular de rodillas, despertares nocturnos por dolor",11.2,83,7.9,30,68,2,0,0,210,"Sin blastos; morfología sin alteraciones relevantes","3, 4, 5, 7, 14, 16","BH normal y frotis sin blastos NO excluyen LLA: dolor óseo nocturno y persistente exige vigilancia, LDH y valorar médula."),
("LA","LLA-B","Aspirado de médula ósea + citometría de flujo",7,"M","Sangrado gingival, fiebre, esplenomegalia",5.9,84,85.4,1,14,1,84,0,12,"Blastos 84 %","8, 12","Leucocitosis marcada con anemia y trombocitopenia graves."),
("LA","LLA-B","Aspirado de médula ósea + citometría de flujo",14,"F","Fatiga, palidez, adenopatías",8.9,87,3.1,18,72,2,8,0,54,"Blastos 8 %","12, 14","Leucopenia con blastos escasos: frotis revisado manualmente identifica blastos."),
("LA","LLA-B","Aspirado de médula ósea + citometría de flujo",1,"M","Fiebre, palidez, hepatomegalia (18 meses)",7.0,80,24.6,6,40,2,52,0,30,"Blastos 52 %","12","Lactante con bicitopenia y blastos."),
("LA","LLA-B","Aspirado de médula ósea + citometría de flujo",10,"F","Dolor óseo, petequias en piernas",10.1,85,15.7,20,42,3,35,0,88,"Blastos 35 %","4, 12","Dolor óseo + trombocitopenia + blastos."),
("LA","LLA-B","Aspirado de médula ósea + citometría de flujo",8,"M","Palidez, fiebre, equimosis",6.6,86,1.6,10,86,2,2,0,22,"Pancitopenia; blastos raros (2 %), visibles solo en revisión cuidadosa","8, 14, 26","Pancitopenia con blastos casi ausentes: la médula es indispensable (diferencial con anemia aplásica)."),
# ---- LLA adulto ----
("LA","LLA-B","Aspirado de médula ósea + citometría de flujo",24,"M","Fiebre, astenia, dolor óseo",8.1,88,34.3,8,22,2,68,0,31,"Blastos 68 % de aspecto linfoide","21, 22","Adulto joven con bicitopenia y blastos (valores típicos de LLA en adultos)."),
("LA","LLA-B","Aspirado de médula ósea + citometría de flujo",45,"F","Sangrado menstrual abundante, fiebre",7.4,90,17.2,12,28,2,58,0,19,"Blastos 58 %","22","Anemia grave y trombocitopenia grave (<50×10⁹/L), típico de LA."),
("LA","LLA-T","Aspirado de médula ósea + citometría de flujo",19,"M","Disnea, síndrome de vena cava superior",9.8,86,98.0,3,10,1,86,0,40,"Blastos 86 %","22","Leucocitosis alta y masa mediastínica: LLA-T."),
# ---- LMA adulto ----
("LA","LMA","Aspirado de médula ósea + citometría + citogenética",58,"M","Fiebre, infecciones repetidas, astenia",7.0,95,19.2,12,25,8,55,0,22,"Mieloblastos 55 %, citoplasma con gránulos finos, bastones de Auer aislados","21, 22, 31","Bastones de Auer = linaje mieloide."),
("LA","LMA","Aspirado de médula ósea + citometría + citogenética",67,"F","Astenia, disnea de esfuerzo, equimosis",8.4,98,2.6,14,60,4,22,0,45,"Blastos 22 %; neutrófilos hipogranulares","22, 24","LMA con leucopenia: la leucocitosis no es necesaria."),
("LA","LMA","Aspirado de médula ósea + citometría + citogenética",42,"M","Fiebre, sangrado nasal, pérdida de peso",6.2,92,54.0,5,10,15,70,0,24,"Mieloblastos 70 %","22","Patrón de LMA CD34+: más leucocitos, menos Hb y plaquetas."),
("LA","LMA","Aspirado de médula ósea + citometría + citogenética",71,"M","Astenia progresiva, palidez",9.1,101,1.8,6,80,4,10,0,38,"Pancitopenia; blastos 10 %","24, 28","LMA en adulto mayor que se presenta como pancitopenia."),
("LA","LMA (monoblástica, M5)","Aspirado de médula ósea + citometría + citogenética",35,"F","Hipertrofia gingival, fiebre",7.6,93,43.5,4,12,40,44,0,43,"Monoblastos/promonocitos 44 % con núcleo plegado; monocitosis","21, 22","Hipertrofia gingival + monocitosis + blastos: LMA monocítica."),
("LA","LMA","Aspirado de médula ósea + citometría + citogenética",50,"M","Cefalea, visión borrosa, fiebre",8.0,94,88.4,3,7,10,80,0,30,"Mieloblastos 80 %; algunos con bastones de Auer","22","Leucocitosis alta (riesgo de leucostasis)."),
("LA","LMA","Aspirado de médula ósea + citometría + citogenética",29,"F","Petequias, gingivorragia, fiebre",6.8,90,7.5,20,45,5,30,0,15,"Blastos 30 %","21, 22","Leucocitos normales con blastos y trombocitopenia grave."),
("LA","LMA","Aspirado de médula ósea + citometría + citogenética",63,"M","Astenia, infecciones respiratorias",10.2,104,4.1,35,50,5,10,0,92,"Blastos 10 %; displasia (neutrófilos pseudo-Pelger)","24, 37","Pocos blastos en SP; la médula mostró ≥20 % de blastos (diferencial con SMD)."),
# ---- LMA pediátrica ----
("LA","LMA","Aspirado de médula ósea + citometría + citogenética",11,"M","Dolor óseo en piernas, fiebre",7.9,88,61.0,6,12,7,75,0,27,"Mieloblastos 75 %","20","La LMA pediátrica también puede iniciar con dolor musculoesquelético."),
("LA","LMA","Aspirado de médula ósea + citometría + citogenética",3,"F","Palidez, fiebre, petequias",8.2,86,9.4,15,50,10,25,0,33,"Blastos 25 %","20, 21","Niña con bicitopenia y blastos."),
# ---- LPA ----
("LA","LPA (LMA con PML::RARA)","Médula ósea + PML::RARA (PCR/FISH)",37,"F","Gingivorragia, equimosis extensas, menorragia",7.2,92,1.2,6,50,4,0,40,18,"Promielocitos anómalos 40 %: granulación intensa, núcleo bilobulado, bastones de Auer en haces (células 'faggot')","33, 34, 38","Leucopenia + trombocitopenia + sangrado + promielocitos anómalos: urgencia (posible CID); iniciar ATRA ante la sospecha."),
("LA","LPA (LMA con PML::RARA)","Médula ósea + PML::RARA (PCR/FISH)",45,"M","Equimosis, hematuria",9.5,90,3.4,10,45,5,0,40,35,"Promielocitos anómalos 40 %","29, 34, 38","Patrón típico de LPA: leucocitos bajos y plaquetas ~35×10⁹/L."),
("LA","LPA variante microgranular","Médula ósea + PML::RARA (PCR/FISH)",22,"M","Sangrado gingival, fiebre",8.1,91,28.0,4,18,3,0,75,22,"Promielocitos anómalos microgranulares con núcleo bilobulado 75 %; pueden confundirse con monocitos","33, 34","La variante microgranular cursa con leucocitosis y los promielocitos imitan monocitos: el analizador puede clasificarlos mal."),
# ---- LAFM ----
("LA","Leucemia aguda de fenotipo mixto (B/mieloide)","Médula ósea + citometría de flujo",33,"M","Fiebre y sangrado",6.7,89,45.0,5,15,5,75,0,22,"Blastos 75 % heterogéneos","9, 22","La morfología no define el linaje: se necesita citometría."),
# ---- LA aleucémica ----
("LA","LMA (presentación aleucémica)","Aspirado y biopsia de médula ósea + citometría",55,"F","Astenia, palidez",8.8,96,2.2,25,70,5,0,0,40,"Sin blastos circulantes; anisocitosis leve","14, 16, 37","Citopenias sin blastos: la LA puede no mostrar blastos en SP; la médula confirma."),
# ======== NO LEUCEMIA AGUDA ========
("Otra","Anemia aplásica","Biopsia de médula ósea (hipocelular, sin blastos)",16,"M","Petequias, palidez, astenia",6.5,98,1.9,20,78,2,0,0,12,"Pancitopenia sin blastos ni células inmaduras; reticulocitos 0,3 %","23, 26","Diferencial principal de la LA con pancitopenia: frotis sin blastos y médula hipocelular."),
("Otra","Anemia aplásica","Biopsia de médula ósea (hipocelular, sin blastos)",8,"F","Equimosis, epistaxis",7.1,96,2.4,25,73,2,0,0,15,"Pancitopenia sin blastos","23, 26","Igual a la LA en la BH; el frotis y la médula la distinguen."),
("Otra","Anemia megaloblástica (déficit de B12)","Niveles de B12 + médula megaloblástica",46,"F","Astenia, parestesias, glositis",7.3,118,2.8,48,46,6,0,0,72,"Macroovalocitos, neutrófilos hipersegmentados (≥6 lóbulos)","24, 25","Pancitopenia con VCM >100 e hipersegmentación: causa tratable, primera causa de pancitopenia en varias cohortes."),
("Otra","Anemia megaloblástica (déficit de B12/folato)","Niveles de B12 y folato",9,"M","Palidez, irritabilidad, dieta pobre",6.9,112,3.2,45,50,5,0,0,85,"Macrocitosis, neutrófilos hipersegmentados","23, 25","Macrocitosis marcada orienta a megaloblástica, no a LA."),
("Otra","Púrpura trombocitopénica inmune (PTI)","Diagnóstico de exclusión (frotis normal salvo plaquetas)",5,"F","Petequias de inicio súbito tras cuadro viral; buen estado general",12.1,82,7.8,45,48,7,0,0,9,"Trombocitopenia aislada con macroplaquetas; series roja y blanca normales","27, 34","Trombocitopenia AISLADA con Hb y leucocitos normales y frotis sin blastos."),
("Otra","Púrpura trombocitopénica inmune (PTI)","Diagnóstico de exclusión",28,"F","Petequias y gingivorragia leve",13.0,86,6.5,58,35,7,0,0,14,"Macroplaquetas; resto normal","27, 34","Trombocitopenia aislada."),
("Otra","Artritis idiopática juvenil (AIJ)","Criterios ILAR; médula normal si se realizó",6,"F","Artritis de rodilla y tobillo 8 semanas, rigidez matutina",10.9,79,12.4,65,28,7,0,0,485,"Neutrofilia leve, trombocitosis; sin blastos","1, 3, 4, 5, 7","En la AIJ los neutrófilos y las plaquetas suelen estar normales o altos; en la LLA que imita artritis suelen estar bajos."),
("Otra","Artritis idiopática juvenil (AIJ)","Criterios ILAR",10,"M","Dolor y tumefacción articular, fiebre vespertina",11.5,81,10.1,60,32,8,0,0,410,"Trombocitosis reactiva; sin blastos","1, 3, 5, 7","Contraste con los casos de LLA con dolor óseo."),
("Otra","Mononucleosis infecciosa (VEB)","Anticuerpos heterófilos / serología VEB",17,"M","Faringitis, fiebre, adenopatías, esplenomegalia",13.8,88,14.2,25,67,8,0,0,120,"Linfocitos reactivos (atípicos) 30 % con citoplasma amplio que 'abraza' eritrocitos; pueden confundirse con blastos","34, 36","Linfocitos reactivos ≠ blastos: citoplasma abundante, cromatina más madura, población heterogénea."),
("Otra","Sepsis bacteriana","Hemocultivo positivo",62,"M","Fiebre alta, hipotensión, foco urinario",11.8,89,28.5,86,6,4,0,4,260,"Neutrofilia con desviación a la izquierda (bandas, metamielocitos 4 %), granulación tóxica, cuerpos de Döhle","36","Leucocitosis por infección: neutrófilos maduros, sin blastos; la IA y las reglas deben distinguirla de la LA."),
("Otra","Reacción leucemoide","Resolución con tratamiento de la causa (neumonía)",70,"F","Neumonía grave",10.5,90,52.0,80,5,3,0,12,310,"Neutrofilia con mielocitos 6 % y metamielocitos 6 %; sin blastos, sin basofilia","28, 36","Leucocitosis muy alta pero madura, sin hiato leucémico."),
("Otra","Anemia ferropénica","Ferritina baja",30,"F","Astenia, menstruaciones abundantes",8.1,64,6.2,60,32,6,0,0,450,"Microcitosis, hipocromía, eliptocitos ('lápices'); trombocitosis reactiva","25","Anemia aislada microcítica con plaquetas altas: no orienta a LA."),
("Otra","Leucemia mieloide crónica, fase crónica","BCR::ABL1 por RT-PCR",48,"M","Saciedad precoz, esplenomegalia gigante",8.5,88,153.5,55,4,2,2,37,312,"Todos los estadios de maduración (mielocitos 20 %, metamielocitos 10 %), basofilia 5 %, eosinofilia 2 %; blastos 2 %","22, 31","Leucocitosis muy alta con plaquetas normales/altas y maduración completa: leucemia CRÓNICA, no aguda."),
("Otra","Leucemia linfocítica crónica","Citometría de flujo (CD5+/CD23+)",66,"M","Adenopatías indoloras, hallazgo casual",10.1,92,69.0,8,88,4,0,0,175,"Linfocitos pequeños maduros 88 %, sombras de Gumprecht (células rotas)","22, 36","Linfocitosis madura en adulto mayor; no es LA."),
("Otra","Síndrome mielodisplásico","Médula ósea (blastos <20 %, displasia) + citogenética",74,"M","Astenia, anemia que no responde a hierro",8.9,104,2.9,40,52,5,3,0,68,"Displasia: neutrófilos hipogranulares, pseudo-Pelger; blastos 3 %","24, 37","Citopenias + macrocitosis + displasia con <20 % de blastos: SMD, no LA."),
("Otra","Dengue (infección viral)","NS1 / serología",25,"F","Fiebre, cefalea retroocular, mialgias, exantema",13.5,86,2.6,40,50,10,0,0,48,"Leucopenia, linfocitos reactivos aislados; sin blastos","36","Leucopenia y trombocitopenia agudas por virus; Hb normal o alta (hemoconcentración)."),
("Otra","Leishmaniasis visceral (kala-azar)","Amastigotes en médula ósea",4,"M","Fiebre prolongada, esplenomegalia masiva, pérdida de peso",7.0,80,2.3,30,65,5,0,0,50,"Pancitopenia sin blastos","23, 25, 26","Causa infecciosa de pancitopenia en zonas endémicas."),
("Otra","Anemia hemolítica (esferocitosis hereditaria)","Prueba EMA / fragilidad osmótica",12,"F","Ictericia, palidez, esplenomegalia",7.5,88,9.0,58,34,8,0,0,260,"Esferocitos, policromatofilia; reticulocitos 15 %","25","Anemia con reticulocitosis y plaquetas normales: no es LA."),
("Otra","Sin enfermedad hematológica (dolor de crecimiento)","Seguimiento clínico; BH normal",13,"M","Dolor de piernas vespertino, sin cojera ni fiebre",14.5,86,7.0,55,35,7,0,0,280,"Frotis normal","3, 4, 5","BH y frotis normales; vigilar si el dolor persiste, es nocturno o se acompaña de síntomas sistémicos."),
("Otra","Hiperesplenismo por cirrosis hepática","Ecografía abdominal, pruebas hepáticas",56,"M","Ascitis, ictericia, antecedente de alcoholismo",10.0,102,3.0,55,35,8,0,0,65,"Macrocitosis leve, dianocitos; sin blastos","24","Citopenias por secuestro esplénico."),
]

nombres = ["Mateo Hernández Ruiz","Valentina Castro Ortega","Santiago López Mejía","Diego Ramírez Salas","Camila Torres Vega","Emiliano Flores Navarro","Renata Gómez Paredes","Leonardo Díaz Fuentes","Ximena Morales Cruz","Tomás Jiménez Rivas","Sofía Vargas Medina","Andrés Peña Castillo","Julián Rojas Aguilar","María Fernanda Silva León","Ricardo Herrera Campos","Héctor Gutiérrez Luna","Patricia Mendoza Ríos","Fernando Sánchez Ibarra","Arturo Cabrera Molina","Daniela Ortiz Romero","Jorge Reyes Valdez","Laura Guzmán Cortés","Raúl Delgado Pineda","Bruno Acosta Lara","Regina Cervantes Mora","Alejandra Ponce Rangel","Manuel Domínguez Soto","Iván Carrillo Becerra","Óscar Villalobos Trejo","Gabriela Nieto Espinoza","Kevin Salazar Montes","Lucía Ramos Benítez","Teresa Quintero Ávila","Joaquín Muñoz Serrano","Abril Rosales Galindo","Mónica Bravo Zamora","Isabella Figueroa Montoya","Sebastián Cordero Vela","Carlos Esquivel Duarte","Rogelio Barrera Olmos","Elena Ferrer Solís","Claudia Robles Arellano","Francisco Lozano Treviño","Alberto Miranda Cano","Gustavo Peralta Durán","Paola Ibáñez Robledo","Matías Cuevas Barrón","Natalia Arroyo Sandoval","Daniel Murillo Ochoa","Ernesto Valencia Godoy"]
assert len(C)==50 and len(nombres)==50
random.seed(2026)
orden=list(range(50)); random.shuffle(orden)

filas=[]
for k,i in enumerate(orden):
    g,dx,conf,edad,sexo,sint,hb,vcm,wbc,n,l,m,bl,ot,plt,frot,art,raz=C[i]
    s=n+l+m+bl+ot; assert s<=100,(dx,s)
    eos=100-s
    nom=nombres[i]
    # sexo coherente con nombre ya elegido a mano
    filas.append(dict(ID=f"P{k+1:02d}",Nombre=nom,Edad=edad,Grupo_edad="Pediátrico (<15 años)" if edad<15 else "Adulto",Sexo=sexo,
        Cuadro_clinico=sint,Hb=hb,Hto=round(hb*3,1),VCM=vcm,Leucocitos=wbc,
        Neut_pct=n,Linf_pct=l,Mono_pct=m,Eos_pct=eos,Blastos_pct=bl,Otras_pct=ot,
        Neut_abs=round(wbc*n/100,2),Linf_abs=round(wbc*l/100,2),Blastos_abs=round(wbc*bl/100,2),
        Plaquetas=plt,Frotis=frot,Diagnostico=dx,Es_LA="Sí" if g=="LA" else "No",
        Confirmacion=conf,Razonamiento=raz,Articulos=art))
filas.sort(key=lambda r:r["ID"])

def flags(r):
    f=[]
    if r["Hb"]<(11 if r["Edad"]<15 else 12): f.append("anemia")
    if r["Leucocitos"]<4: f.append("leucopenia")
    if r["Leucocitos"]>11: f.append("leucocitosis")
    if r["Leucocitos"]>100: f.append("hiperleucocitosis")
    if r["Plaquetas"]<150: f.append("trombocitopenia")
    if r["Plaquetas"]>450: f.append("trombocitosis")
    if r["Neut_abs"]<1.5: f.append("neutropenia")
    cit=sum(x in f for x in ["anemia","leucopenia","trombocitopenia"])
    if cit==3: f.append("PANCITOPENIA")
    return ", ".join(f) or "sin alteraciones"
for r in filas: r["Alteraciones_BH"]=flags(r)

cols_ej=[("ID","ID"),("Nombre","Nombre (ficticio)"),("Edad","Edad (años)"),("Sexo","Sexo"),("Cuadro_clinico","Cuadro clínico"),
 ("Hb","Hb (g/dL)"),("Hto","Hto (%)"),("VCM","VCM (fL)"),("Leucocitos","Leucocitos (×10⁹/L)"),("Neut_pct","Neutrófilos %"),
 ("Linf_pct","Linfocitos %"),("Mono_pct","Monocitos %"),("Eos_pct","Eos/Baso %"),("Blastos_pct","Blastos %"),("Otras_pct","Otras células %"),
 ("Neut_abs","Neutrófilos abs (×10⁹/L)"),("Plaquetas","Plaquetas (×10⁹/L)"),("Frotis","Frotis de sangre periférica")]
cols_clave=[("ID","ID"),("Nombre","Nombre (ficticio)"),("Edad","Edad"),("Grupo_edad","Grupo de edad"),("Alteraciones_BH","Alteraciones de la BH"),
 ("Es_LA","¿Leucemia aguda?"),("Diagnostico","Diagnóstico confirmado"),("Confirmacion","Método de confirmación"),
 ("Razonamiento","Razonamiento docente"),("Articulos","Artículos de la revisión que sustentan el patrón (n.º de ficha)")]

wb=Workbook()
H=Font(bold=True,color="FFFFFF"); F=PatternFill("solid",fgColor="1F4E78")
def hoja(ws,cols,rows):
    ws.append([c[1] for c in cols])
    for c in ws[1]: c.font=H; c.fill=F; c.alignment=Alignment(wrap_text=True,vertical="center")
    for r in rows: ws.append([r[c[0]] for c in cols])
    for j,(k,_) in enumerate(cols,1):
        w=60 if k in("Frotis","Razonamiento","Cuadro_clinico") else 34 if k in("Confirmacion","Diagnostico","Alteraciones_BH","Nombre","Articulos") else 12
        ws.column_dimensions[get_column_letter(j)].width=w
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment=Alignment(wrap_text=True,vertical="top")
    ws.freeze_panes="C2"

ws=wb.active; ws.title="Instrucciones"
txt=["EJERCICIO: Biometría hemática y frotis en la sospecha temprana de leucemia aguda",
"",
"AVISO: base de datos SIMULADA con fines docentes. Los pacientes, nombres y valores son FICTICIOS.",
"No corresponden a personas reales ni a registros clínicos. Los patrones se construyeron a partir de los",
"hallazgos de los 38 artículos de la revisión sistemática (ver hoja 'Fundamento' y la ficha de extracción).",
"",
"Contenido:",
" • 'Ejercicio': 50 biometrías con cuadro clínico y frotis, SIN diagnóstico (para el estudiante).",
" • 'Preguntas': preguntas guía del ejercicio.",
" • 'Clave': diagnóstico confirmado, método de confirmación, razonamiento y artículos de soporte.",
" • 'Fundamento': patrones de la evidencia usados para construir los casos.",
"",
"Composición: 30 leucemias agudas (15 LLA, 10 LMA, 3 LPA, 1 fenotipo mixto, 1 LMA aleucémica)",
"y 20 diagnósticos diferenciales (aplasia, megaloblástica, PTI, AIJ, infecciones, LMC, LLC, SMD, etc.).",
"Incluye casos 'trampa' basados en la evidencia: LLA con BH normal y sin blastos, LA aleucémica,",
"linfocitos reactivos que imitan blastos, LPA microgranular y leucemias crónicas.",
"",
"Valores de referencia orientativos: Hb adulto ≥12 g/dL (niño ≥11); leucocitos 4–11×10⁹/L;",
"neutrófilos ≥1,5×10⁹/L; plaquetas 150–450×10⁹/L; VCM 80–100 fL. Blastos en SP: 0 %.",
"Nota: el diagnóstico de LA exige médula ósea/inmunofenotipo; la BH y el frotis solo fundamentan la SOSPECHA."]
for t in txt: ws.append([t])
ws["A1"].font=Font(bold=True,size=14); ws["A3"].font=Font(bold=True,color="C00000"); ws.column_dimensions["A"].width=110

hoja(wb.create_sheet("Ejercicio"),cols_ej,filas)
wp=wb.create_sheet("Preguntas")
for q in ["Preguntas guía para cada paciente:",
"1. ¿Qué alteraciones cuantitativas presenta la BH (anemia, leucopenia/leucocitosis, trombocitopenia, pancitopenia)?",
"2. ¿Qué hallazgo del frotis es más relevante? ¿Hay blastos, promielocitos anómalos, bastones de Auer o células reactivas?",
"3. ¿La combinación BH + frotis + clínica justifica sospechar leucemia aguda? ¿Con qué urgencia?",
"4. Si sospecha LA, ¿orienta a linaje linfoide o mieloide? ¿Qué dato lo apoya y qué limitación tiene?",
"5. Si no es LA, ¿cuál es el diagnóstico diferencial más probable y qué dato lo distingue?",
"6. ¿Qué estudio confirmaría el diagnóstico?",
"",
"Preguntas de síntesis del grupo:",
"A. ¿Cuántos pacientes con LA tenían blastos en SP? ¿Cuántos no? ¿Qué implica para la sensibilidad del frotis?",
"B. ¿Cuántas LA tenían leucocitos normales o bajos? ¿La leucocitosis es requisito para sospechar LA?",
"C. Compare los casos de LLA con dolor óseo y los de AIJ: ¿qué parámetros de la BH los separan?",
"D. ¿Qué rasgos identifican a la LPA y por qué es una urgencia?",
"E. ¿Qué casos de NO LA tienen pancitopenia? ¿Qué dato del frotis o del VCM los diferencia de la LA?",
"F. Construya una tabla 2×2 usando 'blastos en SP >0 %' como prueba y la LA confirmada como referencia; calcule sensibilidad y especificidad."]:
    wp.append([q])
wp.column_dimensions["A"].width=120; wp["A1"].font=Font(bold=True); wp["A9"].font=Font(bold=True)
hoja(wb.create_sheet("Clave"),cols_clave,filas)

wf=wb.create_sheet("Fundamento")
fund=[("Patrón usado en los casos","Evidencia de la revisión (n.º de ficha)"),
("LMA/LLA en adultos: Hb media ~7 g/dL, leucocitos medianos 12–19×10⁹/L, trombocitopenia grave (<50×10⁹/L) en >90 %","Shome 2026 (ficha 22)"),
("Hb ~8 g/dL, leucocitos medianos 34–43×10⁹/L, plaquetas medianas 31–43×10⁹/L; la BH no distingue el linaje","Al-Aghbri 2026 (ficha 21)"),
("LMA CD34+: más leucocitos, menos Hb y plaquetas","Shome 2026 (ficha 22)"),
("LPA: leucopenia frecuente (mediana 5,86×10⁹/L en Zhang; 3,4 ± 1,5 en Wang), plaquetas ~35×10⁹/L, promielocitos anómalos en SP ~40 % (1–84 %)","Zhang 2025 (ficha 34); Wang 2026 (ficha 38)"),
("LPA: plaquetas bajas con IPF baja/normal y NE-SFL alto (alerta por CPD)","Haider 2020 (ficha 29)"),
("LA sin blastos circulantes al diagnóstico; LA con BH normal","Mangum 2023 (ficha 16); Dai 2021 (ficha 14); Singi 2026 (ficha 37)"),
("LLA que imita artritis: dolor osteoarticular; neutrófilos/plaquetas más bajos que en AIJ","Agodi 2013; Brix 2020; Louvigné 2020; Torres Jiménez 2023; Mousavi Torshizi 2026 (fichas 1, 3, 4, 5, 7)"),
("Pancitopenia pediátrica: LA en ~17–26 % (aplásica y megaloblástica como diferenciales principales)","Zeb Jan 2013; Zeeshan 2019; Alim 2021 (fichas 23, 25, 26)"),
("Pancitopenia del adulto: LMA 27,4 %; anemia megaloblástica 41,9 %","Das Makheja 2013 (ficha 24)"),
("Trombocitopenia con indicación de médula: LA 28 %","Verma 2022 (ficha 27)"),
("LMA con perfil heterogéneo (1/3 leucopenia; 1/3 Hb o plaquetas normales)","Ebrahim 2022 (ficha 28)"),
("Leucocitosis: reglas de revisión no alertan en parte de las LA; diferencial con infección bacteriana/viral","Liao 2026 (ficha 36)"),
("Linaje requiere citometría: errores de linaje morfológico ~11 %; LAFM","Al-Aghbri 2026 (ficha 21); Sharma 2017 (ficha 9)"),
("Pancitopenia en LLA pediátrica","Raja 2015 (ficha 8)"),
("LMA pediátrica con síntomas musculoesqueléticos","Jensen 2025 (ficha 20)"),
("Valores no cubiertos por la revisión (LMC, LLC, SMD, PTI, dengue, ferropenia, hemólisis, cirrosis) se construyeron con patrones hematológicos de manual, no con datos de la revisión","Inferencia del revisor (docente)")]
for f in fund: wf.append(list(f))
for c in wf[1]: c.font=H; c.fill=F
wf.column_dimensions["A"].width=100; wf.column_dimensions["B"].width=70
for row in wf.iter_rows(min_row=2):
    for c in row: c.alignment=Alignment(wrap_text=True,vertical="top")

out="/home/user/Claude/revision-sistematica/ejercicio/"
wb.save(out+"base_50_biometrias_ejercicio.xlsx")
with open(out+"base_50_biometrias_completa.csv","w",newline="",encoding="utf-8-sig") as fh:
    w=csv.DictWriter(fh,fieldnames=list(filas[0].keys())); w.writeheader(); w.writerows(filas)
la=sum(r["Es_LA"]=="Sí" for r in filas)
print("LA:",la,"No LA:",50-la)
print("LA con blastos/promielocitos en SP:",sum(r["Es_LA"]=="Sí" and (r["Blastos_pct"]>0 or "Promielocitos" in r["Frotis"]) for r in filas))
print("No-LA con blastos:",sum(r["Es_LA"]=="No" and r["Blastos_pct"]>0 for r in filas))
print("LA con leucocitos <=11:",sum(r["Es_LA"]=="Sí" and r["Leucocitos"]<=11 for r in filas))
