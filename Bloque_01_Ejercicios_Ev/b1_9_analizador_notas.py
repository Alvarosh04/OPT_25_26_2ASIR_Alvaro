# Bloque_01_Ejercicios_Ev/b1_9_analizador_notas.py

"""
Este programa pide al usuario tres notas y calcula el promedio.
Error original: solo sumaba dos notas en vez de tres, por lo que el promedio era incorrecto.
Corrección: se suman correctamente las tres notas antes de dividir entre 3.
"""

# Pedir tres notas al usuario
nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
nota3 = float(input("Introduce la tercera nota: "))

# Error lógico: solo suma dos notas
promedio = (nota1 + nota2) / 3

print("El promedio (con error lógico) es:", promedio)