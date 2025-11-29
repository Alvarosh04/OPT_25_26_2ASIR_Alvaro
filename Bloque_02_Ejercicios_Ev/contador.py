contador = 0  # variable global


def incrementar():
    global contador
    contador += 1


def decrementar():
    global contador
    contador -= 1

def mostrar_contador():
    print(f"El valor del contador es:{contador}")


print("Llamamos a incrementar dos veces")
incrementar()
incrementar()
print(f"El valor es: {contador}")

print("Llamamos a decrementar una vez")
decrementar()

mostrar_contador()