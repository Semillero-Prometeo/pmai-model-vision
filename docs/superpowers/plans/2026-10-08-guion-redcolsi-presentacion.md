# Guion REDCOLSI 7 min y presentación Canva Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Entregar un guion conversacional de 7:00 para REDCOLSI (Johel fases 1–2 + demo CNN; Juan fases 3 + demo) y una presentación Canva de 11 slides Unilibre alineada a ese guion.

**Architecture:** El markdown `docs/guion-redcolsi-7min.md` es la fuente de verdad del habla, cues y plan B. La presentación se genera en Canva como diseño **nuevo** (no se pisan `DAHXcArwx2g` ni `DAHVITCFNFc`). Por marca Universidad Libre se usa `generate-design` + `create-design-from-candidate`, no `create-design`. Al cierre, la URL de edición se anexa al markdown.

**Tech Stack:** Markdown en el repo; Canva MCP (`plugin-canva-canva`); paleta Unilibre; assets del Canva Prometeo o marcos etiquetados; gráficas locales solo si hace falta (`runs/detect/train5`).

## Global Constraints

- Duración hablada + demos = 7:00. Demo CNN ~45 s (Johel, slide 7). Demo fase 3 ~80 s (Juan, slide 9).
- Voces: Johel Santiago Arias Becerra = fases 1 y 2 + objetivos de objetos + referente + Scrum + métricas + pase. Juan Manuel Toro Grajales = problema R-ONE + objetivos CLAUD-IA/evaluar + ping metodología + fase 3 + cierre prototipo.
- Métricas oficiales (solo Resultados, nunca Conclusiones del paper): precisión 0.8486 (se dice “cero ochenta y cinco”), recall 0.9474 (“cero noventa y cinco”), mAP50 0.9942 (“cero noventa y nueve”), mAP50-95 0.8677 (“cero ochenta y siete”), 60 épocas. En slides se muestran 0.85 / 0.95 / 0.99 / 0.87.
- 11 diapositivas 16:9. Paleta de trabajo: rojo `#C8102E`, oro `#FDB913`, blanco `#FFFFFF`, carbón `#2B2B2B`. Brand kit Canva `kAHAXAjmnKs` pisa esos hex si trae muestras.
- Título Canva exacto: `REDCOLSI 2026 — Visión artificial Prometeo (7 min)`.
- No reescribir `docs/proyecto-completo.md`. No editar `docs/proyecto-conversacional.md`. No pisar Canva de referencia. No coreografiar demos. No preguntas de jurado en los 7 min. No citas de papers en slides. No neon. No QR.
- Quien habla avanza su slide, salvo pase Johel→Juan (Johel deja la 7; Juan abre la 8). El ping de Juan en metodología no cambia de slide.
- Demos: cue de entrada + detalle libre + frase de respaldo. No reiniciar software en escena.

## File Structure

- Create: `docs/guion-redcolsi-7min.md` — libreto oficial (tiempos, texto, cues, plan B, URL Canva al final).
- Read-only: `docs/superpowers/specs/2026-10-08-guion-redcolsi-presentacion-design.md`, `docs/proyecto-completo.md`, `docs/proyecto-conversacional.md`.
- Read-only Canva: `DAHXcArwx2g`, `DAHVITCFNFc`.
- Create (Canva, fuera del repo): diseño nuevo de 11 páginas.
- Optional read: `runs/detect/train5/val_batch0_pred.jpg`, `runs/detect/train5/results.png`.

---

### Task 1: Escribir el guion conversacional

**Files:**
- Create: `docs/guion-redcolsi-7min.md`
- Test: comprobaciones `rg` sobre ese archivo (el archivo aún no existe → fallan)

**Interfaces:**
- Consumes: spec `docs/superpowers/specs/2026-10-08-guion-redcolsi-presentacion-design.md` secciones 4–6, 8–10
- Produces: markdown con anclas `## Reloj`, `## Beat`, `**JOHEL:**`, `**JUAN:**`, cues `[SLIDE n]`, `[DEMO CNN]`, `[DEMO FASE 3]`, `[PLAN B CNN]`, `[PLAN B FASE 3]`, y bloque `## Reserva para jurado` que no se habla en los 7 min

- [ ] **Step 1: Correr las comprobaciones sobre un archivo que aún no existe**

En la raíz del repo:

```powershell
rg -n "cero ochenta y cinco" docs/guion-redcolsi-7min.md
rg -n "\[DEMO CNN\]" docs/guion-redcolsi-7min.md
rg -n "\[DEMO FASE 3\]" docs/guion-redcolsi-7min.md
rg -n "0\.82" docs/guion-redcolsi-7min.md
```

Expected: las tres primeras fallan con error de archivo no encontrado (o 0 matches). La cuarta también 0 matches — se volverá a correr al final para garantizar que **no** aparezcan las cifras de Conclusiones.

- [ ] **Step 2: Crear `docs/guion-redcolsi-7min.md` con este contenido exacto**

```markdown
# Guion REDCOLSI — 7 minutos

**Evento:** REDCOLSI / encuentro de semilleros  
**Proyecto:** Desarrollo de un modelo de IA y visión artificial para reconocimiento automático de objetos en entornos reales  
**Semillero:** Prometeo — Universidad Libre, seccional Bogotá, sede Bosque Popular  
**Expositores:** Johel Santiago Arias Becerra (fases 1 y 2) y Juan Manuel Toro Grajales (fase 3)

Este archivo es el libreto oficial. El texto bajo **JOHEL** / **JUAN** es sugerido (académico hablado). Son rígidos: números, pases y cues de demo. No leer párrafos. Preguntas del jurado quedan fuera de los 7:00.

Presentación Canva: _pendiente de URL (Task 5)_.

## Reloj

| Tiempo | Quién | Beat | Slide |
|---|---|---|---|
| 0:00–0:40 | Ambos | Portada y problema | 1 → 2 |
| 0:40–1:25 | Ambos | Objetivos | 3 |
| 1:25–1:50 | Johel | Referente técnico | 4 |
| 1:50–2:15 | Johel + pase de Juan | Scrum y tres fases | 5 |
| 2:15–2:55 | Johel | Fases 1 y 2 + métricas | 6 → 7 |
| 2:55–3:40 | Johel | Demo CNN | 7 se queda |
| 3:40–3:55 | Pase | Entrega a personas y prototipo | 8 |
| 3:55–5:10 | Juan | Fase 3 | 8 → 9 |
| 5:10–6:30 | Juan | Demo fase 3 | 9 se queda |
| 6:30–7:00 | Ambos | Conclusiones y cierre | 10 → 11 |

Si una demo se alarga, se recorta el cierre. No se recortan objetivos, métricas ni el pase Johel → Juan. Si Johel se pasa en la demo CNN, Juan recorta la explicación de fase 3, no la demo 3, salvo que queden menos de 90 s totales.

Corte de tiempo, en este orden: (1) cierre a una frase cada uno; (2) detalle del referente; (3) detalle de servos / cuello / repertorio.

## Beat 1 — Apertura (0:00–0:40)

[SLIDE 1] Johel avanza a [SLIDE 2] cuando Juan empieza el problema.

**JOHEL:** Muy buenos días. El día de hoy, junto a mi compañero Juan Manuel Toro Grajales y yo, Johel Santiago Arias, integrantes del semillero Prometeo, presentamos el proyecto Desarrollo de un modelo de IA y visión artificial para reconocimiento automático de objetos en entornos reales.

**JUAN:** Actualmente la Universidad Libre de Colombia, en la seccional Bogotá, sede Bosque Popular, cuenta con un androide de propósito general denominado R-ONE. Va a interactuar con visitantes y miembros de la universidad y a orientar procesos internos y administrativos. Hoy el androide no reconoce objetos ni atributos de las personas que se cruzan con él; sin eso la interacción se queda corta. Toda integración de visión la certificamos antes en el prototipo homólogo CLAUD-IA.

**JOHEL:** Por eso el trabajo se organizó en tres fases. Hoy vamos a ver el modelo y el prototipo.

## Beat 2 — Objetivos (0:40–1:25)

[SLIDE 3]

**JOHEL:** El objetivo general fue desarrollar un modelo de IA y visión artificial para el reconocimiento automático de objetos y personas en entornos reales. En las dos primeras fases nos concentramos en los objetos: analizar las técnicas actuales de reconocimiento y sus limitaciones en entornos reales, y desarrollar un modelo basado en redes neuronales convolucionales, entrenarlo y dejarlo medible.

**JUAN:** Del lado del prototipo, implementar ese modelo en CLAUD-IA a través de la creación de la cabeza, y evaluarlo en escenarios reales para medir precisión y eficiencia —ya no solo sobre objetos, también sobre personas.

## Beat 3 — Referente técnico (1:25–1:50)

[SLIDE 4]

**JOHEL:** En la literatura de visión artificial con CNN, el flujo consolidado parte de un dataset propio, sigue con preprocesamiento y aumento de datos, y recién entonces el entrenamiento. Trabajos con CNN personalizadas sobre datasets heterogéneos usan redimensionado, normalización y augmentation —rotación, volteo y color— para ganar robustez. Ese fue nuestro marco para las fases 1 y 2.

## Beat 4 — Metodología (1:50–2:15)

[SLIDE 5] Johel no cambia de slide cuando habla Juan.

**JOHEL:** El proceso fue investigación-desarrollo, organizado con Scrum: un sprint por fase. El dataset es propio: 802 imágenes, 25 clases, capturadas con celular, etiquetadas a mano con bounding boxes YOLO, y partidas ochenta, diez y diez entre entrenamiento, validación y prueba.

**JUAN:** En paralelo, en el prototipo ya montábamos la percepción de personas.

## Beat 5 — Fases 1 y 2 (2:15–2:55)

[SLIDE 6] al hablar de fase 1. [SLIDE 7] al hablar de fase 2 y métricas.

**JOHEL:** La fase 1 fue el desarrollo propio de un modelo de visión por computador para objetos en entornos reales, fundamentado en redes neuronales convolucionales profundas y entrenado con YOLO.

En la fase 2 mejoramos ese modelo con preprocesamiento, estandarización, data augmentation fotométrica y geométrica, y más datos. En sesenta épocas las pérdidas de entrenamiento y validación bajaron sin signos de sobreajuste. El modelo quedó en precisión cero ochenta y cinco, recall cero noventa y cinco, mAP50 cero noventa y nueve, y mAP50-95 cero ochenta y siete.

## Beat 6 — Demo CNN (2:55–3:40)

[SLIDE 7 se queda]

**JOHEL:** Mejor que contarlo, lo mostramos.

[DEMO CNN] Johel muestra el funcionamiento del detector. El detalle es libre. No narrar librerías ni hiperparámetros.

[PLAN B CNN] Si la demo falla: “El detector localiza objetos en cámara; las métricas que acaban de ver corresponden a ese modelo.” Pasa de inmediato a Juan. No se reinicia el software en escena.

## Beat 7 — Pase (3:40–3:55)

Juan abre [SLIDE 8].

**JOHEL:** Eso es el modelo de objetos. El siguiente paso es que el androide reconozca personas.

## Beat 8 — Fase 3 (3:55–5:10)

[SLIDE 8] pipeline. [SLIDE 9] al nombrar CLAUD-IA.

**JUAN:** En la fase 3 el modelo de visión combina cuatro componentes en un solo ciclo. Detectamos y localizamos rostros, incluso con varias personas en escena. Sobre el rostro distinguimos si es alguien conocido o desconocido. En paralelo leemos el estado emocional —alegría, tristeza, enojo, sorpresa, miedo, disgusto o neutro— e interpretamos gestos de mano: palma abierta, puño o pulgar arriba.

Todo eso vive en CLAUD-IA: calibramos catorce servomotores faciales, el cuello sigue a la persona, y hay un repertorio de gestos de emoción, saludo y atención, sincronizados con cabeza y torso. Se prueba en el homólogo antes de subir a R-ONE.

## Beat 9 — Demo fase 3 (5:10–6:30)

[SLIDE 9 se queda]

**JUAN:** Y esto es el funcionamiento.

[DEMO FASE 3] Juan muestra rostro, emoción y/o gesto. El detalle es libre.

[PLAN B FASE 3] Si la demo falla: “El ciclo detecta rostro, emoción y gesto, y mueve la cabeza de CLAUD-IA.” Salta a conclusiones. Prototipo a postura neutra. No se culpa al hardware.

**JUAN:** Lo que acaban de ver es percepción y actuación en el mismo ciclo.

## Beat 10 — Cierre (6:30–7:00)

[SLIDE 10] conclusiones. [SLIDE 11] agradecimiento.

**JOHEL:** En conjunto, el entrenamiento fue exitoso: el modelo quedó con un equilibrio adecuado entre precisión y recall, robusto y usable en entorno real.

**JUAN:** Y eso nos permitió explorar caras, emoción y gesto sobre el prototipo.

**JOHEL:** Por ello, Juan Manuel y yo, junto al semillero de investigación Prometeo y la Universidad Libre, agradecemos el espacio y la oportunidad.

## Ensayo

Cronómetro de 7:00, slides reales, ambas demos en el mismo orden. Listo cuando se termina entre 6:40 y 7:00, sin leer párrafos, con los dos pases de demo ensayados al menos una vez.

## Reserva para jurado (no se habla en los 7:00)

- Detección de rostros: BlazeFace / MediaPipe, latencia menor a 15 ms.
- Identidad: face_recognition / dlib ResNet-34, embeddings de 128 dimensiones, umbral 0.5.
- Emoción: DeepFace, siete clases.
- Gestos: MediaPipe HandLandmarker, 21 puntos.
- Integración: `inmoov_vision.py`, hilos para emoción y parpadeo, latencia de seguimiento menor a 200 ms.
- Cuello: PID Kp=0.20, Ki=0.002, Kd=0.08.
- Gestos: secuencias JSON; expresión facial adelanta al cuerpo 80–150 ms.
```

- [ ] **Step 3: Volver a correr las comprobaciones**

```powershell
rg -n "cero ochenta y cinco" docs/guion-redcolsi-7min.md
rg -n "\[DEMO CNN\]" docs/guion-redcolsi-7min.md
rg -n "\[DEMO FASE 3\]" docs/guion-redcolsi-7min.md
rg -n "Implementar ese modelo en CLAUD-IA" docs/guion-redcolsi-7min.md
rg -n "En paralelo, en el prototipo ya montábamos" docs/guion-redcolsi-7min.md
rg -n "0\.82|0\.96|mAP50 cero noventa[^ ]" docs/guion-redcolsi-7min.md
```

Expected:

- `cero ochenta y cinco` ≥ 1 match
- `[DEMO CNN]` ≥ 1 match
- `[DEMO FASE 3]` ≥ 1 match
- objetivos de Juan presentes (`Implementar ese modelo en CLAUD-IA`)
- ping de metodología presente
- `0.82` y `0.96` = 0 matches (no usar cifras de Conclusiones)

Comprobar también que el texto de Johel en objetivos incluye “analizar las técnicas” y “redes neuronales convolucionales”, y que el pase dice “el androide reconozca personas”.

- [ ] **Step 4: Commit**

```bash
git add docs/guion-redcolsi-7min.md
git commit -m "Agregar el guion conversacional REDCOLSI de 7 minutos a dos voces."
```

---

### Task 2: Inventariar assets visuales sin pisar el Canva de referencia

**Files:**
- Read-only Canva: `DAHXcArwx2g`, `DAHVITCFNFc`
- Optional read: `runs/detect/train5/val_batch0_pred.jpg`, `runs/detect/train5/results.png`
- Produce: lista en el chat (y, si hay IDs útiles, `asset_ids` para Task 3). No crear archivos de inventario en el repo.

**Interfaces:**
- Consumes: diseño de referencia (copia Prometeo REDCOLSI) y original
- Produces: `asset_ids` ordenados para slides 2 (R-ONE), 6 (detección YOLO), 9 (CLAUD-IA), máximo 10 IDs; o la decisión explícita “sin assets reutilizables → marcos etiquetados”

- [ ] **Step 1: Inspeccionar el Canva de referencia (solo lectura)**

Llamar `get-design` y `get-design-pages` sobre `DAHXcArwx2g`. Si `page_count` es 1 y `design_types` incluye `unknown`, tratarlo como video/compuesto: no editarlo.

Llamar `start-editing-transaction` con `design_id=DAHXcArwx2g` **solo para listar** elementos de media. Si aparecen `asset_id` de imagen, llamar `get-assets` con esos IDs y anotar cuáles son foto de robot / detección / prototipo.

**Prohibido:** `commit-editing-transaction` sobre este diseño. Si se abrió transacción, `cancel-editing-transaction` al terminar el inventario.

Repetir inventario en `DAHVITCFNFc` solo si `DAHXcArwx2g` no entrega stills útiles.

- [ ] **Step 2: Decidir fuente de imagen por slide**

Fijar una de estas tres, en este orden, para cada hueco:

1. `asset_id` reutilizable del Canva de referencia (R-ONE → slide 2; predicción/etiquetado → slide 6; CLAUD-IA/cabeza → slide 9).
2. Si no hay still del robot: marco diseñado con leyenda visible `Foto: R-ONE` / `Foto: CLAUD-IA` / `Imagen: detección YOLO`. No usar texto `[TBD]`.
3. Gráfica de métricas: **no** poner curvas en la slide 7 (la spec pide cuatro cifras grandes, no `results.png`). `results.png` y `val_batch0_pred.jpg` quedan de respaldo solo si el marco de la slide 6 necesita una predicción real y Canva permite subir el archivo.

Expected: una tabla de 3 filas (slides 2, 6, 9) con `asset_id` o “marco etiquetado”.

- [ ] **Step 3: No hay commit**

Esta tarea no toca el repo. Seguir a Task 3 con la tabla de assets.

---

### Task 3: Generar candidatos Canva con marca Unilibre

**Files:**
- Create (Canva): job de generación, aún no diseño editable
- Do not use: `create-design` (no aplica Brand Kit)

**Interfaces:**
- Consumes: tabla de assets de Task 2; copy de slides del spec §7.2; guion de Task 1 (mensajes, no párrafos)
- Produces: `job_id` + al menos un `candidate_id` de presentación ~11 slides

- [ ] **Step 1: Confirmar Brand Kit**

Llamar `list-brand-kits`. Usar `brand_kit_id=kAHAXAjmnKs` en el paso 2. Si la llamada falla o el kit no aplica colores, repetir el paso 2 **sin** `brand_kit_id` e incluir los hex `#C8102E` `#FDB913` `#FFFFFF` `#2B2B2B` en el query (ya van en el query de todos modos).

- [ ] **Step 2: Llamar `generate-design`**

Parámetros:

- `design_type`: `presentation`
- `length`: `balanced` (el usuario/spec piden 11 slides, no el default de 1–5)
- `brand_kit_id`: `kAHAXAjmnKs` (omitir solo si el paso 1 falló)
- `asset_ids`: los IDs de Task 2, en orden slide 2 → slide 6 → slide 9. Omitir el parámetro si no hay IDs. Máximo 10.
- `query`: el markdown siguiente, **completo**, sin resumir:

```markdown
**Presentation Brief**
* **Title:** REDCOLSI 2026 — Visión artificial Prometeo (7 min)
* **Topic / Scope:** Presentación académica de 7 minutos del semillero Prometeo, Universidad Libre seccional Bogotá sede Bosque Popular. Modelo CNN/YOLO de reconocimiento de objetos (fases 1–2) e integración de visión de personas en el prototipo CLAUD-IA antes de R-ONE (fase 3).
* **Key Messages:** R-ONE aún no ve; hay un modelo propio medible; el prototipo ya percibe personas.
* **Constraints & Assumptions:** Exactamente 11 diapositivas 16:9. Español. Marca Universidad Libre (rojo #C8102E, oro #FDB913, blanco #FFFFFF, carbón #2B2B2B; escudo Unilibre si el Brand Kit lo trae). Sin neon, sin ciber-grid, sin QR, sin citas de papers, sin notas de orador visibles en la slide. Máximo 5 líneas de cuerpo por slide. Un mensaje visual por slide.
* **Style Guide:** Institucional, limpio, académico. Sans (Arial o la del Brand Kit). Títulos cortos. Números grandes en la slide 7.

**Narrative Arc**
Portada institucional → problema de R-ONE → objetivos a dos columnas (Johel | Juan) → flujo metodológico CNN → Scrum y tres fases → fase 1 → métricas fase 2 → cuatro bloques de fase 3 → prototipo CLAUD-IA → conclusiones a dos voces → cierre de agradecimiento.

**Slide Plan**

* **Slide 1 — "Visión artificial para entornos reales"**
* **Goal:** Identificar institución, semillero y expositores.
* **Bullets (3–6):**
  * Desarrollo de un modelo de IA y visión artificial para reconocimiento automático de objetos en entornos reales
  * Semillero de investigación Prometeo
  * Universidad Libre — Seccional Bogotá, sede Bosque Popular
  * Johel Santiago Arias Becerra
  * Juan Manuel Toro Grajales
* **Visuals:** Fondo blanco o rojo institucional suave; escudo Unilibre; franja oro.
* **Data/Inputs:** Nombres completos; no inventar logos ajenos.
* **Speaker Notes (2–4 sentences):** El guion vive en docs/guion-redcolsi-7min.md. No proyectar notas.
* **Transition:** El problema: R-ONE no ve.

* **Slide 2 — "R-ONE todavía no reconoce el entorno"**
* **Goal:** Enunciar el problema en una frase.
* **Bullets (3–6):**
  * Androide de propósito general en Bosque Popular
  * Interactúa con visitantes y orienta procesos internos
  * Hoy no reconoce objetos ni personas
  * Toda visión se prueba antes en CLAUD-IA
* **Visuals:** Foto de R-ONE a la derecha; si no hay foto, marco rojo/oro con leyenda "Foto: R-ONE".
* **Data/Inputs:** No cifras.
* **Speaker Notes (2–4 sentences):** Habla Juan. Ver guion Beat 1.
* **Transition:** Objetivos repartidos.

* **Slide 3 — "Objetivos a dos voces"**
* **Goal:** Mostrar el reparto Johel | Juan.
* **Bullets (3–6):**
  * Columna Johel: objetivo general (objetos en entornos reales)
  * Columna Johel: analizar técnicas actuales y limitaciones
  * Columna Johel: desarrollar y entrenar una CNN
  * Columna Juan: implementar el modelo en la cabeza de CLAUD-IA
  * Columna Juan: evaluar en escenarios reales
* **Visuals:** Dos columnas iguales, acentos rojo (Johel) y oro (Juan).
* **Data/Inputs:** Texto de objetivos del spec, sin parafrasear el sentido.
* **Speaker Notes (2–4 sentences):** Beat 2 del guion.
* **Transition:** Cómo se construye un CNN propio.

* **Slide 4 — "Dataset propio, luego el modelo"**
* **Goal:** Mostrar el flujo del referente sin autores.
* **Bullets (3–6):**
  * Dataset propio
  * Preprocesamiento
  * Augmentation
  * Entrenamiento CNN
* **Visuals:** Flecha o 4 pasos horizontales. Cero nombres de papers.
* **Data/Inputs:** Rotación, volteo y color se pueden mencionar en subtítulo pequeño, no como cita.
* **Speaker Notes (2–4 sentences):** Beat 3. Si falta tiempo, esta es la segunda pieza recortable.
* **Transition:** Cómo se organizó el trabajo.

* **Slide 5 — "Tres sprints, un dataset propio"**
* **Goal:** Scrum + cifras de muestra.
* **Bullets (3–6):**
  * Metodología Scrum: un sprint por fase
  * 802 imágenes
  * 25 clases
  * Partición 80 / 10 / 10
  * Etiquetado YOLO a mano
* **Visuals:** Línea de tiempo Fase 1 · Fase 2 · Fase 3.
* **Data/Inputs:** 802, 25, 80/10/10 exactos.
* **Speaker Notes (2–4 sentences):** Beat 4. Juan dice una frase; no cambiar de slide.
* **Transition:** Qué produjo la fase 1.

* **Slide 6 — "Fase 1: CNN propia para objetos"**
* **Goal:** Nombrar el modelo inicial.
* **Bullets (3–6):**
  * Visión por computador en entorno real
  * Redes neuronales convolucionales profundas
  * Entrenamiento YOLO
  * Dataset recolectado por el semillero
* **Visuals:** Imagen de etiquetado o predicción YOLO; si no hay, marco con leyenda "Imagen: detección YOLO".
* **Data/Inputs:** No métricas aún.
* **Speaker Notes (2–4 sentences):** Beat 5 primera mitad.
* **Transition:** Mejora y números.

* **Slide 7 — "Fase 2: el modelo ya es medible"**
* **Goal:** Cuatro cifras grandes; esta slide se queda en la demo CNN.
* **Bullets (3–6):**
  * Precisión 0.85
  * Recall 0.95
  * mAP50 0.99
  * mAP50-95 0.87
  * 60 épocas, sin sobreajuste evidente
* **Visuals:** Cuatro números a tipografía extra grande; no curvas; no 0.82 ni 0.90.
* **Data/Inputs:** 0.85 / 0.95 / 0.99 / 0.87 únicamente.
* **Speaker Notes (2–4 sentences):** Beat 5–6. Cue: "Mejor que contarlo, lo mostramos."
* **Transition:** Pase a personas.

* **Slide 8 — "Fase 3: cuatro percepciones, un ciclo"**
* **Goal:** Pase visual Johel → Juan.
* **Bullets (3–6):**
  * Rostro: detectar y localizar
  * Identidad: conocido o desconocido
  * Emoción: siete estados
  * Gesto: palma, puño, pulgar arriba
* **Visuals:** Cuatro bloques iguales. No logos de MediaPipe/DeepFace.
* **Data/Inputs:** Siete emociones no hace falta listarlas todas en la slide (el habla sí las puede decir).
* **Speaker Notes (2–4 sentences):** Beat 7–8.
* **Transition:** El cuerpo que ejecuta esa percepción.

* **Slide 9 — "CLAUD-IA, el homólogo de R-ONE"**
* **Goal:** Anclar el prototipo; esta slide se queda en la demo de Juan.
* **Bullets (3–6):**
  * 14 servomotores faciales
  * Seguimiento de cuello
  * Gestos de emoción, saludo y atención
  * Se prueba aquí antes de R-ONE
* **Visuals:** Foto de CLAUD-IA / cabeza; si no hay, marco con leyenda "Foto: CLAUD-IA".
* **Data/Inputs:** No PID, no JSON, no nombres de archivos.
* **Speaker Notes (2–4 sentences):** Beat 8–9. Cue de demo libre.
* **Transition:** Cerrar el arco.

* **Slide 10 — "Lo que quedó demostrado"**
* **Goal:** Dos conclusiones, una por voz.
* **Bullets (3–6):**
  * Johel: entrenamiento estable; equilibrio precisión / recall; usable en entorno real
  * Juan: el prototipo percibe caras, emoción y gesto
* **Visuals:** Dos viñetas, mismo peso visual que la slide 3.
* **Data/Inputs:** Sin cifras (las cifras ya están en la 7).
* **Speaker Notes (2–4 sentences):** Beat 10. Si falta tiempo, una frase cada uno.
* **Transition:** Agradecimiento.

* **Slide 11 — "Gracias"**
* **Goal:** Cerrar con identidad institucional.
* **Bullets (3–6):**
  * Gracias
  * Semillero Prometeo
  * Universidad Libre — Seccional Bogotá
  * Johel Santiago Arias Becerra · Juan Manuel Toro Grajales
* **Visuals:** Escudo Unilibre; franja oro; sin QR, sin correos, sin Instagram.
* **Data/Inputs:** Mismos nombres que la portada.
* **Speaker Notes (2–4 sentences):** Última frase del guion.
* **Transition:** Fin.
```

Expected: respuesta con `job_id` y candidatos con thumbnails. Si el error es “Common queries will not be generated”, reenviar el mismo query (no acortarlo).

- [ ] **Step 3: Elegir candidato**

Elegir el candidato cuya portada se vea institucional (rojo/oro/blanco, no neon) y que muestre ~11 slides en el preview. Anotar `job_id` y `candidate_id`. No crear aún el diseño editable.

- [ ] **Step 4: No hay commit de repo**

---

### Task 4: Materializar, verificar y corregir las 11 slides

**Files:**
- Create (Canva): diseño editable nuevo
- Modify (Canva): texto/imágenes del diseño nuevo únicamente

**Interfaces:**
- Consumes: `job_id`, `candidate_id` de Task 3
- Produces: `design_id` nuevo (11 caracteres, empieza por `D`); `edit_url`; 11 páginas; copy alineado a la tabla de verificación de este task

- [ ] **Step 1: Convertir el candidato**

Llamar `create-design-from-candidate` con el `job_id` y `candidate_id` de Task 3.

Expected: `design_id` distinto de `DAHXcArwx2g` y de `DAHVITCFNFc`. Llamar `update_title` en una transacción posterior si el título no es exactamente `REDCOLSI 2026 — Visión artificial Prometeo (7 min)`.

- [ ] **Step 2: Verificar páginas y copy (prueba que debe pasar)**

```
get-design(design_id)           → page_count == 11
get-design-pages(design_id)     → 11 thumbnails 16:9
get-design-content(design_id, content_types=["richtexts"])
```

El texto extraído **debe** contener:

- `Johel Santiago Arias Becerra`
- `Juan Manuel Toro Grajales`
- `Prometeo`
- `CLAUD-IA`
- `0.85` (o `0,85`) y `0.95` y `0.99` y `0.87`
- `802`
- `R-ONE`

El texto extraído **no debe** contener:

- `0.82` ni `0.90` como métricas de Conclusiones
- nombres de papers (`Tabassum`, `Avro`)
- `BlazeFace`, `DeepFace`, `inmoov_vision.py` (reserva de jurado, no slide)
- URLs o QR

Si `page_count != 11`, no parchar con slides de relleno genéricas: regenerar en Task 3 con el mismo query insistiendo “exactamente 11 diapositivas, ni 10 ni 12”.

- [ ] **Step 3: Corregir copy si la prueba falla**

`start-editing-transaction` sobre el **nuevo** `design_id`. Usar `replace_text` / `find_and_replace_text` para alinear cada slide a esta copy corta (cuerpo máximo 5 líneas):

| Slide | Título visible | Cuerpo visible |
|---|---|---|
| 1 | Visión artificial para entornos reales | Título largo del proyecto; Prometeo; Universidad Libre seccional Bogotá; Johel Santiago Arias Becerra; Juan Manuel Toro Grajales |
| 2 | R-ONE todavía no reconoce el entorno | No reconoce objetos ni personas. Se prueba en CLAUD-IA. |
| 3 | Objetivos a dos voces | Columna Johel: general + analizar + CNN. Columna Juan: implementar en CLAUD-IA + evaluar. |
| 4 | Dataset propio, luego el modelo | Dataset propio → preproceso → augmentation → CNN |
| 5 | Tres sprints, un dataset propio | Scrum. 802 imágenes · 25 clases · 80/10/10 |
| 6 | Fase 1: CNN propia para objetos | CNN profundas. YOLO. Entorno real. |
| 7 | Fase 2: el modelo ya es medible | 0.85 Precisión · 0.95 Recall · 0.99 mAP50 · 0.87 mAP50-95 · 60 épocas |
| 8 | Fase 3: cuatro percepciones, un ciclo | Rostro · Identidad · Emoción · Gesto |
| 9 | CLAUD-IA, el homólogo de R-ONE | 14 servos · cuello · gestos · antes de R-ONE |
| 10 | Lo que quedó demostrado | Modelo robusto (Johel). Percepción en el prototipo (Juan). |
| 11 | Gracias | Prometeo · Universidad Libre · ambos nombres |

Mostrar preview al usuario. **Solo después de su OK**, `commit-editing-transaction`. Si rechaza, `cancel-editing-transaction` y ajustar.

- [ ] **Step 4: No hay commit de repo todavía**

Anotar `edit_url` para Task 5.

---

### Task 5: Anclar la URL Canva en el guion

**Files:**
- Modify: `docs/guion-redcolsi-7min.md` (única línea “Presentación Canva”)

**Interfaces:**
- Consumes: `edit_url` de Task 4
- Produces: guion con enlace real; repo listo para ensayo

- [ ] **Step 1: Reemplazar el placeholder de URL**

En `docs/guion-redcolsi-7min.md`, cambiar:

```markdown
Presentación Canva: _pendiente de URL (Task 5)_.
```

por:

```markdown
Presentación Canva (edición): <edit_url exacta de Task 4>
```

No tocar el resto del guion.

- [ ] **Step 2: Comprobación final conjunta**

```powershell
rg -n "canva.com" docs/guion-redcolsi-7min.md
rg -n "pendiente de URL" docs/guion-redcolsi-7min.md
rg -n "cero ochenta y cinco" docs/guion-redcolsi-7min.md
```

Expected: `canva.com` ≥ 1; `pendiente de URL` = 0; métrica hablada sigue presente.

Confirmar otra vez `get-design` del diseño nuevo: `page_count == 11` y título `REDCOLSI 2026 — Visión artificial Prometeo (7 min)`.

- [ ] **Step 3: Commit**

```bash
git add docs/guion-redcolsi-7min.md
git commit -m "Enlazar la presentación Canva REDCOLSI en el guion de 7 minutos."
```

- [ ] **Step 4: Entrega al usuario**

Devolver:

1. Ruta del guion: `docs/guion-redcolsi-7min.md`
2. `edit_url` de Canva
3. Recordatorio de ensayo: cronómetro 7:00, dos demos, plan B en el propio guion
