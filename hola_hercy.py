"""
Escribir script que pregunte el nombre del usuario en la consola y el numero entero e imprima
por pantalla en lineas distintas el nombre del usuario tantas veces como el numero
    
"""

name = input("¿Como te llamas?")
n = input("Introduce un  numero entero:")
print ((name + "\n") * int(n))