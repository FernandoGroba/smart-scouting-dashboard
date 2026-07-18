# Metodologia

## Flujo del Proyecto

```
StatsBomb API  --->  Python (extraccion)  --->  CSV  --->  Power BI (visualizacion)
     |                      |                    |                    |
  Datos crudos        Limpieza y           Datos limpios       Dashboard
  de eventos          agregacion           listos para          interactivo
  (Qatar 2022)        de metricas          analisis
```

## 1. Fuente de Datos

Se utiliza la **API abierta de StatsBomb**, que provee datos de eventos a nivel granular para competiciones profesionales. El dataset incluye todos los partidos del **Mundial Qatar 2022** (Competencia ID: 43, Temporada ID: 106).

## 2. Extraccion y Procesamiento (Python)

El script `extractor_futbol.py` realiza los siguientes pasos:

1. **Conexion a la API**: Se conecta a StatsBomb y obtiene la lista de todos los partidos del mundial
2. **Extraccion de eventos**: Para cada partido, se descargan todos los eventos registrados
3. **Filtrado**: Se seleccionan solo los eventos relevantes para scouting:
   - `Pass` (pases)
   - `Shot` (tiros)
   - `Pressure` (presiones)
   - `Duel` (duelos/tackles)
   - `Dribble` (regates)
4. **Agregacion**: Se acumulan las metricas por jugador en un diccionario
5. **Calculo de indicadores**: Se derivan porcentajes de efectividad
6. **Limpieza**: Se eliminan jugadores con menos de 5 pases intentados

## 3. Metricas Calculadas

| Metrica | Formula | Utilidad para Scouting |
|---------|---------|----------------------|
| Efectividad de Pases | (Pases Completados / Pases Intentados) x 100 | Mide precision y decision en la distribution |
| Efectividad de Regates | (Regates Exitosos / Regates Intentados) x 100 | Mide capacidad de superar al rival en el 1v1 |
| Volumen de Presiones | Total de presiones registradas | Indica intensidad defensiva y trabajo sin pelota |
| Participacion en Ataque | Tiros + Regates + Pases al ultimo tercio | Mide involucramiento ofensivo |

## 4. Visualizacion (Power BI)

Los datos procesados se cargan en Power BI para crear un dashboard interactivo que permite:

- Comparar jugadores por posicion y equipo
- Filtrar por metricas especificas
- Identificar perfiles de jugadores segun el perfil buscado
- Analizar distribucion de rendimiento por seleccion

## 5. Reproduccion

Para replicar el analisis:

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar el extractor
python extractor_futbol.py

# 3. Abrir scouting.pbix en Power BI y cargar el CSV generado
```

**Nota**: La API de StatsBomb es gratuita para datos no competitivos. Algunos eventos premium pueden no estar disponibles.
