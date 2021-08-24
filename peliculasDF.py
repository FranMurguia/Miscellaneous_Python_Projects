# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:42:37 2021

@author: FranJa
"""

import numpy as np
import pandas as pd

peliculas = pd.DataFrame(
    {'Año': [2014,2014,2013,2013, 2001],
     'Valoracion':[6,None,8.75,None, 8.9],
     'Presupuesto':[160,250,100,None, 93],
     'Director':['Gareth Edwards', 'Peter Jackson', 'Mastin Scorsese', 'Alfosno Cuarón', 'Peter Jackson'],
     'Título': ['Godzilla', 'El Hobbit III---', 'El lobo de Wall Street', 'Gravity', 'Lord Of the Rings']}
    )

print(peliculas, "\n")

print( peliculas.pivot("Año","Director","Título") ,"\n")