# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:06:08 2019

@author: BLUEIT-PARTICIPANTE
"""
devices =  ["R1" , "R2" , "R3" , "S1" , "S2"]

for item in devices:
        print(item)
"""
imprime la lista devices
"""        
for item in devices:
    if "R" in item:
        print(item)
"""
llena las listas de switches y router
"""
switches=[]
router=[]
for item in devices:
    i=0

    if "S" in item:
        switches.append(item) 
        print(switches)
        print(i)
        i=i+1
    else:
        router.append(item) 
        print(router)
        print(i)
        i=i+1
print(switches)
print(router)        