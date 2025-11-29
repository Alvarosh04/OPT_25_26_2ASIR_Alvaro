#Lista de 20 números

num_origi = list(range(1, 21))

print(f"Lista original: {num_origi}")

#Una lista con los cuadrados de todos los números.

cuadrados = [numero ** 2 for numero in num_origi]
print(f"Los cuadrados de los numeros son: {cuadrados}")

#Una lista con solo los números pares.

pares = [numero for numero in num_origi if numero % 2 ==0]
print(f"Los numeros pares son: {pares}")

#Una lista con los números mayores que 10.

mayor_diez = [n for n in num_origi if n > 10]
print(f"Los numeros mayores de 10 son: {mayor_diez}")

#Cree un diccionario que relacione cada número con su doble.

doble = {n: n * 2 for n in num_origi}
print(f"Diccionario Doble): {doble}")
