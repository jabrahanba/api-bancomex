import pandas as pd
import numpy as np
import requests 
import psycopg2
from dotenv import load_dotenv
import os
token = ''
load_dotenv("config.env")

def dload_bmx_serie(serie, token):
    '''Esta funcion devuelve un DataFrame extraido a través de la API del banco de México
     tomando como parametros el nombre de la serie y el rango de fechas. 
     El catalogo adjuntado previamente otorga los códigos alimentar la función'''
        
    url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/'+serie+'/datos/'
    headers = {'Bmx-Token':token} #Asi lo establece la web
    response = requests.get(url, headers=headers)
    status = response.status_code
    if status != 200: #código de estado http 200 significa OK.
        return print(f'Error en la consulta, codigo {status}')
    rawData = response.json() #aca es donde trae la info.
    data = rawData['bmx']['series'][0]['datos'] #con el método de corchetes se extraen los elementos que se necesitan de response.
    df = pd.DataFrame(data)
    df['dato'] = df['dato'].replace('N/E', np.nan).str.replace(',', '').astype(float)
    df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')
    df.set_index('fecha', inplace=True)
    df.rename(columns={'dato': serie}, inplace=True)
    return df

def dload_bcrp(serie):
    '''Esta funcion devuelve un DataFrame extraido a través de la API del banco de Perú
     tomando como parametros el nombre de la serie. 
     El catalogo adjuntado previamente otorga los códigos alimentar la función'''
        
    url = 'https://estadisticas.bcrp.gob.pe/estadisticas/series/api/'+serie+'/json'
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
    else:
        print("Error en la solicitud:", response.status_code)
    data = json_data['periods']
    df = pd.DataFrame(data)
    df['values'] = df['values'].apply(lambda x: x[0])
    df = df.rename(columns={'name': 'fecha', 'values':serie})
    df['fecha'] = pd.to_datetime(df['fecha'], format='%d.%b.%y').dt.strftime('%Y-%m-%d')
    return df


host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")

conn = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database,
)