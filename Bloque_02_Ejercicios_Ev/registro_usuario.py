# Todos los argumentos posicionales.

def crear_usuario(nombre, edad, ciudad="Madrid"):
    print(f"Usuario: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

crear_usuario("Alvaro",21, "Huelva")

# Algún argumento omitido, usando el valor por defecto.

def crear_usuario(nombre, edad, ciudad="Madrid"):
    print(f"Usuario: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

crear_usuario("Alvaro",21)

# Argumentos nombrados en distinto orden.

def crear_usuario(nombre, edad, ciudad="Madrid"):
    print(f"Usuario: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

crear_usuario( edad=21,ciudad="Madrid", nombre="Alvaro")