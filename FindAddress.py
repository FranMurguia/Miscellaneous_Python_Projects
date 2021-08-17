# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:08:13 2021

@author: FranJa
"""

m_fileName = input("Enter file name: ")
if len(m_fileName) < 1:
    m_fileName = "mbox-short.txt"
m_fileHandler = open(m_fileName)
m_count = 0
m_listOfAddress = list()

for line in m_fileHandler:
    # Not include lines that start with 'From:'
    if(line.startswith("From:")):
        continue
    # Find lines that star with 'From'
    if(line.startswith("From")):
        listOfWords = line.split()
        # Add to a list the [1] element (address)
        m_listOfAddress.append(listOfWords[1])
        m_count = m_count + 1

for address in m_listOfAddress:
    print(address)


print("There were", m_count, "lines in the file with \'From\' as the first word")
