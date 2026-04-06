# Archivo: cleaning.py
import settings as st
def filtrar_columnas_relevantes(df):
    df_filtrado = df[st.COLUMNAS_PLANETARIAS].copy()
    return df_filtrado