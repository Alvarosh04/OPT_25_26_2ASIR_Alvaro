estudiantes = {
    "Ana": [8, 7, 9],
    "Luis": [7, 6, 8],
    "Marta": [9, 10, 9],
    "Carlos": [6, 7, 5],
    "Laura": [10, 9, 10]
}

# El bucle for itera sobre cada par clave, valor (nombre, notas)

for nombre, notas in estudiantes.items():

    promedio = sum(notas) / len(notas)

    if promedio >= 6.5:
        estado = "Aprobado"
    elif promedio >= 5:
        estado = "Suficiente"
    else:
        estado = "Suspenso"

    print(
        f"{nombre} - Notas: {notas}, Promedio: {promedio:.2f}, Estado: {estado}")

