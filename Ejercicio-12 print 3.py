# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:54:39 2019

@author: BLUEIT-PARTICIPANTE
"""
#variables
x=3

#codigo

# print("the value of x is" + x)  #TypeError: can only concatenate str (not "int") to str

print(end='\n')
print ("""EJERCICIO 1: print (x,y) COLOCA UN ESPACIO DESPUES DE CADA VARIABLE""")
print("the value of x is",x)

print(end='\n')
print ("""EJERCICIO 2: PRINT STRING CON str(x)""")
print("the value of x is"+str(x)) 

print(end='\n')
print ("""EJERCICIO 2: PRINT STRING CON x=str(x)""")
x=str(x)
print("the value of x is"+x)
