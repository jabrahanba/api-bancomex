#Librerias y frameworks:
import pandas as pd
import etl_functions as etl
from dotenv import load_dotenv
import os
token = ''
load_dotenv("config.env")
token = os.getenv("TOKEN")

# **E- Extracción**
# Definir la lista de series a descargar
series = ['SF44042','SF44043','SF44044','SF43695','SF43702','SF43696']
df_final = pd.DataFrame()
# Token
token = token 
for serie in series:
    df = etl.dload_bmx_serie(serie, token)
    if df_final.empty:
        df_final = df
    else:
        df_final = pd.concat([df_final, df], axis=1)

# **T- Transformación**
df_final = df_final.fillna(0)
df_final = df_final.reset_index()
fechaInicio = input("Por favor, ingresa fecha de inicio de la carga en el formato AAAA-MM-DD: ")
fechaFin = input("Por favor, ingresa fecha de fin de la carga en el formato AAAA-MM-DD: ")
df_final = df_final[(df_final['fecha'] >= fechaInicio) & (df_final['fecha'] <= fechaFin)]


# **L- Carga**

#Crear tabla vacia
with etl.conn.cursor() as cursor:
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS jabrahanba_coderhouse.bancoMex (
        fecha DATE,
        SF44042 NUMERIC(16,2),
	    SF44043 NUMERIC(16,2),
	    SF44044 NUMERIC(16,2),
	    SF43695 NUMERIC(16,2),
	    SF43702 NUMERIC(16,2),
	    SF43696 NUMERIC(16,2)
    )
'''
    cursor.execute(create_table_query)
    etl.conn.commit()

#Cargar tabla vacia.
filas_bancoMex = [tuple(df_final.iloc[i].values) for i in range (df_final.shape[0])]
fill_bancoMex = '''
INSERT INTO jabrahanba_coderhouse.bancoMex (fecha, SF44042, SF44043, SF44044, SF43695, SF43702, SF43696)
VALUES (%s, %s, %s, %s, %s, %s, %s)
'''
with etl.conn.cursor() as cursor:
    cursor.executemany(fill_bancoMex, filas_bancoMex)
    etl.conn.commit()
