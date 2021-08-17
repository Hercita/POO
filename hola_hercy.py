# -*- coding: utf-8 -*-
"""
Escribir SCRIPT que pregunte el nombre del usuario en la consola y un numero entero e imprima
por pantalla en lineas distintas el nombre del usuario tantas veces como el numero
    
"""

name = input("¿Como te llamas? ")  # input campo de entrada de datos, en python no se pone el punto y coma
n = input("Introduce un  numero entero: ") # input campo de entrda de datos
print ((name + "\n") * int(n))   #  /n es un salto de linea, * multiplicacion, con int decimos que n es entero
  