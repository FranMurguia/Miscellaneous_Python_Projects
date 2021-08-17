# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:55:12 2021

@author: FranJa
"""

m_largest = None
m_smallest = None

while True:
    num = input("Enter a number: ")
    
    if num == "done":
        break
        
    try:
        n = float(num)
    except:
        print('Invalid input')
        continue
    
    if(m_largest is None):
        m_largest = n
        
    if(m_smallest is None):
        m_smallest = n
    
    if(m_largest <= n):
        m_largest = n
        
    if(m_smallest >= n):
        m_smallest = n


print("Maximum is", m_largest)

print("Minimum is", m_smallest)
