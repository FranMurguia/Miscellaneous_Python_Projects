# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:06:16 2021

@author: FranJa
"""

m_fileName = input("Enter file name: ")
m_fileHandler = open(m_fileName)

m_list = list()
for line in m_fileHandler:
    listOfWords = line.split()
    
    for word in listOfWords:
        if(word in m_list):
            continue
        m_list.append(word)

m_list.sort()
print(m_list)
    
