# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 15:00:15 2021

@author: FranJa
"""

import numpy as np
import pandas as pd

# Especificando dimensiones
m_empty_array_1 = np.empty((3,2), dtype = np.unicode)
print(m_empty_array_1)

# Copiando dimensiones y tipo desde otra estructura
m_empty_array_2 = np.empty_like([1,2,3,4,5])
print(m_empty_array_2)

# Array de 1's
m_empty_array_3 = np.ones((4,5))
print(m_empty_array_3)

# Array de 1's
m_empty_array_4 = np.zeros((4,5))
print(m_empty_array_4)

# Copiando dimensiones y tipo desde otra estructura
m_empty_array_5 = np.zeros_like([1,2,3,4,5])
print(m_empty_array_5)

# Identidad
m_empty_array_6 = np.identity(5)
print(m_empty_array_6)

# Matriz triángular
m_empty_array_7 = np.eye(5, k = 2)
print(m_empty_array_7)

# Matriz no cuadrada con 1's en la diagonal específicada
m_empty_array_8 = np.eye(4,3, k = -2)
print(m_empty_array_8)

# Array secuencial
m_array_secuencia_1 = np.arange(15)
print(m_array_secuencia_1)

# Unidimensional
m_array_secuencia_2 = np.array([1,2,3,4,5])
print(m_array_secuencia_2)

# Multidimesional
m_array_secuencia_3 = np.array( [ [1,2,3,4,5], [6,7,8,9,10] ])
print(m_array_secuencia_3)

array_inicial_enteros = np.array([1,2,3,4,5], dtype = np.int32)
print(array_inicial_enteros)

array_inicial_flotantes = np.array(array_inicial_enteros, dtype = np.float64)
print(array_inicial_flotantes)

array_inicial_strings = np.array(array_inicial_enteros, dtype = np.unicode)
print(array_inicial_strings)

""" 
array.dtype: Tipo del contenido del ndarray
array.ndim: Núimero de dimensiones
array.shape: Estructura/forma 
array.size: Número total de elementos

"""
