# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:55:46 2021

@author: FranJa
"""

# Use words.txt as the file name
m_fileName = input("Enter file name: ")
m_fileHandler = open(m_fileName)

for line in m_fileHandler:
    lineInUpper = line.upper()
    print(lineInUpper.rstrip())