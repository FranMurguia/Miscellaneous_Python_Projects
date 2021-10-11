# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 01:33:39 2021

@author: FranJa
"""

def EuclideanGDC(a, b):
    
    while(b != 0):
        temp = b
        b = a % b
        a = temp
    return a

# Euclid's Algorithm for GCD

a_values = (55, 27, 3, 14, 500, 30, 874)
b_values = (5, 45, 15, 49, 12, 18, 1944)

for i in range(0, len(a_values)):
    print(EuclideanGDC(a_values[i], b_values[i]))
    
        