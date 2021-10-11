# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:57:23 2021

@author: FranJa
"""

# Use the file name mbox-short.txt as the file name
m_fileName = input("Enter file name: ")
m_fileHandler = open(m_fileName)

m_totalValue = 0
m_count = 0

for line in m_fileHandler:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    m_count = m_count + 1
    lineList = line.split()
    pointValue = float(lineList[1])
    m_totalValue = m_totalValue + pointValue
    
m_average = m_totalValue/m_count
print("Average spam confidence:", m_average)
