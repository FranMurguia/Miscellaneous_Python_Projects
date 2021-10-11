# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 09:41:15 2021

@author: FranJa
"""

import numpy as np
import pandas as pd

# Estructura de datos

""" Series (Estructura de datos unidimensional que puede contener
cualquier tipo de dato de Numpy)
"""

# Serie desde escalar
serie = pd.Series(5)

# Serie desde secuencia
serie_1 = pd.Series([1,2,3,4,5], dtype = np.string_)
print("Serie_1:\n", serie_1, "\n")

# Serie desde ndarray
array = np.array([2,4,6,8,10])
serie_2 = pd.Series(array)
print("Serie_2:\n", serie_2, "\n")

#Serie con índice preestablecido
serie_3 = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])
print("Serie_3:\n", serie_3, "\n")

# Serie desde diccionario
serie_4 = pd.Series( {'a':1,'b':78,'c':4,'d':6,'e':21,'f':2,'g':76,'h':5} )
print("Serie_4:\n", serie_4, "\n")

# Elementos de una serie
print(serie_4.values, "\n")
print(serie_4.index, "\n")

# Los índices son INMUTABLES (o cambiamos todos o ninguno)
serie_5 = serie_4
print("Serie_5:\n", serie_5, "\n")
serie_5.index = ['1','2','3','4','5','6','7','8']
print("Serie_5:\n", serie_5, "\n")

# DataFrame
"""
Estructura de tabla, filas y columnas ordenadas.
las filas y columnas tienen índice independientes.
cada columna puede tener un tipo de Numpy diferente.
Puede ser visto como un diccionario de Series.
"""

dataframe_1 = pd.DataFrame({'var1':[1,2,3],'var2':[1.0,2.0,3.0],'var3':['uno','dos','tres'],})
print("DataFrame_1: \n", dataframe_1, "\n")

dataframe_2 = pd.DataFrame( { 'var1':pd.Series([1,2,3], dtype=np.float64) , 'var2':pd.Series(['a','b']) } )
print("DataFrame_2: \n", dataframe_2, "\n")

dataframe_3 = pd.DataFrame( np.arange(16).reshape(4,4), dtype=np.float64 )
print("DataFrame_3: \n", dataframe_3, "\n")

# Dataframe desde ndarray con índices para filas y columnas
dataframe_4 = pd.DataFrame( np.arange(16).reshape(4,4), index = ['f1','f2','f3','f4'], columns= ['c1','c2','c3','c4'] )
print("DataFrame_4: \n", dataframe_4, "\n")

# Elementos de DataFrame
print(dataframe_3.values, "\n")
print(dataframe_3.index, "\n")
print(dataframe_3.columns, "\n")

# Los índices son INMUTABLES (o cambiamos todos o ninguno)
dataframe_5 = dataframe_4
print("dataframe_5:\n", dataframe_5, "\n")
dataframe_5.index = [5,6,7,8]
print("dataframe_5:\n", dataframe_5, "\n")
dataframe_5.columns = ['col1','col2','col3','col4']
print("dataframe_5:\n", dataframe_5, "\n")

# Cambiar una única columna:
mapping = {"var1": "a"}
dataframe_6 = dataframe_1.rename(columns=mapping)
print("dataframe_6:\n", dataframe_6, "\n")



