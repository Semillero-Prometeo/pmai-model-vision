# Guion REDCOLSI — 7 minutos

**Evento:** REDCOLSI / encuentro de semilleros  
**Proyecto:** Desarrollo de un modelo de IA y visión artificial para reconocimiento automático de objetos en entornos reales  
**Semillero:** Prometeo — Universidad Libre, seccional Bogotá, sede Bosque Popular  
**Expositores:** Johel Santiago Arias Becerra (fases 1 y 2) y Juan Manuel Toro Grajales (fase 3)

Este archivo es el libreto oficial. El texto bajo **JOHEL** / **JUAN** es sugerido (académico hablado). Son rígidos: números, pases y cues de demo. No leer párrafos. Preguntas del jurado quedan fuera de los 7:00.

Presentación Canva (edición): https://canva.link/ioduyokyi3bctkp

## Reloj

| Tiempo | Quién | Beat | Slide |
|---|---|---|---|
| 0:00–0:40 | Ambos | Portada y problema | 1 → 2 |
| 0:40–0:45 | Ambos | Portadilla Objetivos | 3 |
| 0:45–1:25 | Ambos | Objetivos (sin nombres en la slide) | 4 |
| 1:25–1:30 | Johel | Portadilla Referente técnico | 5 |
| 1:30–1:50 | Johel | Referente técnico | 6 |
| 1:50–1:55 | Johel | Portadilla Metodología | 7 |
| 1:55–2:15 | Johel + pase de Juan | Scrum y tres fases | 8 |
| 2:15–2:20 | Johel | Portadilla Resultados | 9 |
| 2:20–2:55 | Johel | Fases 1 y 2 + métricas | 10 → 11 |
| 2:55–3:40 | Johel | Demo CNN | 11 se queda |
| 3:40–3:55 | Pase | Entrega a personas | 12 |
| 3:55–5:10 | Juan | Fase 3 y CLAUD-IA | 12 → 13 |
| 5:10–6:30 | Juan | Demo fase 3 | 13 se queda → 14 |
| 6:30–7:00 | Ambos | Conclusiones y cierre | 15 → 16 |

Si una demo se alarga, se recorta el cierre. No se recortan objetivos, métricas ni el pase Johel → Juan. Si Johel se pasa en la demo CNN, Juan recorta la explicación de fase 3, no la demo 3, salvo que queden menos de 90 s totales.

Corte de tiempo, en este orden: (1) cierre a una frase cada uno; (2) detalle del referente; (3) detalle de servos / cuello / repertorio.

## Beat 1 — Apertura (0:00–0:40)

[SLIDE 1] Johel avanza a [SLIDE 2] cuando Juan empieza el problema.

**JOHEL:** Muy buenos días. El día de hoy, junto a mi compañero Juan Manuel Toro Grajales y yo, Johel Santiago Arias, integrantes del semillero Prometeo, presentamos el proyecto Desarrollo de un modelo de IA y visión artificial para reconocimiento automático de objetos en entornos reales.

**JUAN:** Actualmente la Universidad Libre de Colombia, en la seccional Bogotá, sede Bosque Popular, cuenta con un androide de propósito general denominado R-ONE. Va a interactuar con visitantes y miembros de la universidad y a orientar procesos internos y administrativos. Hoy el androide no reconoce objetos ni atributos de las personas que se cruzan con él; sin eso la interacción se queda corta. Toda integración de visión la certificamos antes en el prototipo homólogo CLAUD-IA.

**JOHEL:** Por eso el trabajo se organizó en tres fases. Hoy vamos a ver el modelo y el prototipo.

## Beat 2 — Objetivos (0:40–1:25)

[SLIDE 3] portadilla. Johel avanza a [SLIDE 4] al empezar el objetivo general.

**JOHEL:** El objetivo general fue desarrollar un modelo de IA y visión artificial para el reconocimiento automático de objetos y personas en entornos reales. En las dos primeras fases nos concentramos en los objetos: analizar las técnicas actuales de reconocimiento y sus limitaciones en entornos reales, y desarrollar un modelo basado en redes neuronales convolucionales, entrenarlo y dejarlo medible.

**JUAN:** Del lado del prototipo, implementar ese modelo en CLAUD-IA a través de la creación de la cabeza, y evaluarlo en escenarios reales para medir precisión y eficiencia —ya no solo sobre objetos, también sobre personas.

## Beat 3 — Referente técnico (1:25–1:50)

[SLIDE 5] portadilla. Johel avanza a [SLIDE 6] al hablar del flujo CNN.

**JOHEL:** En la literatura de visión artificial con CNN, el flujo consolidado parte de un dataset propio, sigue con preprocesamiento y aumento de datos, y recién entonces el entrenamiento. Trabajos con CNN personalizadas sobre datasets heterogéneos usan redimensionado, normalización y augmentation —rotación, volteo y color— para ganar robustez. Ese fue nuestro marco para las fases 1 y 2.

## Beat 4 — Metodología (1:50–2:15)

[SLIDE 7] portadilla. Johel avanza a [SLIDE 8] al nombrar Scrum. No cambia de slide cuando habla Juan.

**JOHEL:** El proceso fue investigación-desarrollo, organizado con Scrum: un sprint por fase. El dataset es propio: 802 imágenes, 25 clases, capturadas con celular, etiquetadas a mano con bounding boxes YOLO, y partidas ochenta, diez y diez entre entrenamiento, validación y prueba.

**JUAN:** En paralelo, en el prototipo ya montábamos la percepción de personas.

## Beat 5 — Fases 1 y 2 (2:15–2:55)

[SLIDE 9] portadilla Resultados. [SLIDE 10] al hablar de fase 1. [SLIDE 11] al hablar de fase 2 y métricas.

**JOHEL:** La fase 1 fue el desarrollo propio de un modelo de visión por computador para objetos en entornos reales, fundamentado en redes neuronales convolucionales profundas y entrenado con YOLO.

En la fase 2 mejoramos ese modelo con preprocesamiento, estandarización, data augmentation fotométrica y geométrica, y más datos. En sesenta épocas las pérdidas de entrenamiento y validación bajaron sin signos de sobreajuste. El modelo quedó en precisión cero ochenta y cinco, recall cero noventa y cinco, mAP50 cero noventa y nueve, y mAP50-95 cero ochenta y siete.

## Beat 6 — Demo CNN (2:55–3:40)

[SLIDE 11 se queda]

**JOHEL:** Mejor que contarlo, lo mostramos.

[DEMO CNN] Johel muestra el funcionamiento del detector. El detalle es libre. No narrar librerías ni hiperparámetros.

[PLAN B CNN] Si la demo falla: “El detector localiza objetos en cámara; las métricas que acaban de ver corresponden a ese modelo.” Pasa de inmediato a Juan. No se reinicia el software en escena.

## Beat 7 — Pase (3:40–3:55)

Juan abre [SLIDE 12].

**JOHEL:** Eso es el modelo de objetos. El siguiente paso es que el androide reconozca personas.

## Beat 8 — Fase 3 (3:55–5:10)

[SLIDE 12] pipeline. [SLIDE 13] al nombrar CLAUD-IA.

**JUAN:** En la fase 3 el modelo de visión combina cuatro componentes en un solo ciclo. Detectamos y localizamos rostros, incluso con varias personas en escena. Sobre el rostro distinguimos si es alguien conocido o desconocido. En paralelo leemos el estado emocional —alegría, tristeza, enojo, sorpresa, miedo, disgusto o neutro— e interpretamos gestos de mano: palma abierta, puño o pulgar arriba.

Todo eso vive en CLAUD-IA: calibramos catorce servomotores faciales, el cuello sigue a la persona, y hay un repertorio de gestos de emoción, saludo y atención, sincronizados con cabeza y torso. Se prueba en el homólogo antes de subir a R-ONE.

## Beat 9 — Demo fase 3 (5:10–6:30)

[SLIDE 13 se queda]. Tras la demo, Juan deja [SLIDE 14] un instante.

**JUAN:** Y esto es el funcionamiento.

[DEMO FASE 3] Juan muestra rostro, emoción y/o gesto. El detalle es libre.

[PLAN B FASE 3] Si la demo falla: “El ciclo detecta rostro, emoción y gesto, y mueve la cabeza de CLAUD-IA.” Salta a conclusiones. Prototipo a postura neutra. No se culpa al hardware.

**JUAN:** Lo que acaban de ver es percepción y actuación en el mismo ciclo.

## Beat 10 — Cierre (6:30–7:00)

[SLIDE 15] conclusiones. [SLIDE 16] agradecimiento.

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
