# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 14:31:30 2021

@author: FranJa
"""


def FindInList(listIn, initial, mayus = True):
    listOut = []
    for element in listIn:
        if element[0] == initial:
            if mayus:
                listOut.append(element.upper())
            else:
                listOut.append(element.lower())
    return (listOut, len(listOut))

m_list1 = ["uno", "dos", "tres", "cuatro", "cinco"]

print(FindInList(m_list1, "c"))
print(FindInList(m_list1, "a", True))
print(FindInList(m_list1, "d", False))
print(FindInList(initial = "c", mayus = False, listIn = m_list1))

elements, num_elements = FindInList(listIn = m_list1, initial = "c")

print(elements,num_elements)

# Ficheros de texto plano

# w = Write, r = read, a = append
m_fichero = open("prueba.txt", "w")
m_fichero.write("Esto\n")
m_fichero.write("es\n")
m_fichero.write("un\n")
m_fichero.write("archivo\n")
m_fichero.write("de\n")
m_fichero.write("prueba\n")
m_fichero.close()


m_fichero_lectura = open("prueba.txt", "r")
m_contenido = m_fichero_lectura.read()
m_fichero_lectura.close()

print(m_contenido)


m_fichero_lectura = open("prueba.txt", "r")
for linea in m_fichero_lectura:
    print (linea)
m_fichero_lectura.close()

