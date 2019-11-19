# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:11:50 2019

@author: BLUEIT-PARTICIPANTE
"""
#definicion de funcion
 
def subtra(a,b):
    print(a - b)

#inicio codigo
    
print ("este codigo resta las variables a - b")
a1=int(input("ingrese el valor de a:  "))
b1=int(input("ingrese el valor de b:  "))
subtra(a1,b1)
subtra(2,b=2) #correcto
# subtra(a=2,b1) error positional