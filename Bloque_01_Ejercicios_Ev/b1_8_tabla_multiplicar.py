num1 = input("Introduzca un numero:")
num1= int(num1)
num2 = input("Introduzca un numero:")
num2 = int(num2)
operacion = input("elige operacion (suma, resta, multiplicacion, division):")
operacion = str(operacion)
if operacion == "suma":
    print(f"Resultado: {num1 + num2}")
elif operacion == "resta":
    print(f"Resultado: {num1 - num2}")
elif operacion == "multiplicacion":
    print(f"Resultado: {num1 * num2}")
elif operacion == "division":
    print(f"Resultado: {num1 / num2}")
else:
    print("Operacion no reconocida")