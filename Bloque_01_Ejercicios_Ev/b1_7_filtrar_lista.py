lista = ["Ana", "Pedro", "Alba", "Marta", "Alvaro", "Carlos"]

for nombre in lista:
    if nombre.lower().startswith("a"):
        continue
    print(nombre)