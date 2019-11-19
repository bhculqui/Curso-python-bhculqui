# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:01:09 2019

@author: Tecnologia
"""

first_name = input("First Name: ")
last_name = input("Last Name: ")
location = input("Location: ")
age = int(input("Age: "))

spacio = " "

if age <= 10:
    mensaje = "Eres un ninio"
elif age > 10 and age <= 30:
    mensaje = "Eres joven"
elif age > 30 and age <= 40:
    mensaje = "te estas poniendo viejo"
else:
     mensaje = "estas viejo"
  


print("Hola " + first_name + spacio + last_name + spacio + 
      "tu vives en" + spacio + location + " y tienes" + spacio + str(age) +
      spacio + "anios" + "\n" + "por lo tanto:" + mensaje + "Bienvenido!")