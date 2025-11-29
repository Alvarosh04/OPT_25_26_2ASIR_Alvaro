estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]

notas_juntas = list(zip(notas_matematicas, notas_fisica, notas_quimica))

for indice, (nom, notas)  in enumerate(zip(estudiantes, notas_juntas), start=1):

    nm, nf, nq = notas

    promedio = ((nm + nf + nq) / 3)

    if promedio >= 6.5:
        estado = "Aprobado"

    elif promedio >= 5:
        estado = "suficiente"
    else:
        estado = "suspenso"

    print(
        f"{indice} {nom} - Matemáticas: {nm}, Física: {nf}, Química: {nq}, Promedio: {promedio:.2f}, Estado: {estado}")
