# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 12:02:30 2021

@author: FranJa
"""

import numpy as np
import pandas as pd

# Tratamiento de Series y DataFrames como ndarrays
serie = pd.Series( {'a':1,'b':78,'c':4,'d':6,'e':21,'f':2,'g':76,'h':5} )
print("serie:\n", serie, "\n")

mapping = { 'var1': pd.Series(serie, dtype=np.int32) , 'var2': pd.Series(serie, dtype=np.string_) }
dataframe = pd.DataFrame(mapping)
print("dataframe: \n", dataframe, "\n")


# Operaciones con escalares

# serie += 2
# print("Serie + 2:\n", serie, "\n")

# serie -= 2
# print("Serie - 2:\n", serie, "\n")

# serie = serie * 2
# print("Serie * 2:\n", serie, "\n")

# serie = 1/serie
# print("1/Serie:\n", serie, "\n")

# dataframe = dataframe * 2
# print("dataframe * 2:\n", dataframe, "\n")

serie1 = serie[:]
print("\n Serie1: \n",serie1) 

serie1['i'] = 7
print("\n Serie1: \n",serie1) 

dataframe1 = dataframe
dataframe1['var3'] = [1,2,3,4,5,6,7,8]
print("\n dataframe1: \n",dataframe1) 

serie2 = serie + serie1
print("\n serie2: \n",serie2) 

dataframe2 = dataframe + dataframe1
print("\n dataframe2: \n",dataframe2) 

dataframe3 = dataframe.T
print("\n dataframe3: \n",dataframe3) 

