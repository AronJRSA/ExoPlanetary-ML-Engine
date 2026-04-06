# Archivo: ingestion.py
import pandas as pd
import settings as st

def carga_de_datos():
    df = pd.read_csv(st.INPUT_CSV, comment='#')
    return df