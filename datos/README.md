# Diccionario de Datos

## scouting_qatar_2022.csv

Dataset consolidado de rendimiento de jugadores en el Mundial Qatar 2022.

| Columna | Tipo | Descripcion |
|---------|------|-------------|
| Jugador | string | Nombre completo del jugador |
| Equipo | string | Seleccion nacional |
| Pases_Intentados | int | Total de pases intentados |
| Pases_Completados | int | Pases completados exitosamente |
| Tiros_Totales | int | Total de tiros al arco |
| Goles | int | Goles convertidos |
| Presiones | int | Acciones de presion sobre el rival |
| Regates_Intentados | int | Intentos de driblar |
| Regates_Exitosos | int | Regates completados |
| Quites_Intentados | int | Intentos de quitar la pelota (tackles) |
| Efectividad_Pases_% | float | Porcentaje de pases completados |
| Efectividad_Regates_% | float | Porcentaje de regates exitosos |

### Filtros aplicados
- Solo jugadores con 5 o mas pases intentados (se eliminaron jugadores testimoniales)

---

## datos_pases_final.csv

Datos granulares de cada pase registrado en la final del Mundial Qatar 2022 (Argentina vs Francia).

| Columna | Tipo | Descripcion |
|---------|------|-------------|
| id | string | Identificador unico del evento |
| period | int | Periodo del partido (1 = primer tiempo, 2 = segundo tiempo, etc.) |
| timestamp | string | Marca de tiempo del evento |
| minute | int | Minuto del partido |
| second | int | Segundo del minuto |
| team | string | Equipo que ejecuta el pase |
| player | string | Jugador que ejecuta el pase |
| pass_recipient | string | Jugador que recibe el pase |
| pass_length | float | Distancia del pase en metros |
| pass_angle | float | Angulo del pase en radianes |
| pass_outcome | string | Resultado del pase (Completado, Incomplete, Out, Unknown, Pass Offside) |
