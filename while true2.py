# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:47:24 2019

@author: BLUEIT-PARTICIPANTE
"""

while True:
    x=input("ingrese un valor hasta el cual contar ")
    if x== "q" or x=="quit":
        break
    x=int(x)
    y=1
    while True:
        print (y)
        y=y+1
        if y>x:
            break
    