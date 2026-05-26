import pandas as pd
import numpy as np
from scipy import stats
import joblib

def evaluar_calidad_datos(df):
    nulos = df.isnull().sum()
    z_scores = np.abs(stats.zscore(df['DBO_salida_mg_L'].dropna()))
    outliers = np.sum(z_scores > 3)
    
    reporte = {
        "nulos": nulos,
        "outliers_detectados": outliers,
        "resumen_estadistico": df.describe()
    }
    
    joblib.dump(reporte, 'reporte_calidad.pkl')
    return reporte

def generar_reporte_operaciones(df):
    columnas_op = [
        'fecha_registro', 'planta', 'caudal_entrada_m3_d', 
        'DBO_entrada_mg_L', 'DBO_salida_mg_L', 
        'energia_aeracion_kWh', 'lodos_generados_kg_d'
    ]
    df_operaciones = df[columnas_op].copy()
    
    df_operaciones['eficiencia_remocion_%'] = np.round(
        (1 - (df_operaciones['DBO_salida_mg_L'] / df_operaciones['DBO_entrada_mg_L'])) * 100, 2
    )
    
    df_operaciones.to_csv("reporte_operaciones.csv", index=False)

def generar_reporte_ambiental(df):
    columnas_amb = ['fecha_registro', 'planta', 'DBO_salida_mg_L', 'cumplimiento_norma']
    df_ambiental = df[columnas_amb].copy()
    
    df_ambiental.to_csv("reporte_ambiental.csv", index=False)