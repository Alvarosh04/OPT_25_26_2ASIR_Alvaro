a  = input("Escribe el primer numero para calcular")
b = input("Escribe el segundo numero para calcular")

def sumar (a,b):
    return a+b

def restar (a,b):
    return a - b

def multiplicar (a,b):
    return a * b

def dividir (a,b):
    return a / b

num1 = float(a)
num2 = float(b)
print("La suma es:", sumar(num1,num2))
print("La resta es:", restar(num1,num2))
print("La multiplicación es:", multiplicar(num1,num2))
print("La división es", dividir(num1,num2))