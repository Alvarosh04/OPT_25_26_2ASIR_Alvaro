estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]

resultado_final = {}

for e, nm, nf, nq  in zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica):
    promedio = ((nm + nf + nq) / 3)

    if promedio >= 6.5:
        estado = "Aprobado"

    elif promedio >= 5:
        estado = "suficiente"
    else:
        estado = "suspenso"

    resultado_final[e] = {
        "Matematicas": nm,
        "Física": nf,
        "Química": nq,
        "Promedio": promedio,
        "Estado": estado
    }

for nombre, datos in resultado_final.items():
    print(f"{nombre} - Matemáticas: {datos['Matematicas']}, Física: {datos['Física']}, Química: {datos['Química']},Promedio: {datos['Promedio']},Estado: {datos['Estado']}")
