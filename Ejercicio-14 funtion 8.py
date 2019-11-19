# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:12:08 2019

@author: BLUEIT-PARTICIPANTE
"""
#ejemplo 1

def wishes():
    print("my wishes")
    return "happy birthday"

# inicio codigo
    
wishes () #ejecuta la funcion e imprime en este caso


#ejemplo 2

# diferencia con return, devuelve el valor de return en la funcion que llama a wishes

def wishes():
    print("my wishes")
    return "happy birthday"

# inicio codigo
    
print(wishes ())