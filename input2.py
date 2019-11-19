# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:53:32 2019

@author: BLUEIT-PARTICIPANTE
"""

firstname = input("what is your first name?")
lastname = input("what is your last name?")
location = input("what is your location?")
age = input("what is your age?")
space = " "
print("El señor",firstname,lastname,
      "tiene que hacer mucho deporte en",location,
      "porque ya tiene",age,"años")

print("El señor"+space+firstname+space+lastname+space+
      "tiene que hacer mucho deporte en"+space+location+space+
      "porque ya tiene"+space+age+space+"años")