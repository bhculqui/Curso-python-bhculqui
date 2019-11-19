# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:53:32 2019

@author: BLUEIT-PARTICIPANTE
"""

firstname = "Borys"
lastname = "Culqui"
location = "Quito"
space = " "

print ("Has llamado a SEGUROS LARGAVIDA")
age = input("what is your age?")
age = int(age)


print("El señor"+space+firstname+space+lastname+space+
      "require un plan de retiro en"+space+location+space+
      "porque ya tiene"+space,age,space+"años")

if int(age)<=18:
    print("gracias por responder nuestra encuesta, eres menor de edad para continuar")
elif int(age)<=30:
    print("eres joven para nuestros planes de retiro")
elif int(age)<=45:
    print("puedes tomar nuestro planes de retiro bronce")
elif int(age)<=60:
    print("puedes tomar nuestro planes de retiro plata")
elif int(age)<=75:
    print("puedes tomar nuestro planes de retiro oro")
else:
    print("bip bip bip")
    
   
