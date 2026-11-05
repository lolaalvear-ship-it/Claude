# Etapa 4 — Extracción de datos y evaluación metodológica

**Fecha:** 5 de noviembre de 2026 · **Revisor:** asistente de IA (único revisor)

**Archivos generados:**
- `etapa4/matriz_extraccion.xlsx`: matriz de 17 campos con tres hojas (Matriz, JBI prevalencia, QUADAS-2). Hay una versión idéntica en `matriz_extraccion.csv`.
- `etapa4/extraccion_notas.jsonl`: nota de extracción original de cada estudio.
- `etapa4/riesgo_sesgo.json`: juicios de riesgo de sesgo por ítem y por dominio.

## 1. Procedimiento

- **Fuente.** Los datos se extrajeron del texto completo de acceso abierto (XML de PMC o Europe PMC) de los 38 estudios incluidos, revisando los métodos, los resultados y las tablas. No se usó ningún dato procedente solo del resumen.
- **Origen de cada dato.** El campo «Fuente de la información» indica de dónde procede cada dato. Cuando un artículo contiene errores o incoherencias internas, se registran y el dato afectado no se usa en la síntesis:
  - Ahmad 2024: unidades hematológicas imposibles y edad media incompatible con su distribución por grupos.
  - Patel 2021: afirma que todos los pacientes tenían leucocitosis >100 000, lo que contradice la media y la desviación estándar que publica.
  - Jaime-Pérez 2019: unidades mal rotuladas.
- **Sin imputación.** No se imputaron datos. Las proporciones que no venían publicadas y se calcularon a partir de n/N se identifican como «calculadas»; por ejemplo, LA en 10/228 en Ebrahim 2022.
- **Material suplementario.** No se consultó. Esto afecta al menos a Jensen 2025, cuyas cifras de la BH no aparecen en el texto principal.

## 2. Características de los estudios incluidos (n = 38)

| Rasgo | Distribución |
|---|---|
| Año de publicación | 2013–2026 (28 de 38 publicados en 2020 o después) |
| País | India 8, Pakistán 6, China 5, EE. UU. 3, México 2, Dinamarca 2, Francia 2; Indonesia, Irán, Corea del Sur, Italia, Yemen, Arabia Saudí, Tailandia, Etiopía, Qatar y Reino Unido/Nigeria, 1 cada uno. **Ninguno de Sudamérica.** |
| Diseño | Todos observacionales. Predominan los retrospectivos (≈30). Solo hay 1 estudio diagnóstico prospectivo en pacientes con sospecha clínica (Zhang 2025). Los estudios D son de dos grupos (tipo caso-control diagnóstico). |
| Población | Pediátrica exclusiva: 15. Adulta exclusiva o predominante: 6. Mixta: 17. |
| Ámbito | Hospitales terciarios o de referencia: 37 de 38. Ninguno en primer nivel de atención. |
| Tipo de leucemia | LLA: 14. LMA (incluida LPA): 13. Ambas: 9. Linaje ambiguo (LAFM): 1. Neoplasias mixtas con LA como subgrupo: varios. |
| Tamaño | De 15 (Sharma 2017) a 4996 registros (Liao 2026). |

**Tabla resumida.** Cada estudio tiene la matriz completa de 17 campos en el Excel.

| Grupo | Estudio | País | Diseño | n | Tipo de LA | Riesgo de sesgo |
|---|---|---|---|---|---|---|
| D | Agodi 2013 | Italia | Casos y controles retrospectivo | 134 (47 LLA, 71 AIJ) | LLA | Alto |
| D | Park 2016 | Corea | Diagnóstico retrospectivo (carta) | 31 | LPA frente a LMA | Alto |
| D | Brix 2020 | Dinamarca | Dos cohortes independientes | 511 (26 LLA, 485 AIJ) | LLA-B | Alto |
| D | Louvigné 2020 | Francia | Casos y controles 1:2 | 147 (49 LLA, 98 AIJ) | LLA | Alto |
| D | Torres Jiménez 2023 | México | Dos grupos retrospectivo | 76 (14 LLA, 62 AIJ) | LLA | Alto |
| D | Rostikasari 2026 | Indonesia | Transversal analítico | 106 LA | LLA y LMA | Alto |
| D | Mousavi Torshizi 2026 | Irán | Dos grupos retrospectivo | 66 (29 LLA, 37 AIJ) | LLA | Alto |
| F1 | Raja 2015 | India | Comparativo retrospectivo | 44 | LLA | Alto |
| F1 | Sharma 2017 | India | Prospectivo consecutivo | 15 LAFM | LAFM | Moderado |
| F1 | Linu 2017 | India | Serie retrospectiva | 32 | Leucemia eritroide | Moderado |
| F1 | Basharat 2019 | Pakistán | Transversal (conveniencia) | 106 | LMA | Moderado |
| F1 | Jaime-Pérez 2019 | México | Cohorte consecutiva | 203 | LLA-B | Bajo |
| F1 | Patel 2021 | India | Transversal | 68 | LMA y LLA | Alto |
| F1 | Dai 2021 | China | Cohorte retrospectiva | 367 | LLA | Bajo |
| F1 | Kittivisuit 2022 | Tailandia | Cohorte retrospectiva | 1042 | LLA y LMA | Bajo-moderado |
| F1 | Mangum 2023 | EE. UU. | Cohorte (ensayos) | 1003 | LLA | Bajo |
| F1 | Ahmad 2024 | India | Transversal | 147 | LLA | Alto |
| F1 | Alshahrani 2024 | Arabia Saudí | Registro retrospectivo | 210 (BH en 106) | LMA y LLA | Alto |
| F1 | Bobée 2025 | Francia | Comparación de métodos | 87 | LA hiperleucocitaria | Moderado |
| F1 | Jensen 2025 | Dinamarca | Cohorte nacional | 144 | LMA pediátrica | Bajo* |
| F1 | Al-Aghbri 2026 | Yemen | Transversal prospectivo | 75 | LLA y LMA | Moderado |
| F1 | Shome 2026 | India | Transversal | 151 (90 LA) | LLA, LMA, LAFM | Bajo-moderado |
| F2 | Zeb Jan 2013 | Pakistán | Descriptivo retrospectivo | 205 | «Leucemias» | Moderado |
| F2 | Das Makheja 2013 | Pakistán | Transversal | 62 | LMA | Moderado |
| F2 | Zeeshan 2019 | Pakistán | Transversal (conveniencia) | 115 | LLA y LMA | Alto |
| F2 | Alim 2021 | India | Prospectivo | 84 | LLA y LMA | Moderado |
| F2 | Verma 2022 | India | Prospectivo | 100 | LA | Alto |
| F2 | Ebrahim 2022 | Etiopía | Transversal consecutivo | 228 | LMA, LLA | Moderado |
| M | Haider 2020 | Pakistán | Desarrollo de modelo (RNA) | 1067 | LPA | Alto |
| M | Sidhom 2021 | EE. UU. | Modelo con validación temporal | 106 | LPA frente a LMA | Alto |
| M | Haider 2022 | Pakistán | Desarrollo de modelo (RNA) | 1577 | LMA, LPA, LLA | Alto |
| M | Manescu 2023 | Reino Unido/Nigeria | Aprendizaje profundo débil | ~200 frotis | LLA, LMA, LPA | Alto |
| M | Cai 2025 | China | Multicéntrico con validación externa | 2682 | LPA | Alto |
| M | Zhang 2025 | China | **Prospectivo con sospecha clínica** | 192 | LPA | Bajo-moderado |
| M | Alaoui 2026 | Qatar | Modelo con validación temporal | 510 | LMA | Alto |
| M | Liao 2026 | China | Multicéntrico con validación externa | 4996 | LMA, LPA, LLA | Alto |
| M | Singi 2026 | EE. UU. | Frotis digitales completos | 573 | LA | Alto |
| M | Wang 2026 | China | Modelo con validación interna independiente | 422 | LPA | Alto |

\*El riesgo de sesgo de Jensen 2025 es bajo, pero sus datos de la BH no son cuantificables en el texto accesible.

**Informes posiblemente vinculados.** Haider 2020 y Haider 2022 (NIBD, Karachi; 2014–2017 y 2014–2020) comparten centro y periodo. Se tratarán como un solo cuerpo de evidencia y no como dos estudios independientes.

## 3. Evaluación del riesgo de sesgo

### 3.1 Herramientas aplicadas

- **Lista JBI para estudios de prevalencia** (9 ítems): grupos F1 y F2 (21 estudios).
- **QUADAS-2** (4 dominios de riesgo y 3 de aplicabilidad): grupos D y M (17 estudios). Las preguntas de señalización se adaptaron así:
  - En el subgrupo M, la «prueba índice» es el modelo o el analizador.
  - El riesgo en el dominio 2 se consideró alto si el umbral o el modelo se optimizó y evaluó en los mismos datos sin validación independiente.
- No se sumaron puntuaciones. El juicio global se justifica por dominio.

### 3.2 Resultados

| Grupo | Bajo | Bajo-moderado | Moderado | Alto |
|---|---|---|---|---|
| F1 (n = 15) | 4 (Jaime-Pérez, Dai, Mangum, Jensen*) | 2 (Kittivisuit, Shome) | 5 | 4 (Raja, Patel, Ahmad, Alshahrani) |
| F2 (n = 6) | 0 | 0 | 4 | 2 (Zeeshan, Verma) |
| D (n = 7) | 0 | 0 | 0 | **7** |
| M (n = 10) | 0 | 1 (Zhang) | 0 | **9** |

**Patrones de sesgo dominantes:**

1. **Sesgo de espectro (QUADAS-2, dominio 1).** Afecta a 16 de los 17 estudios D y M.
   - Los estudios D comparan LLA con AIJ en dos poblaciones reclutadas por separado (diseño de «dos puertas»).
   - Los estudios M usan con frecuencia controles sanos o de centros oncológicos.
   - Solo Zhang 2025 reclutó de forma consecutiva a pacientes con sospecha clínica.
   - Las sensibilidades y especificidades publicadas son, por tanto, probablemente optimistas.
2. **Verificación diferencial (dominio 4).** En los estudios LLA frente a AIJ, la LLA se confirma con médula ósea, pero la AIJ con criterios clínicos ILAR, sin médula.
3. **Umbrales y modelos optimizados en la misma muestra (dominio 2).** Afecta a Park 2016, Mousavi Torshizi 2026, Torres Jiménez 2023 (el 100 % de clasificación correcta indica sobreajuste), Haider 2020/2022 y Alaoui 2026. En Alaoui 2026 la exactitud cae del 96,4 % al 80 % en la validación temporal.
4. **Sesgo de verificación en las cohortes F2.** Solo se incluyó a pacientes con citopenia remitidos a médula. La proporción de LA observada (4,4–28 %) sobrestima la que se encontraría entre todas las citopenias de un primer nivel de atención.
5. **Calidad del informe.** Cuatro estudios F1 tienen datos incompletos, inconsistentes o mal rotulados (véase la sección 1).
6. **Aplicabilidad.** Todos los estudios proceden de hospitales de referencia y ninguno del primer nivel de atención. La aplicabilidad directa a la pregunta de la sospecha temprana en atención primaria es baja.

## 4. Valoración preliminar de la viabilidad del metaanálisis (criterios del protocolo, sección 10)

| Posible síntesis cuantitativa | Estudios con datos | Criterio del protocolo | Decisión |
|---|---|---|---|
| Proporción de anemia, trombocitopenia o leucopenia en la LLA pediátrica | Jaime-Pérez 2019 y Mangum 2023 (solo el subgrupo sin blastos); Kittivisuit 2022 mezcla LLA y LMA y usa otros umbrales | ≥5 estudios con definiciones compatibles | **No se cumple**: síntesis narrativa |
| Proporción de LA sin blastos en SP | Mangum 2023 (14,7 %), Kittivisuit 2022 (10,2 %, LA mixta), Dai 2021 (20,4 %, «sin blastos») | ≥5 | **No se cumple** (3 estudios, definiciones distintas) |
| Exactitud de la neutropenia o la trombocitopenia para LLA frente a AIJ | Brix 2020 (<1,0), Torres Jiménez 2023 (<1,5), Agodi 2013 (umbral institucional), Louvigné 2020 (<2,0; solo OR), Mousavi Torshizi 2026 (medianas) | ≥4 con umbral comparable y tablas 2×2 | **No se cumple** (umbrales distintos; 2×2 reconstruibles solo en 3; diseño de dos puertas) |
| Proporción de LA entre las pancitopenias | 5 estudios F2 | ≥5 con población comparable | **No procede**: mezclan edades y criterios, y el sesgo de verificación es alto. Se presentarán como rango. |
| Modelos de IA | 10 | Modelos, analizadores y clases heterogéneos | **No procede** |

**Conclusión:** no hay datos suficientemente homogéneos para un metaanálisis. La Etapa 5 usará una síntesis narrativa estructurada (SWiM), con tablas por grupo y rangos.

## 5. Limitaciones de la Etapa 4

1. Extracción y evaluación por un solo revisor, sin doble extracción.
2. No se consultó el material suplementario de los artículos.
3. Los juicios JBI y QUADAS-2 implican una interpretación. Están registrados ítem por ítem para que la investigadora pueda auditarlos y discrepar.
4. Los 133 informes no recuperados (Etapa 3) siguen sin evaluar.
