# Etapa 3 — Depuración, cribado y selección de estudios

**Fecha:** 5 de noviembre de 2026 · **Revisor:** asistente de IA (único revisor; desviación declarada en el protocolo, sección 12)
**Registros de entrada:** 3029 registros únicos procedentes de la Etapa 2 (PubMed y Europe PMC).
**Archivos de trazabilidad:**
- `etapa3/cribado_titulo_resumen.csv`: los 3029 registros, con la decisión tomada en el título y, cuando corresponde, la decisión y la razón en el resumen.
- `etapa3/texto_completo.csv`: los 224 registros que superaron el cribado, con su estado (incluido, excluido con razón, no recuperado, anexo) y un enlace verificable.
- `etapa3/excluidos_idioma.json`: identificadores de los registros excluidos por idioma.

---

## 1. Procedimiento aplicado

| Paso | Procedimiento | Criterio |
|---|---|---|
| 1. Idioma | Exclusión automática a partir del campo de idioma de MEDLINE o Europe PMC. No hay juicio de contenido. | Elegibles: inglés, español y portugués. Los registros sin idioma (35) pasaron al cribado. |
| 2. Título | Lectura de los 2717 títulos restantes en 10 bloques. Se clasificaron como «pasa» o «excluido». Los que pasaron se etiquetaron como P (estudio primario potencial), A (reporte de caso con presentación atípica, para el anexo), M (algoritmo o IA sobre BH o frotis) o S (revisión sistemática). | Ante la duda, el registro pasa. |
| 3. Resumen | Lectura de los resúmenes de los 270 títulos seleccionados (truncados a unos 950 caracteres; 18 no tenían resumen y pasaron por defecto). | Criterios del protocolo, sección 4. Se registró una razón por cada exclusión. |
| 4. Recuperación del texto completo | Europe PMC (`fullTextXML`) y PMC (E-utilities). | Solo texto completo de acceso abierto. Las demás plataformas editoriales no son accesibles desde el entorno. |
| 5. Elegibilidad en texto completo | Revisión de métodos, resultados y tablas de cada informe recuperado. | Una razón principal de exclusión por informe, según la jerarquía del protocolo. |

**Advertencia metodológica.** El cribado lo hizo un solo revisor, y en el paso del título la decisión se basó únicamente en el enunciado. Se recomienda que la investigadora revise de forma independiente una muestra aleatoria del 20 % de `cribado_titulo_resumen.csv` y todos los registros marcados como «pasa a resumen», y que calcule el coeficiente kappa.

## 2. Resultados del cribado

| Fase | n |
|---|---|
| Registros cribados | 3029 |
| Excluidos por idioma no elegible | 312 (chino 83, alemán 64, francés 55, japonés 42, ruso 23, polaco 16, otros 29) |
| Excluidos por título | 2447 |
| Excluidos en el resumen | 46 |
| **Registros que superan el cribado** | **224** |
| — Informes de estudios primarios para buscar el texto completo | 179 |
| — Reportes de caso para el anexo descriptivo | 44 |
| — Revisión sistemática de contraste | 1 (PMID 36454343) |

**Razones de exclusión en el resumen (n = 46):**
- Sin datos de BH o frotis al diagnóstico, o con un objetivo no pertinente: 25. Incluye estudios moleculares, citogenéticos y pronósticos; estudios de seguimiento o postratamiento; estudios con la prueba índice en médula ósea o en LCR; y estudios de deformabilidad eritrocitaria o estado férrico.
- Series de menos de 10 pacientes: 5.
- Población no elegible (SMD, mastocitosis, linfoma u otras sin LA): 6.
- Reporte de caso fuera del anexo, revisión narrativa o capítulo de libro: 5.
- Duplicados detectados durante el cribado (preprint con su versión publicada): 3.
- Sin datos de BH en un reporte de caso: 2.

El desglose de cada registro está en `cribado_titulo_resumen.csv`.

## 3. Recuperación y elegibilidad en texto completo

| Fase | n |
|---|---|
| Informes buscados para recuperación | 179 |
| **Informes no recuperados** | **133** (de ellos, 10 están indizados en PMC sin cuerpo de texto disponible; los demás están en plataformas editoriales no accesibles desde el entorno o no tienen versión electrónica) |
| Informes evaluados en texto completo | 46 |
| Excluidos en texto completo | 8 |
| **Estudios incluidos** | **38** |

**Exclusiones en texto completo (n = 8):**

| Registro | Razón principal |
|---|---|
| Elendu 2026, PMID 42967073 (LPA: rasgos clínicos y morfológicos) | Diseño: reporte de un solo caso |
| Muthukumaran 2026, PMID 42907972 (ClinNetDx) | Datos no clínicos o no verificables: conjunto de BH «inspirado» en un repositorio público e imágenes de Kaggle |
| Yan 2026, PMID 41848210 | Prueba índice no elegible (citometría de flujo de leucocitos) |
| Iddy 2024, PMID 39816383 (GSM frente a WSI) | Prueba índice en médula ósea, no en sangre periférica |
| Ahmad N 2024, PMID 38487155 | Prueba índice principal en médula ósea |
| Lu 2022, PMID 38358601 | Datos de LA no separables de otras neoplasias mieloides |
| Qiao 2021, PMID 34359320 | Validación técnica en bancos públicos de imágenes, sin cohorte diagnóstica |
| Choccalingam 2018, PMID 29403212 | Solo 2 pacientes con LA |

## 4. Estudios incluidos (n = 38), agrupados según la pregunta del protocolo

**F1 — Frecuencia de alteraciones de la BH o el FSP en LA confirmada (n = 15)**

| Estudio | Tema | PMID |
|---|---|---|
| Raja 2015 | LLA pediátrica con y sin pancitopenia | 25992344 |
| Sharma 2017 | LA de fenotipo mixto (n = 15) | 28639598 |
| Linu 2017 | Leucemia eritroide aguda (n = 32) | 28144286 |
| Basharat 2019 | LMA (n = 106): BH y morfología frente a citometría | 31086535 |
| Jaime-Pérez 2019 | BH al diagnóstico de la LLA infantil (n = 203) | 30793106 |
| Patel 2021 | Perfil clinicopatológico de la LA (n = 68) | 33973643 |
| Dai 2021 | LLA pediátrica con recuento bajo de blastos periféricos (n = 367) | 33530278 |
| Kittivisuit 2022 | Leucemia infantil con afectación musculoesquelética (n = 1042) | 35501817 |
| Mangum 2023 | LLA sin blastos periféricos al diagnóstico (n = 1003) | 36352514 |
| Ahmad 2024 | LLA en el norte de India (n = 147) | 38883069 |
| Alshahrani 2024 | Neoplasias hematológicas en Arabia Saudí (n = 210) | 38438211 |
| Bobée 2025 | Pseudoplaquetas por fragmentos de blastos en LA hipercelular (n = 87) | 40165766 |
| Jensen 2025 | LMA pediátrica nacional en Dinamarca (n = 144) | 39295289 |
| Al-Aghbri 2026 | Morfología frente a citometría en Yemen (n = 75) | 42762201 |
| Shome 2026 | Perfil clinicohematológico en Jharkhand (n = 151; 90 con LA) | 42147558 |

**F2 — Proporción de LA en cohortes no seleccionadas con citopenias (n = 6).** Estos estudios no informan de la exactitud diagnóstica de la BH, pero aproximan con qué frecuencia una citopenia corresponde a una LA.

| Estudio | Tema | PMID |
|---|---|---|
| Zeb Jan 2013 | Pancitopenia pediátrica (n = 205) | 24353710 |
| Das Makheja 2013 | Pancitopenia en adultos (n = 62) | 24353701 |
| Zeeshan 2019 | Pancitopenia pediátrica (n = 115) | 31523555 |
| Alim 2021 | Pancitopenia pediátrica (n = 84) | 34249535 |
| Verma 2022 | Trombocitopenia (n = 100) | 36654609 |
| Ebrahim 2022 | Parámetros hematológicos anormales con estudio de médula ósea (n = 228) | 35210892 |

**D — Exactitud diagnóstica o comparación con un grupo sin LA (n = 7)**

| Estudio | Tema | PMID |
|---|---|---|
| Agodi 2013 | Neoplasia frente a AIJ, sin blastos en el frotis | 23368751 |
| Park 2016 | CPD del Sysmex XN para distinguir LPA de otras LMA (carta con datos) | 27578517 |
| Brix 2020 | LLA con artritis frente a AIJ | 32780759 |
| Louvigné 2020 | LLA frente a AIJ con dolor osteoarticular persistente | 31898528 |
| Torres Jiménez 2023 | Artritis leucémica frente a AIJ, sin blastos | 37259088 |
| Rostikasari 2026 | Escatergrama gris del analizador frente a frotis | 42699297 |
| Mousavi Torshizi 2026 | LLA frente a AIJ, sin blastos en sangre periférica | 41877088 |

**M — Subgrupo de algoritmos o IA basados en la BH o en imágenes del frotis (n = 10)**
- Haider 2020 (31733590) y Haider 2022 (35054304).
- Sidhom 2021 (33990660).
- Manescu 2023 (36781917).
- Cai 2025 (41204132).
- Zhang 2025 (40260295).
- Alaoui 2026 (42553493).
- Liao 2026 (42421054).
- Singi 2026 (41981246).
- Wang 2026 (41975751).

**Cohortes posiblemente solapadas, que deben verificarse en la Etapa 4:** Haider 2020 y Haider 2022 proceden del mismo instituto de Karachi, con periodos 2014–2017 y 2014–2020. Si se confirma el solapamiento, se contarán como un solo estudio con dos informes.

## 5. Anexo de reportes de caso (n = 44)

Se identificaron 44 reportes y series de menos de 10 casos con presentaciones atípicas: BH normal, ausencia de blastos circulantes, pancitopenia o pródromo aplásico, o simulación de otras entidades (déficit de vitamina B12, agranulocitosis, LLC, eosinofilia, PTT, mononucleosis). Hay texto completo abierto de 16; los otros 28 solo se conocen por el título o el resumen. Se usarán exclusivamente como evidencia de que estas presentaciones son posibles (protocolo, sección 4.3).

## 6. Revisiones sistemáticas de contraste y búsqueda por otros métodos

- **Identificada en la búsqueda:** PMID 36454343, una revisión sistemática de manifestaciones osteoarticulares de la LLA en adultos basada en casos.
- **Identificada por otros métodos:** Clarke RT et al., *Arch Dis Child* 2016;101(10):894-901, doi:10.1136/archdischild-2016-311251, PMID 27647842. Es una revisión sistemática con metaanálisis de la presentación clínica de la leucemia infantil (33 estudios). **Nuestra estrategia no la recuperó**, porque se centra en signos y síntomas y no menciona términos de BH en el título ni en el resumen.
  - Implicación para la sensibilidad de la búsqueda: los estudios de «características de presentación» que solo informan de la BH en las tablas del texto completo pueden haber quedado fuera.
  - Medida correctora prevista: revisar las listas de referencias de esta revisión y de los estudios incluidos (búsqueda hacia atrás). Está **pendiente**, porque el texto completo de Clarke 2016 no es accesible desde el entorno.

## 7. Datos para el diagrama PRISMA 2020

```
IDENTIFICACIÓN
  Registros de bases de datos: PubMed 2798 · Europe PMC 1346 (total 4144)
  Scopus / WoS / Embase / Cochrane / LILACS / SciELO: [pendiente]
  Eliminados antes del cribado: duplicados 1115 · automatización 0 · otros 0
  Otros métodos: 1 revisión sistemática de contraste (Clarke 2016) · búsqueda en referencias [pendiente]

CRIBADO
  Registros cribados: 3029
    → Excluidos: 2805 (idioma 312 · título 2447 · resumen 46)
  Informes buscados para recuperación: 179 (+ 44 reportes de caso para el anexo)
    → No recuperados: 133
  Informes evaluados para elegibilidad: 46
    → Excluidos: 8 (caso único 1 · datos no verificables 1 · prueba índice no elegible 3 ·
       datos no separables 1 · validación técnica 1 · n<10 1)

INCLUIDOS
  Estudios incluidos en la revisión: 38 (F1 15 · F2 6 · D 7 · M 10)
  Anexo descriptivo de reportes de caso: 44 (16 con texto completo)
```

## 8. Limitaciones de la Etapa 3 y datos pendientes

1. **Pérdida de informes por falta de acceso (133 de 179; 74 %).** Es la limitación más importante de toda la revisión. Afecta sobre todo a estudios anteriores a 2010 (87 de los 133), entre ellos varios que, por el resumen, parecen centrales para la pregunta:
   - Detección de LA mediante criterios automatizados y revisión del frotis: Rabizadeh 2015, PMID 24702792.
   - LLA infantil sin afectación de las tres series: Brix 2014, PMID 25162442.
   - LA con plaquetas normales: Hara 1990, PMID 2284928.
   - Dolor óseo con índices casi normales: Jonsson 1990, PMID 2380822.
   - Alertas del Coulter STKS: Hoyer 1996, PMID 8816593.
   - Alertas del Technicon H-1: Fernández-Castro 1995, PMID 7725855.
   - Estudio de casos y controles LLA frente a AIR: Jones 2006, PMID 16651289.
   - Registro francés de hemogramas: 1987, PMID 3476180.
   - Características de presentación de la LA del adulto según FAB: Burns 1981, PMID 6944140.
   - Signos de alarma de la LLA: Bernbeck 2009, PMID 19890789.
   - Presentación ortopédica con frotis normal: Raj 2020, PMID 32675920.
   - Monocitopenia como pista diagnóstica: Park 2014, PMID 24804826.
   - Presentación en urgencias: Kashiwa 2026, PMID 42385662.
   - Estudio en atención primaria con historias electrónicas: Shephard 2016, PMID 26917658.
   - Gran cohorte mexicana: Gómez-Almaguer 2017, PMID 27742477.

   **No se ha extraído ningún dato de estos informes**, y no se incluirán con datos del resumen en la síntesis principal. La lista completa, con PMID y DOI, está en `etapa3/texto_completo.csv` (estado «no recuperado»). Si la investigadora obtiene los PDF mediante su biblioteca, se evaluarán con los mismos criterios.
2. **Sesgo hacia literatura reciente y de acceso abierto.** Los 38 incluidos tienen una mediana de publicación de 2022 y una proporción alta de revistas de acceso abierto de India, Pakistán y China. Esto afecta a la aplicabilidad.
3. **Un único revisor,** con cribado de títulos basado solo en el enunciado.
4. **Búsqueda en referencias** (hacia atrás y hacia delante) aún no realizada.
5. **Bases pendientes de la Etapa 2** (Scopus, WoS, Embase, LILACS, SciELO): sus registros, si se aportan, se cribarán con el mismo procedimiento.

## 9. Próximo paso (Etapa 4)

Extraer los datos de los 38 estudios incluidos en la matriz de 17 campos, marcando el origen de cada dato, y evaluar el riesgo de sesgo con QUADAS-2 (grupos D y M) y las listas JBI de prevalencia o de series de casos (grupos F1 y F2).
