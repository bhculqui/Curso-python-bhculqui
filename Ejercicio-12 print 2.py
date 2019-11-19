# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:54:39 2019

@author: BLUEIT-PARTICIPANTE
"""
stri1="Cisco"
stri2="Netoworking"
stri3="Academy"
space=" "

print(end='\n')
print ("""EJERCICIO 1:  STRING SIN ESPACIO""")
print(stri1+stri2+stri3)      #+concatena

print(end='\n')
print ("""EJERCICIO 2: PRINT STRING CON ESPACIO""")
print(stri1+space+stri2+space+stri3)

print(end='\n')
print ("""EJERCICIO 2: PRINT (x,y,z)""")
print(stri1,stri2,stri3)#coma separa el texto de las variable

x=3
# print("the value of x is" + x)  #TypeError: can only concatenate str (not "int") to str

x=3
print("the value of x is",x) #TypeError: can only concatenate str (not "int") to str

x=3
print("the value of x is"+str(x)) #x=3
print("the value of x is"+str(x)) #error


x=3
x=str(x)
print("the value of x is"+str(x))

