# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:49:49 2024

@author: Usuario
"""
import pandas as pd
import numpy as np
datos=pd.read_csv('netflix_titles.csv')
#Ves encabezado de las tablas
#print(datos.info())
#Se visualiza las 5 primeras filas
print(datos.head(30))
#count= numeros de valores no nulos
#mean= promedio de valores 
#std= desviación estandar
#min= valor minimo
#percentiles 25% 50% 75% Q1 Q2 QU3
#max= valor máximo
#print(datos.describe())
#reemplaza valor NaN a "0"
#df=datos.replace(np.nan,"0")
#Pero de forma más directa sería
 #df2=datos.fillna("0")
print(datos['title'])