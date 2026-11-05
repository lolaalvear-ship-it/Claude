# Etapa 2 — Estrategias de búsqueda y recuperación de publicaciones

**Fecha de ejecución de las búsquedas:** 5 de noviembre de 2026 (UTC)
**Ejecutor:** asistente de IA, mediante las API públicas de NCBI (E-utilities) y Europe PMC (REST). Los scripts, las ecuaciones y los registros descargados están en `etapa2/datos/` para que cualquiera pueda reproducir o auditar la búsqueda.
**Norma de notificación:** PRISMA-S (Rethlefsen et al., 2021).

**Decisiones de la investigadora (aplicadas tal como se recomendó en la Etapa 1):** series de casos ≥10 pacientes; idiomas inglés, español y portugués; modelos de aprendizaje automático basados en la BH solo como subgrupo separado.

---

## 1. Resumen de fuentes y recuentos

| Fuente | Interfaz | Estado | Filtros | Registros |
|---|---|---|---|---|
| PubMed/MEDLINE | NCBI E-utilities (`esearch`/`efetch`) | **Ejecutada** | Exclusión de estudios solo en animales; sin límite de fecha, idioma ni tipo de publicación | **2798** |
| Europe PMC | API REST v6 (`/search`) | **Ejecutada** | Ninguno | **1346** |
| Scopus | Elsevier | **Pendiente de ejecución**: sin acceso por suscripción | — | — |
| Web of Science Core Collection | Clarivate | **Pendiente de ejecución**: sin acceso por suscripción | — | — |
| Embase | Elsevier (Embase.com) | **Pendiente de ejecución**: sin acceso por suscripción | — | — |
| Cochrane Library (CDSR y CENTRAL) | Wiley | **Pendiente de ejecución**: interfaz sin API pública accesible | — | — |
| LILACS (Portal BVS) | pesquisa.bvsalud.org | **Pendiente de ejecución**: el portal devolvió HTTP 403 a las consultas automatizadas (protección antibots), aunque la red del entorno lo permitía | — | — |
| SciELO | search.scielo.org | **Pendiente de ejecución**: el portal exige un desafío de navegador antibots (*Bunny Shield*) | — | — |
| Google Scholar | Web | **Pendiente de ejecución**: sin API y con resultados no reproducibles | — | — |
| **Total identificado en bases ejecutadas** | | | | **4144** |

Las ecuaciones de las fuentes pendientes están en la sección 4. Si la investigadora las ejecuta, los nuevos registros se añadirán al cribado con la misma deduplicación, y sus recuentos se incorporarán al diagrama PRISMA. Mientras tanto, esas celdas quedan vacías.

## 2. PubMed/MEDLINE

### 2.1 Construcción y recuentos por bloque (05/11/2026)

| Bloque | Contenido | Registros |
|---|---|---|
| #1 | Leucemia aguda (MeSH + texto libre) | 162 755 |
| #2 | Biometría hemática / frotis (MeSH + texto libre) | 215 229 |
| #3 (v1) | Presentación, diagnóstico, sospecha, exactitud | 3 537 699 |
| #1 AND #2 | | 5 847 |
| #1 AND #2, sin estudios solo en animales | | 5 710 |
| #1 AND #2 AND #3 (v1), sin estudios solo en animales | | 1 782 |
| **#1 AND #2 AND #3 (v2, ampliado), sin estudios solo en animales — estrategia final** | | **2 798** |

### 2.2 Por qué se aplicó y se amplió el bloque #3

El protocolo preveía aplicar el bloque #3 solo si #1 AND #2 resultaba inmanejable. Con 5710 registros y un único revisor, se aplicó. Antes de aceptarlo se hizo una **prueba de sensibilidad**: se tomó una muestra aleatoria de 200 registros de los 3928 que el bloque #3 (v1) eliminaba (semilla 20261105; lista en `etapa2/datos/b3_check_sample.txt`) y se revisaron sus títulos.

- En la muestra aparecieron **7 títulos potencialmente pertinentes** (≈3,5 %). Por ejemplo: PMID 12416355, sobre las características epidemiológicas, clínicas y citohematológicas de la LLA del adulto en Túnez; PMID 6949609, una serie de 39 casos de leucemia promielocítica aguda con descripción morfológica; y PMID 3166371, sobre el uso del analizador Technicon H-1 en la caracterización de las leucemias.
- Extrapolado a los 3928 registros eliminados, se habrían perdido decenas de estudios. Por eso se amplió el bloque #3 con `characteristic*`, `profile*`, `morpholog*`, `epidemiolog*` y los subencabezamientos MeSH `/diagnosis`.
- La versión ampliada (v2) recupera 4 de los 7 títulos señalados, entre ellos los tres citados arriba. Los tres no recuperados (PMID 26708693, 291504 y 4063525) parecen, por el título, un reporte de caso, un estudio del VCM y un subgrupo citogenético, respectivamente: es poco probable que sean elegibles, pero la pérdida se declara como limitación.

Esta verificación fue **solo por título**, con un único revisor.

### 2.3 Ecuación final exacta (traducción de PubMed tal como la devolvió `esearch`, más el bloque ampliado)

```
(("Leukemia, Myeloid, Acute"[Mesh] OR "Precursor Cell Lymphoblastic Leukemia-Lymphoma"[Mesh] OR "Leukemia, Promyelocytic, Acute"[Mesh] OR "acute leukemia*"[tiab] OR "acute leukaemia*"[tiab] OR "acute myeloid leukemia"[tiab] OR "acute myeloid leukaemia"[tiab] OR "acute myelogenous leukemia"[tiab] OR "acute lymphoblastic leukemia"[tiab] OR "acute lymphoblastic leukaemia"[tiab] OR "acute lymphocytic leukemia"[tiab] OR "acute promyelocytic leukemia"[tiab] OR "acute promyelocytic leukaemia"[tiab] OR "acute nonlymphocytic leukemia"[tiab])
AND
("Blood Cell Count"[Mesh] OR "Hematologic Tests"[Mesh:noexp] OR "complete blood count*"[tiab] OR "full blood count*"[tiab] OR "blood count*"[tiab] OR CBC[tiab] OR hemogram*[tiab] OR haemogram*[tiab] OR "hematological parameter*"[tiab] OR "haematological parameter*"[tiab] OR "peripheral blood smear*"[tiab] OR "peripheral blood film*"[tiab] OR "blood film*"[tiab] OR "blood smear*"[tiab] OR "peripheral smear*"[tiab] OR "circulating blast*"[tiab] OR "peripheral blood blast*"[tiab] OR "blast flag*"[tiab] OR "hematology analyzer*"[tiab] OR "haematology analyser*"[tiab] OR "hematology analyser*"[tiab])
AND
("Early Diagnosis"[Mesh] OR "Sensitivity and Specificity"[Mesh] OR "Diagnosis, Differential"[Mesh] OR "Delayed Diagnosis"[Mesh] OR "Pancytopenia"[Mesh] OR "Primary Health Care"[Mesh] OR "presenting feature*"[tiab] OR "presenting sign*"[tiab] OR "presenting symptom*"[tiab] OR "clinical presentation"[tiab] OR "initial presentation"[tiab] OR "at presentation"[tiab] OR "at diagnosis"[tiab] OR "early diagnosis"[tiab] OR "diagnostic accuracy"[tiab] OR sensitivity[tiab] OR specificity[tiab] OR "predictive value*"[tiab] OR "primary care"[tiab] OR "general practice"[tiab] OR suspicion[tiab] OR pancytopeni*[tiab] OR cytopeni*[tiab] OR aleuk*[tiab] OR subleuk*[tiab] OR "clinical feature*"[tiab] OR "hematological feature*"[tiab] OR "haematological feature*"[tiab] OR "hematological finding*"[tiab] OR "haematological finding*"[tiab] OR "hematological abnormalit*"[tiab] OR "haematological abnormalit*"[tiab] OR "laboratory finding*"[tiab] OR "laboratory feature*"[tiab] OR "diagnostic delay"[tiab] OR characteristic*[tiab] OR profile*[tiab] OR morpholog*[tiab] OR epidemiolog*[tiab] OR "Leukemia/diagnosis"[Mesh:noexp] OR "Leukemia, Myeloid, Acute/diagnosis"[Mesh] OR "Precursor Cell Lymphoblastic Leukemia-Lymphoma/diagnosis"[Mesh]))
NOT (animals[mh] NOT humans[mh])
```

Archivo exacto, sin saltos de línea: `etapa2/datos/pubmed_final_query.txt`. Lista de PMID: `pubmed_v2_pmids.txt`. Registros completos en formato MEDLINE: `pubmed_v2.medline`.

**Nota sobre los términos en español:** PubMed indexa los títulos traducidos al inglés y los MeSH se asignan con independencia del idioma, de modo que los artículos en español y portugués indexados en MEDLINE quedan cubiertos por esta ecuación. Los términos DeCS en español se reservan para LILACS y SciELO.

## 3. Europe PMC

**Uso:** fuente complementaria para registros no indizados en MEDLINE (preprints, PMC, Agricola) y para términos del título o resumen que PubMed no recuperó.

**Incidencia técnica:** el campo `MESH:` de Europe PMC no interpreta correctamente los encabezamientos que contienen comas (por ejemplo, `MESH:"Leukemia, Myeloid, Acute"` devolvió 280 registros, y combinado con OR devolvía todo el índice: 601 158 registros). Se eliminaron los campos MeSH y se usaron solo los términos de título y resumen (`TITLE_ABS`). La pérdida de sensibilidad es mínima, porque los registros MEDLINE ya se captan en PubMed con MeSH.

**Ecuación final exacta (05/11/2026; 1346 registros):**

```
(TITLE_ABS:"acute leukemia" OR TITLE_ABS:"acute leukaemia" OR TITLE_ABS:"acute leukemias" OR TITLE_ABS:"acute myeloid leukemia" OR TITLE_ABS:"acute myeloid leukaemia" OR TITLE_ABS:"acute myelogenous leukemia" OR TITLE_ABS:"acute lymphoblastic leukemia" OR TITLE_ABS:"acute lymphoblastic leukaemia" OR TITLE_ABS:"acute lymphocytic leukemia" OR TITLE_ABS:"acute promyelocytic leukemia" OR TITLE_ABS:"acute nonlymphocytic leukemia")
AND
(TITLE_ABS:"complete blood count" OR TITLE_ABS:"full blood count" OR TITLE_ABS:"blood count" OR TITLE_ABS:"blood counts" OR TITLE_ABS:CBC OR TITLE_ABS:hemogram* OR TITLE_ABS:haemogram* OR TITLE_ABS:"hematological parameters" OR TITLE_ABS:"haematological parameters" OR TITLE_ABS:"peripheral blood smear" OR TITLE_ABS:"peripheral blood film" OR TITLE_ABS:"blood film" OR TITLE_ABS:"blood smear" OR TITLE_ABS:"peripheral smear" OR TITLE_ABS:"circulating blasts" OR TITLE_ABS:"peripheral blood blasts" OR TITLE_ABS:"blast flag" OR TITLE_ABS:"blast flags" OR TITLE_ABS:"hematology analyzer" OR TITLE_ABS:"haematology analyser")
AND
(TITLE_ABS:"presenting features" OR TITLE_ABS:"presenting signs" OR TITLE_ABS:"presenting symptoms" OR TITLE_ABS:"clinical presentation" OR TITLE_ABS:"initial presentation" OR TITLE_ABS:"at presentation" OR TITLE_ABS:"at diagnosis" OR TITLE_ABS:"early diagnosis" OR TITLE_ABS:"diagnostic accuracy" OR TITLE_ABS:sensitivity OR TITLE_ABS:specificity OR TITLE_ABS:"predictive value" OR TITLE_ABS:"primary care" OR TITLE_ABS:"general practice" OR TITLE_ABS:suspicion OR TITLE_ABS:pancytopeni* OR TITLE_ABS:cytopeni* OR TITLE_ABS:aleuk* OR TITLE_ABS:subleuk* OR TITLE_ABS:"clinical features" OR TITLE_ABS:"hematological features" OR TITLE_ABS:"haematological features" OR TITLE_ABS:"hematological findings" OR TITLE_ABS:"haematological findings" OR TITLE_ABS:"hematological abnormalities" OR TITLE_ABS:"laboratory findings" OR TITLE_ABS:"laboratory features" OR TITLE_ABS:"diagnostic delay" OR TITLE_ABS:characteristic* OR TITLE_ABS:profile* OR TITLE_ABS:morpholog* OR TITLE_ABS:epidemiolog*)
```

Distribución por origen dentro de Europe PMC: MEDLINE (MED) 1294, preprints (PPR) 42, PMC 9, Agricola (AGR) 1.

## 4. Ecuaciones preparadas para las fuentes no ejecutadas (pendientes de ejecución)

> Ninguna de estas búsquedas se ha ejecutado. Antes de usarlas, compruebe los descriptores Emtree y DeCS en los tesauros de cada plataforma, porque la sintaxis de los descriptores no se ha podido probar en ellas. Registre la fecha, la plataforma, los filtros y el número de resultados.

### 4.1 Scopus (búsqueda avanzada)

```
TITLE-ABS-KEY("acute leukemia*" OR "acute leukaemia*" OR "acute myeloid leuk*" OR "acute myelogenous leuk*" OR "acute lymphoblastic leuk*" OR "acute lymphocytic leuk*" OR "acute promyelocytic leuk*" OR "acute nonlymphocytic leuk*")
AND TITLE-ABS-KEY("complete blood count*" OR "full blood count*" OR "blood count*" OR cbc OR hemogram* OR haemogram* OR "hematological parameter*" OR "haematological parameter*" OR "peripheral blood smear*" OR "peripheral blood film*" OR "blood film*" OR "blood smear*" OR "peripheral smear*" OR "circulating blast*" OR "peripheral blood blast*" OR "blast flag*" OR "hematology analy*" OR "haematology analy*")
AND TITLE-ABS-KEY("presenting feature*" OR "presenting sign*" OR "presenting symptom*" OR "clinical presentation" OR "initial presentation" OR "at presentation" OR "at diagnosis" OR "early diagnosis" OR "diagnostic accuracy" OR sensitivity OR specificity OR "predictive value*" OR "primary care" OR "general practice" OR suspicion OR pancytopeni* OR cytopeni* OR aleuk* OR subleuk* OR "clinical feature*" OR "hematological feature*" OR "haematological feature*" OR "hematological finding*" OR "haematological finding*" OR "hematological abnormalit*" OR "laboratory finding*" OR "laboratory feature*" OR "diagnostic delay" OR characteristic* OR profile* OR morpholog* OR epidemiolog*)
AND NOT INDEX(medline)
```
*La última línea es opcional: excluye los registros procedentes de MEDLINE, ya captados en PubMed. Si se omite, la deduplicación los eliminará.*

### 4.2 Web of Science Core Collection (búsqueda avanzada)

```
TS=("acute leukemia*" OR "acute leukaemia*" OR "acute myeloid leuk*" OR "acute myelogenous leuk*" OR "acute lymphoblastic leuk*" OR "acute lymphocytic leuk*" OR "acute promyelocytic leuk*" OR "acute nonlymphocytic leuk*")
AND TS=("complete blood count*" OR "full blood count*" OR "blood count*" OR CBC OR hemogram* OR haemogram* OR "hematological parameter*" OR "haematological parameter*" OR "peripheral blood smear*" OR "peripheral blood film*" OR "blood film*" OR "blood smear*" OR "peripheral smear*" OR "circulating blast*" OR "peripheral blood blast*" OR "blast flag*" OR "hematology analy*" OR "haematology analy*")
AND TS=("presenting feature*" OR "presenting sign*" OR "presenting symptom*" OR "clinical presentation" OR "initial presentation" OR "at presentation" OR "at diagnosis" OR "early diagnosis" OR "diagnostic accuracy" OR sensitivity OR specificity OR "predictive value*" OR "primary care" OR "general practice" OR suspicion OR pancytopeni* OR cytopeni* OR aleuk* OR subleuk* OR "clinical feature*" OR "hematological feature*" OR "haematological feature*" OR "hematological finding*" OR "haematological finding*" OR "hematological abnormalit*" OR "laboratory finding*" OR "laboratory feature*" OR "diagnostic delay" OR characteristic* OR profile* OR morpholog* OR epidemiolog*)
```

### 4.3 Embase (Embase.com)

```
#1 'acute leukemia'/exp OR 'acute myeloid leukemia'/exp OR 'acute lymphoblastic leukemia'/exp OR 'acute promyelocytic leukemia'/exp OR ('acute leukemia*' OR 'acute leukaemia*' OR 'acute myeloid leuk*' OR 'acute myelogenous leuk*' OR 'acute lymphoblastic leuk*' OR 'acute lymphocytic leuk*' OR 'acute promyelocytic leuk*' OR 'acute nonlymphocytic leuk*'):ti,ab,kw
#2 'blood cell count'/exp OR 'blood smear'/exp OR 'hematologic analyzer'/exp OR ('complete blood count*' OR 'full blood count*' OR 'blood count*' OR cbc OR hemogram* OR haemogram* OR 'hematological parameter*' OR 'haematological parameter*' OR 'peripheral blood smear*' OR 'peripheral blood film*' OR 'blood film*' OR 'blood smear*' OR 'peripheral smear*' OR 'circulating blast*' OR 'peripheral blood blast*' OR 'blast flag*' OR 'hematology analy*' OR 'haematology analy*'):ti,ab,kw
#3 'early diagnosis'/exp OR 'diagnostic accuracy'/exp OR 'sensitivity and specificity'/exp OR 'differential diagnosis'/exp OR 'delayed diagnosis'/exp OR 'pancytopenia'/exp OR 'primary health care'/exp OR ('presenting feature*' OR 'presenting sign*' OR 'presenting symptom*' OR 'clinical presentation' OR 'initial presentation' OR 'at presentation' OR 'at diagnosis' OR 'early diagnosis' OR 'diagnostic accuracy' OR sensitivity OR specificity OR 'predictive value*' OR 'primary care' OR 'general practice' OR suspicion OR pancytopeni* OR cytopeni* OR aleuk* OR subleuk* OR 'clinical feature*' OR 'hematological feature*' OR 'haematological feature*' OR 'hematological finding*' OR 'haematological finding*' OR 'hematological abnormalit*' OR 'laboratory finding*' OR 'laboratory feature*' OR 'diagnostic delay' OR characteristic* OR profile* OR morpholog* OR epidemiolog*):ti,ab,kw
#4 #1 AND #2 AND #3
#5 #4 NOT ([animals]/lim NOT [humans]/lim)
```
*Opcional: `AND [embase]/lim NOT [medline]/lim` para obtener solo los registros exclusivos de Embase.*

### 4.4 Cochrane Library (búsqueda avanzada; CDSR y CENTRAL)

```
#1 [mh "Leukemia, Myeloid, Acute"] OR [mh "Precursor Cell Lymphoblastic Leukemia-Lymphoma"] OR ("acute leukemia*" OR "acute leukaemia*" OR "acute myeloid leuk*" OR "acute lymphoblastic leuk*" OR "acute promyelocytic leuk*"):ti,ab,kw
#2 [mh "Blood Cell Count"] OR ("complete blood count*" OR "full blood count*" OR "blood count*" OR hemogram* OR haemogram* OR "blood smear*" OR "blood film*" OR "peripheral smear*" OR "circulating blast*" OR "blast flag*"):ti,ab,kw
#3 #1 AND #2
```
*Sin bloque #3 por el bajo volumen previsto; las revisiones Cochrane que aparezcan se usarán según la sección 4.4 del protocolo.*

### 4.5 LILACS (Portal BVS; búsqueda avanzada con DeCS)

```
(mh:"Leucemia Mieloide Aguda" OR mh:"Leucemia-Linfoma Linfoblástico de Células Precursoras" OR mh:"Leucemia Promielocítica Aguda" OR tw:"leucemia aguda" OR tw:"leucemias agudas" OR tw:"leucemia mieloide aguda" OR tw:"leucemia mieloblástica aguda" OR tw:"leucemia linfoblástica aguda" OR tw:"leucemia linfoide aguda" OR tw:"leucemia linfocítica aguda" OR tw:"leucemia promielocítica" OR tw:"acute leukemia")
AND
(mh:"Recuento de Células Sanguíneas" OR mh:"Pruebas Hematológicas" OR tw:hemograma OR tw:"biometría hemática" OR tw:"biometria hematica" OR tw:"citometría hemática" OR tw:"frotis de sangre periférica" OR tw:"frotis sanguíneo" OR tw:"extendido de sangre periférica" OR tw:"esfregaço sanguíneo" OR tw:"esfregaço de sangue periférico" OR tw:"contagem de células sanguíneas" OR tw:"recuento de células sanguíneas" OR tw:blastos OR tw:"parámetros hematológicos" OR tw:"parâmetros hematológicos" OR tw:"complete blood count" OR tw:"blood smear")
AND db:("LILACS")
```
*Sin bloque #3, por el volumen previsiblemente bajo de LILACS.*

### 4.6 SciELO (search.scielo.org; búsqueda avanzada)

```
("leucemia aguda" OR "leucemias agudas" OR "leucemia mieloide aguda" OR "leucemia linfoblástica aguda" OR "leucemia linfoide aguda" OR "leucemia promielocítica" OR "acute leukemia" OR "acute myeloid leukemia" OR "acute lymphoblastic leukemia")
AND
(hemograma OR "biometría hemática" OR "frotis de sangre periférica" OR "frotis sanguíneo" OR "esfregaço sanguíneo" OR "sangue periférico" OR "sangre periférica" OR blastos OR "parámetros hematológicos" OR "parâmetros hematológicos" OR "complete blood count" OR "blood smear" OR "peripheral blood")
```

### 4.7 Google Scholar (complementaria)

```
"acute leukemia" ("complete blood count" OR "peripheral blood smear" OR hemogram OR "blood film") ("at diagnosis" OR presentation OR "early diagnosis")
"leucemia aguda" (hemograma OR "biometría hemática" OR "frotis de sangre periférica") (diagnóstico OR presentación)
```
*Revisar las primeras 200 entradas de cada cadena, ordenadas por pertinencia, y registrar la fecha. No es reproducible y se usará solo para identificar estudios no captados por las bases.*

## 5. Identificación y eliminación de duplicados

| Paso | Registros |
|---|---|
| PubMed | 2798 |
| Europe PMC | 1346 |
| **Total identificado** | **4144** |
| Duplicados eliminados por PMID (registros de Europe PMC ya presentes en PubMed) | 1107 |
| Duplicados eliminados por DOI o por título normalizado más año (preprints con versión publicada, Agricola) | 8 |
| **Total de duplicados eliminados** | **1115** |
| **Registros únicos para cribado** | **3029** |

- Composición de los 3029: 2798 de PubMed; 187 registros MEDLINE que solo recuperó Europe PMC (por diferencias en la indexación del título y el resumen); 35 preprints; 9 registros solo en PMC.
- Los 8 duplicados por DOI o título se listan en la salida de `build.py`: PPR1194488→PMID 41363702, IND608683596→39386823, PPR843397→38789590, PPR816755→39600341, PPR1111905→41282106, PPR1245061→42282795, PPR491528→35501817 y PPR354245→34915860.
- **Registros sin resumen:** 210. Se cribarán por título y, si son dudosos, pasarán a texto completo.
- **Idioma, según MEDLINE:** inglés 2661; chino 83; alemán 64; francés 55; japonés 42; ruso 23; polaco 16; otros o sin dato, el resto. Los no elegibles por idioma se excluirán en el cribado, con su razón registrada, y no se eliminan antes. Así su número queda visible en PRISMA.
- **Rango de años:** 1963–2026.

**Archivos para el cribado:** `etapa2/datos/registros_cribado.{json,csv,ris}`. El archivo RIS se puede importar en Rayyan, Zotero o EndNote, para que la investigadora haga su verificación independiente.

## 6. Datos para el diagrama PRISMA 2020 (bloque de identificación)

| Casilla PRISMA | Valor |
|---|---|
| Registros identificados en bases de datos | PubMed n = 2798; Europe PMC n = 1346; Scopus, WoS, Embase, Cochrane, LILACS y SciELO: **pendiente** |
| Registros identificados en registros (*registers*, p. ej., ClinicalTrials.gov) | No se buscó: no procede para estudios observacionales y diagnósticos |
| Duplicados eliminados | 1115 |
| Registros marcados como no elegibles por herramientas de automatización | 0 (no se usaron) |
| Registros eliminados por otras razones | 0 |
| Registros para cribado | 3029 |
| Otros métodos (búsqueda en listas de referencias, Google Scholar) | **Pendiente** (Etapa 3) |

## 7. Limitaciones de la Etapa 2

1. **Cobertura:** solo se ejecutaron dos fuentes, que se solapan en gran medida con MEDLINE. Faltan Embase (relevante por los resúmenes de congresos de hematología), Scopus y WoS (por las revistas no indizadas en MEDLINE) y, sobre todo, **LILACS y SciELO**, que son clave para la literatura latinoamericana en español y portugués. Esta falta probablemente sesga la revisión hacia publicaciones en inglés.
2. **Bloque #3:** reduce la sensibilidad. La prueba con 200 títulos sugiere una pérdida residual pequeña, pero no nula.
3. **Europe PMC sin MeSH,** por la incidencia técnica descrita en la sección 3.
4. **Un único ejecutor,** sin revisión por pares de la estrategia (PRESS). Se recomienda que la investigadora o un bibliotecario revise las ecuaciones con la lista PRESS 2015.
5. Las búsquedas son reproducibles en la sintaxis, pero no en los recuentos: los índices cambian con el tiempo. Los recuentos corresponden al 05/11/2026.

## 8. Próximo paso (Etapa 3)

Cribado de títulos y resúmenes de los 3029 registros según los criterios del protocolo, con decisión y razón registradas para cada registro. Después, recuperación y evaluación de los textos completos accesibles.
