import pandas as pd
from statsbombpy import sb
from tqdm import tqdm  # Muestra una barra de progreso en la terminal

def generar_dataset_scouting():
    print("--- 1. Conectando a StatsBomb y obteniendo partidos de Qatar 2022 ---")
    # Mundial es Competencia 43, Temporada 106
    id_competencia = 43
    id_temporada = 106
    
    partidos = sb.matches(competition_id=id_competencia, season_id=id_temporada)
    lista_match_ids = partidos['match_id'].tolist()
    print(f"Se encontraron {len(lista_match_ids)} partidos para procesar.")
    
    # Diccionario temporal para acumular las estadísticas por jugador
    stats_jugadores = {}

    print("\n--- 2. Procesando partidos (Extrayendo eventos de rendimiento) ---")
    # Usamos tqdm para ver el progreso real en la terminal de VS Code
    for match_id in tqdm(lista_match_ids):
        try:
            eventos = sb.events(match_id=match_id)
            
            # Filtramos solo los eventos que nos dan métricas de rendimiento técnico-táctico
            eventos_interes = eventos[eventos['type'].isin(['Pass', 'Shot', 'Pressure', 'Duel', 'Dribble'])]
            
            for idx, row in eventos_interes.iterrows():
                jugador = row.get('player')
                equipo = row.get('team')
                tipo_evento = row.get('type')
                
                # Si el evento no tiene jugador asignado (raro), lo saltamos
                if pd.isna(jugador):
                    continue
                
                # Inicializamos el jugador en nuestro diccionario si es la primera vez que aparece
                if jugador not in stats_jugadores:
                    stats_jugadores[jugador] = {
                        'Jugador': jugador,
                        'Equipo': equipo,
                        'Pases_Intentados': 0,
                        'Pases_Completados': 0,
                        'Tiros_Totales': 0,
                        'Goles': 0,
                        'Presiones': 0,
                        'Regates_Intentados': 0,
                        'Regates_Exitosos': 0,
                        'Quites_Intentados': 0
                    }
                
                # --- Lógica de acumulación de métricas ---
                if tipo_evento == 'Pass':
                    stats_jugadores[jugador]['Pases_Intentados'] += 1
                    # En StatsBomb, si 'pass_outcome' es NaN, el pase fue completado con éxito
                    if pd.isna(row.get('pass_outcome')):
                        stats_jugadores[jugador]['Pases_Completados'] += 1
                        
                elif tipo_evento == 'Shot':
                    stats_jugadores[jugador]['Tiros_Totales'] += 1
                    if row.get('shot_outcome') == 'Goal':
                        stats_jugadores[jugador]['Goles'] += 1
                        
                elif tipo_evento == 'Pressure':
                    stats_jugadores[jugador]['Presiones'] += 1
                    
                elif tipo_evento == 'Dribble':
                    stats_jugadores[jugador]['Regates_Intentados'] += 1
                    if row.get('dribble_outcome') == 'Complete':
                        stats_jugadores[jugador]['Regates_Exitosos'] += 1
                        
                elif tipo_evento == 'Duel':
                    # Filtramos duelos que sean específicamente intentos de quitar la pelota (Tackle)
                    if row.get('duel_type') == 'Tackle':
                        stats_jugadores[jugador]['Quites_Intentados'] += 1
                        
        except Exception as e:
            print(f"Error procesando el partido {match_id}: {e}")
            continue

    # --- 3. Convertir a DataFrame y calcular porcentajes/UX ---
    print("\n--- 3. Consolidando y limpiando la base de datos de Scouting ---")
    df_scouting = pd.DataFrame(list(stats_jugadores.values()))
    
    # Calculamos la efectividad de pases
    df_scouting['Efectividad_Pases_%'] = (df_scouting['Pases_Completados'] / df_scouting['Pases_Intentados'] * 100).round(1)
    df_scouting['Efectividad_Pases_%'] = df_scouting['Efectividad_Pases_%'].fillna(0) # Por si no dio pases
    
    # Calculamos efectividad de regates
    df_scouting['Efectividad_Regates_%'] = (df_scouting['Regates_Exitosos'] / df_scouting['Regates_Intentados'] * 100).round(1)
    df_scouting['Efectividad_Regates_%'] = df_scouting['Efectividad_Regates_%'].fillna(0)

    # Filtramos jugadores testimoniales (que hayan intentado menos de 5 pases o acciones en todo el mundial)
    # Esto limpia el dataset para el usuario final (el DT)
    df_scouting = df_scouting[df_scouting['Pases_Intentados'] >= 5]

    # Guardamos el archivo final que va a alimentar a Power BI
    nombre_archivo = 'scouting_qatar_2022.csv'
    df_scouting.to_csv(nombre_archivo, index=False, encoding='utf-8-sig')
    print(f"\n¡Listo, jefe! Archivo '{nombre_archivo}' generado con {len(df_scouting)} jugadores.")

if __name__ == "__main__":
    generar_dataset_scouting()
    