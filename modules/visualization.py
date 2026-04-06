# modules/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns
from settings import TERRESTRES_MASA, TERRESTRES_RADIO, TEMP_MIN_K, TEMP_MAX_K

def graficar_y_guardar_clasificacion(df, path_save):
    """
    Objetivo 1: Scatter Plot de Masa vs Radio con colores por tipo.
    """
    plt.figure(figsize=(12, 7))
    
    # El Scatter Plot pro
    sns.scatterplot(data=df, x='pl_bmasse', y='pl_rade', 
                    hue='tipo_planeta', palette='magma', alpha=0.7)
    
    # Dibujamos los límites de las "Tierras" para que se vea científico
    plt.axvline(TERRESTRES_MASA, color='red', linestyle='--', alpha=0.3, label='Límite Masa Tierra')
    plt.axhline(TERRESTRES_RADIO, color='blue', linestyle='--', alpha=0.3, label='Límite Radio Tierra')

    plt.xscale('log')
    plt.yscale('log')
    plt.title(" Objetivo 1: Clasificación de Exoplanetas (Masa vs Radio)", fontsize=14)
    plt.xlabel("Masa (Tierras) [Log]")
    plt.ylabel("Radio (Tierras) [Log]")
    plt.legend(title="Tipo de Mundo", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, which="both", ls="-", alpha=0.1)
    plt.tight_layout()
    plt.savefig(path_save, dpi=300)
    plt.show()
def graficar_zona_habitable(df, path_save):
    plt.figure(figsize=(10, 6))
    
    df_terrestres = df[df['tipo_planeta'] == 'Terrestre / Super-Tierra']
    
    sns.kdeplot(df_terrestres['pl_eqt'], fill=True, color="green", label="Planetas Terrestres")
    
    # 3. CORRECCIÓN AQUÍ: Asegúrate de que los nombres coincidan con settings.py
    # Si en settings.py se llaman TEMP_MIN_K, úsalos así:
    plt.axvspan(TEMP_MIN_K, TEMP_MAX_K, color='yellow', alpha=0.3, label="Zona Goldilocks")
    
    plt.title(" Distribución de Temperatura en Mundos Rocosos", fontsize=14)
    plt.xlabel("Temperatura de Equilibrio (K)")
    plt.ylabel("Densidad")
    plt.legend()
    
    plt.savefig(path_save, dpi=300)
    plt.show()
def graficar_evolucion_temporal(df, path_save):
    plt.figure(figsize=(12, 6))
    
    # Agrupamos por año y método de descubrimiento
    evolucion = df.groupby(['disc_year', 'discoverymethod']).size().unstack().fillna(0)
    
    evolucion.plot(kind='bar', stacked=True, ax=plt.gca(), colormap='viridis')
    
    plt.title(" Evolución de los Descubrimientos de Exoplanetas", fontsize=14)
    plt.xlabel("Año de Descubrimiento")
    plt.ylabel("Número de Planetas")
    plt.legend(title="Método", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    plt.savefig(path_save, dpi=300)
    plt.show()
def graficar_tipos_estelares(df, path_save):
    plt.figure(figsize=(10, 6))
    
    # Definimos colores astronómicos aproximados
    colores_estrellas = {
        'O': '#0055FF', # Azul Eléctrico (Súper Caliente)
        'B': '#6699FF', # Azul Claro Saturado
        'A': '#222222', # Gris Casi Negro (Para que resalte la "Estrella Blanca")
        'F': '#DDAA00', # Oro/Mostaza Oscuro (Blanco-Amarillento)
        'G': '#FF8800', # Naranja Intenso (Como nuestro Sol, pero visible)
        'K': '#FF4400', # Naranja-Rojo Fuerte
        'M': '#CC0000'  # Rojo Sangre (Enanas Rojas frías)
    }
    
    orden = ['O', 'B', 'A', 'F', 'G', 'K', 'M']
    sns.countplot(data=df, x='clase_estelar', order=orden, palette=colores_estrellas)
    
    plt.title("Distribución de Planetas por Tipo de Estrella", fontsize=14)
    plt.xlabel("Clasificación Espectral (O-M)")
    plt.ylabel("Cantidad de Planetas Detectados")
    plt.grid(axis='y', alpha=0.2)
    
    plt.savefig(path_save, dpi=300)
    plt.show()
def graficar_clusters(df, path_save):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='pl_bmasse', y='pl_rade', hue='cluster_ia', palette='viridis', s=100)
    plt.title('Agrupamiento Inteligente de Exoplanetas (K-Means)')
    plt.xlabel('Masa (Tierras)')
    plt.ylabel('Radio (Tierras)')
    plt.xscale('log') # Escala logarítmica porque hay mucha diferencia de tamaños
    plt.savefig(path_save)
    plt.close()