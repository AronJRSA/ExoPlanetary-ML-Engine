# Archivo: modules/analysis.py
from settings import TERRESTRES_RADIO, TERRESTRES_MASA, GIGANTES_GASEOSOS_MASA, TEMP_MIN_K, TEMP_MAX_K
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
def clasificar_mundos(df):
    def categorizar(row):
        # Usamos las constantes del archivo settings
        if row['pl_rade'] < TERRESTRES_RADIO and row['pl_bmasse'] < TERRESTRES_MASA:
            return 'Terrestre / Super-Tierra'
        elif row['pl_bmasse'] > GIGANTES_GASEOSOS_MASA:
            return 'Gigante Gaseoso'
        else:
            return 'Neptuniano / Medio'

    df['tipo_planeta'] = df.apply(categorizar, axis=1)
    return df

def analizar_habitabilidad(df):
    """
    Identifica planetas terrestres en la zona de temperatura ideal.
    """
    # Filtramos: Solo terrestres Y que estén en el rango de temperatura
    condicion = (
        (df['tipo_planeta'] == 'Terrestre / Super-Tierra') & 
        (df['pl_eqt'] >= TEMP_MIN_K) & 
        (df['pl_eqt'] <= TEMP_MAX_K)
    )
    
    df['habitable'] = condicion
    return df
def limpiar_tipo_espectral(df):
    df['clase_estelar'] = df['st_spectype'].str[0].str.upper()
    
    # Filtramos para quedarnos solo con las clases estándar de Harvard
    clases_validas = ['O', 'B', 'A', 'F', 'G', 'K', 'M']
    df = df[df['clase_estelar'].isin(clases_validas)].copy()
    
    return df
def ejecutar_clustering(df, n_clusters=4):

    cols = ['pl_bmasse', 'pl_rade', 'pl_eqt']
    df_clus = df.dropna(subset=cols).copy()

    scaler = StandardScaler()
    datos_escalados = scaler.fit_transform(df_clus[cols])

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df_clus['cluster_ia'] = kmeans.fit_predict(datos_escalados)
    
    return df_clus