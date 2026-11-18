# Guion REDCOLSI 7 min y presentación Canva

Fecha: 2026-10-08  
Proyecto: Desarrollo de un modelo de IA y visión artificial para reconocimiento automático de objetos en entornos reales  
Semillero: Prometeo — Universidad Libre, seccional Bogotá, sede Bosque Popular  
Expositores: Johel Santiago Arias Becerra (fases 1 y 2) y Juan Manuel Toro Grajales (fase 3)

## 1. Problema

El guion actual (`docs/proyecto-conversacional.md`) es un monólogo en bloques, incompleto para 7 minutos y sin reparto claro de voces. Hace falta un guion conversacional a dos actores, alineado al formato académico REDCOLSI, y una presentación Canva de 11 diapositivas que siga ese guion, con marca Universidad Libre.

## 2. Objetivo

Entregar dos piezas acopladas:

1. Un guion hablable de 7:00 exactos, híbrido (apertura y cierre a dos voces; bloques por fase; pases cortos).
2. Una presentación Canva 16:9 de 11 slides, una por beat, lista para proyectar en REDCOLSI.

Criterio de éxito: un ensayo cronometrado termina entre 6:40 y 7:00, ambos expositores saben cuándo hablar y cuándo avanzar slide, y las dos demos tienen cue de entrada, margen de tiempo y frase de respaldo.

## 3. Fuera de alcance

- No reescribir `docs/proyecto-completo.md`.
- No editar ni pisar el Canva de referencia Prometeo/REDCOLSI.
- No coreografiar el detalle de las demos (el expositor decide qué mostrar).
- No incluir ronda de preguntas del jurado dentro de los 7 minutos.
- No animaciones largas, QR, contactos extra, ni notas de orador dentro de Canva.
- No citar papers en la diapositiva (el referente se habla, no se proyecta).

## 4. Actores y responsabilidades

| Actor | Contenido hablado | Demo |
|---|---|---|
| Johel Santiago Arias | Apertura (nombres, Prometeo, título); objetivos general + analizar técnicas + desarrollar/entrenar CNN; referente técnico; Scrum y tres fases; fases 1 y 2; métricas; pase a Juan; cierre de modelo | Demo corta del detector CNN (~45 s), detalle libre |
| Juan Manuel Toro Grajales | Problema de R-ONE en la apertura; objetivos de implementar en CLAUD-IA y evaluar en escenarios reales; pase corto en metodología (“en paralelo, percepción de personas en el prototipo”); fase 3; cierre de prototipo | Demo de funcionamiento fase 3 (~80 s): rostro, emoción, gesto; detalle libre |

Quien habla avanza su propia diapositiva, salvo el pase Johel → Juan (Johel deja la 7; Juan abre la 8).

## 5. Reloj (7:00)

| Tiempo | Quién | Beat | Slide |
|---|---|---|---|
| 0:00–0:40 | Ambos | Portada, Prometeo, problema de R-ONE | 1 → 2 |
| 0:40–1:25 | Ambos | Objetivos | 3 |
| 1:25–1:50 | Johel | Referente técnico | 4 |
| 1:50–2:15 | Johel + pase de Juan | Scrum y las tres fases | 5 |
| 2:15–2:55 | Johel | Fase 1 (CNN) y fase 2 (mejora + métricas) | 6 → 7 |
| 2:55–3:40 | Johel | Demo corta del modelo CNN | 7 se queda |
| 3:40–3:55 | Pase | Johel entrega; Juan toma personas y prototipo | 8 |
| 3:55–5:10 | Juan Manuel | Fase 3: pipeline y CLAUD-IA | 8 → 9 |
| 5:10–6:30 | Juan Manuel | Demo en vivo fase 3 | 9 se queda |
| 6:30–7:00 | Ambos | Conclusiones y cierre | 10 → 11 |

Si una demo se alarga, se recorta el cierre. No se recortan objetivos, métricas ni el pase entre fases.

## 6. Guion por beats

Tono: académico hablado, en la línea de `docs/proyecto-conversacional.md`. Cada beat son 3–5 frases, no párrafos leídos. El archivo de implementación será un libreto con texto sugerido, cues de slide y cues de demo; no un copión rígido excepto números y pases.

### 6.1 Apertura (0:00–0:40)

- Johel saluda, nombra a Johel Santiago Arias y Juan Manuel Toro Grajales, el semillero Prometeo y el título del proyecto.
- Juan plantea el problema: la Universidad Libre, seccional Bogotá, sede Bosque Popular, cuenta con el androide de propósito general R-ONE (interacción con visitantes y miembros, orientación administrativa). Hoy no reconoce objetos ni atributos de las personas; sin eso la interacción se queda corta. Toda integración de visión se prueba antes en el prototipo homólogo CLAUD-IA.
- Johel cierra el beat: el trabajo va en tres fases; hoy se ve el modelo y el prototipo.

### 6.2 Objetivos (0:40–1:25)

Objetivo general (Johel): desarrollar un modelo de IA y visión artificial para el reconocimiento automático de objetos y personas en entornos reales. Johel enfatiza la parte de objetos; Juan retoma personas al tomar sus específicos.

Johel (~25 s):

- Analizar las técnicas actuales de reconocimiento de objetos y sus limitaciones en entornos reales.
- Desarrollar un modelo de IA basado en CNN para reconocimiento de objetos y entrenarlo.

Juan (~20 s):

- Implementar el modelo al prototipo físico CLAUD-IA, a través de la creación de la cabeza.
- Evaluar el modelo en escenarios reales para medir precisión y eficiencia.

### 6.3 Referente técnico (1:25–1:50) — Johel

La literatura de visión con CNN respalda un flujo: dataset propio → preprocesamiento → aumento de datos → entrenamiento. Estudios sobre CNN personalizadas en datasets heterogéneos usan redimensionado, normalización y augmentation (rotación, volteo, color). Ese es el marco de las fases 1 y 2. No se proyectan autores en la slide.

### 6.4 Metodología (1:50–2:15)

Johel: investigación-desarrollo mixta, organizada con Scrum; cada fase es un sprint. Dataset propio: 802 imágenes, 25 clases (rostros de integrantes del semillero, distintos ambientes), captura con celular, etiquetado manual YOLO, partición 80 % entrenamiento / 10 % validación / 10 % prueba.

Pase corto de Juan (Johel no cambia de slide): en paralelo, en el prototipo ya se montaba la percepción de personas. No adelanta resultados de fase 3.

### 6.5 Fases 1 y 2 (2:15–2:55) — Johel

Fase 1: modelo propio de visión por computador para objetos en entornos reales, basado en CNN profundas (entrenamiento YOLO).

Fase 2: preprocesamiento y estandarización, data augmentation fotométrica y geométrica, y aumento del dataset.

Números oficiales (unificados desde Resultados de `docs/proyecto-completo.md`, no desde Conclusiones):

- 60 épocas
- Precisión 0.8486 → se dice “cero ochenta y cinco”
- Recall 0.9474 → se dice “cero noventa y cinco”
- mAP50 0.9942 → se dice “cero noventa y nueve”
- mAP50-95 0.8677 → se dice “cero ochenta y siete”
- Pérdidas de entrenamiento y validación descendentes, sin sobreajuste evidente

Las conclusiones del documento completo traen cifras distintas (aprox. 0.82 / 0.96 / 0.90 / 0.78). En este guion y en las slides **solo** se usan las de Resultados.

### 6.6 Demo CNN (2:55–3:40) — Johel

Cue de entrada: “mejor que contarlo, lo mostramos”.

El guion no describe el detalle de la demo. Johel muestra el funcionamiento del detector. Slide 7 permanece.

Cue de salida / pase (3:40–3:55): “eso es el modelo de objetos; el siguiente paso es que el androide reconozca personas”.

### 6.7 Fase 3 (3:55–5:10) — Juan Manuel

Cuatro componentes en un solo ciclo de percepción, hablados sin enumerar librerías ni constantes salvo pregunta posterior:

- Detección y localización de rostros (varias personas, tiempo real).
- Identidad: conocido o desconocido.
- Emoción: alegría, tristeza, enojo, sorpresa, miedo, disgusto, neutro.
- Gestos de mano: palma abierta, puño, pulgar arriba.

Integración en CLAUD-IA: 14 servomotores faciales, seguimiento de cuello, repertorio de gestos (emoción, saludo, atención) y sincronía cabeza-torso. Se prueba en el homólogo antes de integrar a R-ONE.

Fuera de la oralidad obligatoria (reserva para jurado): BlazeFace/MediaPipe, face_recognition/dlib embeddings 128-d, umbral 0.5, DeepFace, HandLandmarker 21 puntos, `inmoov_vision.py`, latencia <200 ms, PID Kp=0.20 Ki=0.002 Kd=0.08, secuencias JSON.

### 6.8 Demo fase 3 (5:10–6:30) — Juan Manuel

Cue de entrada: mostrar el funcionamiento. Detalle libre (rostro, emoción, gesto). Slide 9 permanece.

Cue de salida: una frase que une percepción y actuación en el mismo ciclo, y entrega al cierre.

### 6.9 Cierre (6:30–7:00)

Johel: el entrenamiento fue estable; el modelo quedó con buen equilibrio precisión/recall y usable en entorno real.

Juan: eso permitió explorar caras, emoción y gesto sobre el prototipo.

Ambos: agradecimiento al espacio, al semillero Prometeo y a la Universidad Libre.

## 7. Presentación Canva

### 7.1 Marca

- Formato presentación 16:9, 1920×1080, 11 páginas.
- Paleta Universidad Libre (hex de trabajo si el Brand Kit no aporta muestras): rojo `#C8102E`, oro `#FDB913`, blanco `#FFFFFF`, carbón `#2B2B2B`. Sin neon ni paleta “tech” ajena.
- Si el Brand Kit de Canva (`kAHAXAjmnKs`) trae colores y fuentes, esos valores pisan los hex de trabajo. Si no, se aplican los hex anteriores y una sans institucional (Arial o equivalente Canva).
- Identidad en slides 1 y 11: escudo Unilibre, seccional Bogotá / Bosque Popular, semillero Prometeo. Nombres completos en portada: Johel Santiago Arias Becerra y Juan Manuel Toro Grajales. En el habla basta Johel / Juan Manuel.
- Títulos cortos; máximo 5 líneas de cuerpo; un mensaje visual por slide.

### 7.2 Diapositivas

1. **Portada** — título del proyecto; Prometeo; Unilibre; Johel Santiago Arias Becerra; Juan Manuel Toro Grajales.
2. **Problema** — R-ONE no reconoce objetos ni personas. Hueco `[FOTO: R-ONE]` a la derecha.
3. **Objetivos** — dos columnas alineadas al reparto de voz: Johel (general + analizar + CNN) | Juan (implementar en CLAUD-IA + evaluar).
4. **Referente** — flujo de cuatro pasos: dataset propio → preproceso → augmentation → CNN. Sin citas proyectadas.
5. **Metodología** — línea de tres fases (Scrum). Cifras: 802 imágenes, 25 clases, 80/10/10.
6. **Fase 1** — CNN propia para objetos en entorno real. Hueco `[IMG: etiquetado YOLO o predicción]`.
7. **Fase 2 y métricas** — cuatro cifras grandes: 0.85 / 0.95 / 0.99 / 0.87, con etiquetas Precisión, Recall, mAP50, mAP50-95. Permanece durante la demo CNN.
8. **Fase 3** — cuatro bloques: rostro, identidad, emoción, gesto. Pase visual Johel → Juan.
9. **CLAUD-IA** — hueco `[FOTO: CLAUD-IA / cabeza]`. Permanece durante la demo de Juan.
10. **Conclusiones** — dos viñetas: modelo robusto (Johel) y percepción en el prototipo (Juan).
11. **Cierre** — gracias; Prometeo; Universidad Libre.

### 7.3 Imágenes

Orden de obtención:

1. Reutilizar assets del Canva de referencia del proyecto (`DAHXcArwx2g`, copia de “Presentacion de Proyecto - Prometeo - REDCOLSI”; original `DAHVITCFNFc`).
2. Curvas de entrenamiento del repo (`runs/detect/train5`), si se necesita una gráfica real.
3. Si un asset no se puede extraer o copiar: dejar hueco etiquetado para que el equipo lo pegue.

No inventar fotos del robot ni métricas.

Título del nuevo diseño Canva: `REDCOLSI 2026 — Visión artificial Prometeo (7 min)`. Crear diseño nuevo; no sobrescribir los Canva existentes.

## 8. Plan B (demos y tiempo)

Demo CNN falla: Johel dice que el detector localiza objetos en cámara y que las métricas de la slide 7 corresponden a ese modelo; pasa de inmediato a Juan. No se reinicia software en escena.

Demo fase 3 falla: Juan dice que el ciclo detecta rostro, emoción y gesto y mueve la cabeza de CLAUD-IA; salta a conclusiones. Prototipo a postura neutra. No se culpa al hardware.

Prioridad de corte si se acaba el tiempo:

1. Cierre (queda una frase cada uno).
2. Detalle del referente.
3. Detalle de servos / cuello / repertorio de gestos.

Nunca se cortan objetivos, métricas ni el pase Johel → Juan.

Si Johel se pasa en la demo CNN, Juan recorta la explicación de fase 3, no la demo 3, salvo que queden menos de 90 s totales.

## 9. Entregables de implementación

| Pieza | Ruta o destino |
|---|---|
| Guion conversacional completo (tiempos, texto sugerido, cues de slide, cues de demo, plan B) | `docs/guion-redcolsi-7min.md` |
| Presentación Canva de 11 slides | Diseño nuevo en la cuenta Canva; URL de edición en el mismo markdown al cierre |
| Este spec | `docs/superpowers/specs/2026-10-08-guion-redcolsi-presentacion-design.md` |

`docs/proyecto-conversacional.md` se deja como borrador previo; el guion oficial pasa a ser `docs/guion-redcolsi-7min.md`.

## 10. Ensayo

Un cronómetro de 7:00, slides reales, ambas demos en el mismo orden. Listo cuando se termina entre 6:40 y 7:00, sin leer párrafos, con los dos pases de demo ensayados al menos una vez.
