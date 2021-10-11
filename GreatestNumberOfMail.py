# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:11:54 2021

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
        
        # If the word is in m_counts, add 1, else add it to m_counts
        m_counts[listOfWords[1]] = m_counts.get(listOfWords[1], 0) + 1
        

m_biggerValue = None
m_biggerKey = None

# Move throughout the tuples
for key,value in m_counts.items():
    
    # Get the key,value if is the first element
    # or if the new value is bigger than the actual
    if(m_biggerKey is None or m_biggerValue < value):
        m_biggerKey = key
        m_biggerValue = value

print(m_biggerKey, m_biggerValue)