# Archivo: settings.py
import os
INPUT_CSV = "data/input/PSCompPars_2026.03.28_01.37.47.csv"

#
COLUMNAS_PLANETARIAS = [
    'pl_name', 'discoverymethod', 'disc_year', 'pl_rade', 
    'pl_bmasse', 'pl_orbsmax', 'pl_eqt', 'st_teff', 
    'sy_dist', 'sy_pnum','st_spectype'
]

# pl_name	Nombre del planeta	Identificador único (ej. Proxima Centauri b).
# discoverymethod	Método de descubrimiento	Para la gráfica de evolución tecnológica.
# disc_year	Año de descubrimiento	Para ver la historia de la exploración espacial.
# pl_rade	Radio Planetario (Tierras)	Clave: Nos dice si es rocoso ($<1.5$) o gaseoso.
# pl_bmasse	Masa Planetaria (Tierras)	Para calcular la densidad y la gravedad superficial.
# pl_orbsmax	Semieje mayor (UA)	Distancia a su estrella (fundamental para habitabilidad).
# pl_eqt	Temperatura de Equilibrio (K)	Para saber si está en la "Zona de Goldilocks".
# st_teff	Temp. Efectiva de la Estrella	Para clasificar si su "sol" es como el nuestro o una enana roja.
# sy_dist	Distancia al Sistema (pc)	Qué tan lejos está de nosotros (en parsecs).
# sy_pnum	Número de planetas	Para identificar sistemas multi-planetarios.
#st_spectype
# Archivo: settings.py (Añadir al final)

# obj1
TERRESTRES_RADIO = 1.5  
TERRESTRES_MASA = 5.0   
GIGANTES_GASEOSOS_MASA = 50.0

OUTPUT_DIR = os.path.join(os.getcwd(), 'data', 'output')
GRAFICA_OBJ1_PATH = os.path.join(OUTPUT_DIR, "grafica_masa_radio.png")
#obj 2
TEMP_MIN_K = 200  # Límite frío
TEMP_MAX_K = 320  # Límite cálido
GRAFICA_OBJ2_PATH = os.path.join(OUTPUT_DIR, "distribucion_temperatura.png")
#3
GRAFICA_OBJ3_PATH = os.path.join(OUTPUT_DIR, "evolucion_temporal.png")
#4
GRAFICA_OBJ4_PATH = os.path.join(OUTPUT_DIR, "tipo_estelar_histograma.png")
#5
GRAFICA_OBJ5_PATH = os.path.join(OUTPUT_DIR, "Agrupamiento Inteligente.png")
#reporte
REPORTE_WORD_PATH = os.path.join(OUTPUT_DIR, "Reporte_Exoplanetas_Final.docx")