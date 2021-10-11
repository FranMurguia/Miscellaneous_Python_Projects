# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:22:44 2021

@author: FranJa
"""

m_fileName = input("Enter file:")
if len(m_fileName) < 1:
    m_fileName = "mbox-short.txt"
    
m_fileHandler = open(m_fileName)

m_counts = {}

for line in m_fileHandler:
    
    # Not include lines that start with 'From:'
    if (line.startswith("From:")):
        continue
    
    # Find the lines that start with "From" and create a list of his words
    if (line.startswith("From")):
        listOfWords = line.split()
        
        # Split again using a colon
        tempList = listOfWords[5].split(":")
        
        # Get the [0] element of tempList (Hour)
        m_counts[tempList[0]] = m_counts.get(tempList[0], 0) + 1

# Sort the diccionary elements using a List
m_listOfTime = list()
for key,value in m_counts.items():
    tempTuple = (key, value)
    m_listOfTime.append(tempTuple)

#Mostrar en pantalla las tuplas de la lista
print("Hour","Mails sent")
m_listOfTime = sorted(m_listOfTime)
for key,value in m_listOfTime:
    print(key,value)
        
