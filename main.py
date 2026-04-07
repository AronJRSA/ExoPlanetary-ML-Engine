# main.py
from modules import ingestion, cleaning, analysis, visualization, export 
from settings import GRAFICA_OBJ1_PATH, GRAFICA_OBJ2_PATH, GRAFICA_OBJ3_PATH, GRAFICA_OBJ4_PATH, GRAFICA_OBJ5_PATH

def run():
    df_bronze = ingestion.carga_de_datos()
    df_silver = cleaning.filtrar_columnas_relevantes(df_bronze)  
    
    # 2. Análisis: Clasificar 
    df_silver = df_silver.dropna(subset=['pl_rade', 'pl_bmasse'])
    df_gold = analysis.clasificar_mundos(df_silver)
    visualization.graficar_y_guardar_clasificacion(df_gold, path_save=GRAFICA_OBJ1_PATH)
    #3
    df_gold = analysis.analizar_habitabilidad(df_gold)
    visualization.graficar_zona_habitable(df_gold, GRAFICA_OBJ2_PATH)
    #4
    visualization.graficar_evolucion_temporal(df_gold, GRAFICA_OBJ3_PATH)
    #5
    df_gold = analysis.limpiar_tipo_espectral(df_gold)
    visualization.graficar_tipos_estelares(df_gold, GRAFICA_OBJ4_PATH)


    df_clusters = analysis.ejecutar_clustering(df_gold)
    
    # Ahora, la gráfica de ML 
    visualization.graficar_clusters(df_clusters,  GRAFICA_OBJ5_PATH)


    # . Exportación: Generar el Word
    export.generar_reporte_word(df_gold, GRAFICA_OBJ1_PATH, GRAFICA_OBJ2_PATH, GRAFICA_OBJ3_PATH, GRAFICA_OBJ4_PATH, GRAFICA_OBJ5_PATH)
    
    print("Reporte generado en data/output.")

if __name__ == "__main__":
    run()
