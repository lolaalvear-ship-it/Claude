## Anexo A. Ecuaciones de búsqueda

**Ejecutadas el 5 de noviembre de 2026.** Las ecuaciones exactas, sin saltos de línea, están en:
- `etapa2/datos/pubmed_final_query.txt`: PubMed, 2798 registros.
- `etapa2/datos/epmc_final_query.txt`: Europe PMC, 1346 registros.

**Pendientes de ejecución.** La sección 4 de `etapa2_busqueda.md` contiene las ecuaciones de Scopus, Web of Science, Embase, Cochrane Library, LILACS (DeCS), SciELO y Google Scholar.

**Estructura de la estrategia de PubMed:**
- **#1 Leucemia aguda.** MeSH: *Leukemia, Myeloid, Acute*; *Precursor Cell Lymphoblastic Leukemia-Lymphoma*; *Leukemia, Promyelocytic, Acute*. Más variantes en título y resumen.
- **#2 BH o frotis.** MeSH: *Blood Cell Count*; *Hematologic Tests* [noexp]. Más términos de título y resumen: complete/full blood count, CBC, hemogram, hematological parameters, peripheral blood smear/film, blood film/smear, circulating blasts, blast flag, hematology analyzer.
- **#3 Presentación o diagnóstico.** MeSH: *Early Diagnosis*; *Sensitivity and Specificity*; *Diagnosis, Differential*; *Delayed Diagnosis*; *Pancytopenia*; *Primary Health Care*; subencabezamientos */diagnosis*. Más términos de título y resumen: presenting features, at diagnosis, diagnostic accuracy, primary care, cytopeni*, aleuk*, characteristic*, profile*, morpholog*, epidemiolog*, y otros.
- **Combinación:** (#1 AND #2 AND #3) NOT (animals[mh] NOT humans[mh]).

## Anexo B. Diagrama de flujo PRISMA 2020

Véanse `diagrama_prisma.svg` y `diagrama_prisma.png`.

## Anexo C. Matriz de extracción

La matriz completa de 17 campos, con el origen de cada dato, está en `etapa4/matriz_extraccion.xlsx` (hoja «Matriz»). Los juicios de riesgo de sesgo por ítem están en las hojas «JBI prevalencia» y «QUADAS-2».

## Anexo E. Lista de verificación PRISMA 2020

C = cumplido · P = parcial · N = no cumplido. La «sección» remite al manuscrito, salvo que se indique otro documento.

| N.º | Ítem | Sección | Estado | Observaciones |
|---|---|---|---|---|
| 1 | Título | Título | C | Se identifica como revisión sistemática |
| 2 | Resumen estructurado | Resumen | C | — |
| 3 | Justificación | 1–2 | C | — |
| 4 | Objetivos | 3 | C | Formato PIRD |
| 5 | Criterios de elegibilidad | 4 | C | Detalle en la Etapa 1 |
| 6 | Fuentes de información | 4–5 | P | Solo se ejecutaron 2 de 8 bases; fecha declarada; 6 pendientes |
| 7 | Estrategia de búsqueda | 5, anexo A | C | Ecuaciones completas y reproducibles |
| 8 | Proceso de selección | 4 | P | Un único revisor (IA), sin doble revisión independiente |
| 9 | Proceso de extracción | 4 | P | Un único revisor; sin contacto con los autores |
| 10a | Desenlaces buscados | 4; Etapa 1 | C | — |
| 10b | Otras variables | Etapa 1, sección 8 | C | — |
| 11 | Riesgo de sesgo de los estudios | 4, 8 | P | JBI y QUADAS-2 por un único revisor |
| 12 | Medidas del efecto | 4, 9 | C | Proporciones, sensibilidad, especificidad, CP, OR, AUC según los estudios |
| 13a | Elegibilidad para la síntesis | 4; Etapa 4, sección 4 | C | — |
| 13b | Preparación de los datos | Etapa 4, sección 1 | C | Sin imputación; los datos incoherentes se excluyen |
| 13c | Tabulación y presentación | 7, 9 | C | — |
| 13d | Método de síntesis | 4 | C | SWiM; metaanálisis no viable y justificado |
| 13e | Exploración de la heterogeneidad | 9–10 | P | Narrativa (por edad, linaje y entorno) |
| 13f | Análisis de sensibilidad | — | N | No procede sin metaanálisis |
| 14 | Sesgo de notificación | 11 | P | Valoración cualitativa; sin gráfico en embudo |
| 15 | Certeza de la evidencia | 10 | P | Juicio estructurado con la lógica GRADE, no GRADE formal |
| 16a | Resultados de la selección | 6, anexo B | C | — |
| 16b | Estudios excluidos y motivos | 6; Etapa 3 | C | Lista completa en `texto_completo.csv` |
| 17 | Características de los estudios | 7, anexo C | C | — |
| 18 | Riesgo de sesgo de los estudios | 8, anexo C | C | — |
| 19 | Resultados individuales | 9, anexo C | C | — |
| 20a | Características de las síntesis | 9 | C | — |
| 20b | Resultados de las síntesis | 9 | C | Rangos narrativos, no estimaciones combinadas |
| 20c | Heterogeneidad | 9–10 | P | Narrativa |
| 20d | Sensibilidad | — | N | No procede |
| 21 | Sesgo de notificación | 11 | P | Cualitativo |
| 22 | Certeza | 10 | P | Véase el ítem 15 |
| 23a | Interpretación | 10 | C | — |
| 23b | Limitaciones de la evidencia | 10–11 | C | — |
| 23c | Limitaciones del proceso | 11 | C | — |
| 23d | Implicaciones | 12 | C | — |
| 24a | Registro | Portada | N | No registrada |
| 24b | Protocolo | Etapa 1 | C | Accesible en el repositorio |
| 24c | Enmiendas al protocolo | Etapa 2, sección 2.2 | C | Ampliación del bloque 3 de búsqueda; Europe PMC sin MeSH |
| 25 | Financiación | — | C | Sin financiación; ejercicio académico |
| 26 | Conflictos de interés | — | C | Ninguno declarado |
| 27 | Disponibilidad de datos y código | Repositorio | C | Registros, decisiones, scripts y matriz disponibles |
