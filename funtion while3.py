# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:48:00 2019

@author: BLUEIT-PARTICIPANTE
"""
"""
CUENTA INFINITAS VECES HASTA ROMPER CON x=q
"""

while True:
    x=input("enter a numbre to count to  :")
    if x == 'q' or x == 'quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
        
    