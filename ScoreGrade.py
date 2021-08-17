# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 10:35:53 2021

@author: FranJa
"""

# Prompt for a score between 0.0 and 1.0
m_score = input("Enter Score: ")

# Try catch a float number
try:
    s = float(m_score)
except:
    s = 'NAN'

if(s == 'NAN'):
    print('Invalid input')
elif(s < 0 or s>1):
    print('Out of range')
elif(s >= 0.9):
    print('A')
elif(s >= 0.8):
    print('B')
elif(s >= 0.7):
    print('C')
elif(s >= 0.6):
    print('D')
else:
    print('F')