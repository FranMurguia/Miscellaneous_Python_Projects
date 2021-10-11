# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 12:32:35 2021

@author: FranJa
"""

import pandas as pd
import numpy as np

serie = pd.Series( {'a':1,'b':78,'c':4,'d':6,'e':21,'f':2,'g':76,'h':5} )
print("serie:\n", serie, "\n")

dataframe = pd.DataFrame( np.arange(16).reshape(4,4), index = ['f1','f2','f3','f4'], columns= ['c1','c2','c3','c4'] )
print("dataframe: \n", dataframe, "\n")


# print("Serie.a: \n", serie.a, "\n")
# print("dataframe.c1: \n", dataframe.c1, "\n")

# print("serie[0]: \n", serie[0], "\n")
# print("serie[0:2]: \n", serie[0:2], "\n")
# print("serie['d']: \n", serie['d'], "\n")
# print("serie['a':'d']: \n", serie['a':'d'], "\n")
# print("serie[['a','d']]: \n", serie[['a','d']], "\n")

# # .loc trabaja con las 'keys'
# print(" dataframe.loc['f1'] \n", dataframe.loc['f1'], "\n")
# print(" dataframe.loc['f1', 'c1']\n", dataframe.loc['f1', 'c1'], "\n")
# print(" dataframe.loc[:, 'c1']\n", dataframe.loc[:, 'c1'], "\n")

# # .iloc trabaja con las 'índices'
# print(" dataframe.iloc[0] \n", dataframe.iloc[0], "\n")
# print(" dataframe.iloc[3,2] \n", dataframe.iloc[3,2], "\n")
# print(" dataframe.iloc[:,2] \n", dataframe.iloc[:,2], "\n")

# # Índices jerárquicos
# peliculas = pd.DataFrame(
#     {'Valoracion':[6,None,8.75,None],
#      'Presupuesto':[160,250,100,None],
#      'Director':['Peter Jackson', 'Gareth Edwards', 'Mastin Scorsese', 'Alfosno Cuarón']},
#     index = [ [2014,2014,2013,2013], ['Godzilla', 'El Hobbit III', 'El lobo de Wall Street', 'Gravity'] ]
#     )

# print(peliculas, "\n")

# # Indexación total
# print(peliculas.loc[ (2014,'Godzilla') ] , "\n")

# # indexación parcial
# print(peliculas.loc[ 2014 ] , "\n")

# Reindexación, establecimiento y descarte de índices

# Reordenación del índice de una Serie
print( serie.reindex( ['a','b','c','h','e','f','g','d']) , "\n")
print( serie.reindex( ['a','b','c','h','e','f','g','d','i']) , "\n")
print( serie.reindex( ['a','b','c','h','e','f','g','d','i'], fill_value = 0 ) , "\n")

# Selección del índice de un DataFrame
print( dataframe.reindex(['f1','f3']) , "\n")
print( dataframe.reindex(['f1','f3', 'f6']) , "\n")
print( dataframe , "\n")
print( dataframe.reindex(['f1','f3', 'f10'], method = 'ffill') , "\n")
print( dataframe , "\n")
print( dataframe.reindex(['f1','f3', 'f10'], method = 'bfill') , "\n")

print( dataframe.reindex( columns=['c1','c3']) , "\n")
print( dataframe.reindex( columns=['c1','c3', 'c6']) , "\n")
print( dataframe.reindex( columns=['c1','c3', 'c10'], method = 'ffill') , "\n")
print( dataframe.reindex( columns=['c1','c3', 'c10'], method = 'bfill') , "\n")

print( dataframe.reset_index(), "\Yn")
print( dataframe.set_index(['c1']),"\n")

