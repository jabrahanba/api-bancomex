#Librerias y frameworks:
import pandas as pd
import etl_functions as etl
from dotenv import load_dotenv
import os
token = ''
load_dotenv("config.env")
token = os.getenv("TOKEN")

# **E- Extracción**
##BMX
# Definir la lista de series a descargar
series = ['SF343410','SF63528']
df_final_bmx = pd.DataFrame()
# Token
token = token 
for serie in series:
    df = etl.dload_bmx_serie(serie, token)
    if df_final_bmx.empty:
        df_final_bmx = df
    else:
        df_final_bmx = pd.concat([df_final_bmx, df], axis=1)

##BPERU
series = ['PD04645PD','PD04646PD','PD04647PD','PD04648PD']
df_final_peru = etl.dload_bcrp(series[0])
for serie in series[1:]:
    df_series_peru = etl.dload_bcrp(serie)
    df_final_peru = pd.merge(df_final_peru, df_series_peru, on='fecha', how='inner')

# **T- Transformación**
fechaInicio = input("Por favor, ingresa fecha de inicio de la carga en el formato AAAA-MM-DD: ")
fechaFin = input("Por favor, ingresa fecha de fin de la carga en el formato AAAA-MM-DD: ")
#BMX
df_final_bmx = df_final_bmx.fillna(0)
df_final_bmx = df_final_bmx.reset_index()
df_final_bmx = df_final_bmx.rename(columns={'SF343410': 'dolar_peso_cierre', 'SF63528':'dolar_peso_hist'})
df_final_bmx = df_final_bmx[(df_final_bmx['fecha'] >= fechaInicio) & (df_final_bmx['fecha'] <= fechaFin)]
#BPERU
df_final_peru = df_final_peru.fillna(0)
df_final_peru = df_final_peru.reset_index()
df_final_peru = df_final_peru.rename(columns={'PD04645PD':'compra_soles_dolar','PD04646PD':'venta_soles_dolar','PD04647PD':'compra_soles_euro','PD04648PD':'venta_soles_euro'})
#fechas en el mismo formato.
df_final_bmx['fecha'] = pd.to_datetime(df_final_bmx['fecha'])
df_final_peru['fecha'] = pd.to_datetime(df_final_peru['fecha'])

#Fusionar
df_final = pd.merge(df_final_bmx, df_final_peru, on='fecha', how='inner')
columnas = ['dolar_peso_cierre', 'dolar_peso_hist', 'compra_soles_dolar', 'venta_soles_dolar', 'compra_soles_euro', 'venta_soles_euro']
df_final[columnas] = df_final[columnas].astype('Float64')
df_final = df_final.reset_index(drop=True)
df_final = df_final.drop('index', axis=1)
print(df_final)
print(df_final.dtypes)

# **L- Carga**

#Crear tabla vacia
with etl.conn.cursor() as cursor:
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS jabrahanba_coderhouse.tasas_cambio (
        fecha DATE,
        dolar_peso_cierre NUMERIC(16,2),
	    dolar_peso_hist NUMERIC(16,2),
	    compra_soles_dolar NUMERIC(16,2),
	    venta_soles_dolar NUMERIC(16,2),
	    compra_soles_euro NUMERIC(16,2),
	    venta_soles_euro NUMERIC(16,2)
    )
'''
    cursor.execute(create_table_query)
    etl.conn.commit()

#Cargar tabla vacia.
filas_tasas_cambio = [tuple(df_final.iloc[i].values) for i in range (df_final.shape[0])]
fill_tasas_cambio = '''
INSERT INTO jabrahanba_coderhouse.tasas_cambio (fecha, dolar_peso_cierre, dolar_peso_hist, compra_soles_dolar, venta_soles_dolar, compra_soles_euro, venta_soles_euro)
VALUES (%s, %s, %s, %s, %s, %s, %s)
'''
with etl.conn.cursor() as cursor:
    cursor.executemany(fill_tasas_cambio, filas_tasas_cambio)
    etl.conn.commit()