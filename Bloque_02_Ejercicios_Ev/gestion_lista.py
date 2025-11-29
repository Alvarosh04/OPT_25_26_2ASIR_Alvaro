compras = []

pro1 = input("Dime un producto")
compras.append(pro1)
pro2 = input("Dime un producto")
compras.append(pro2)
pro3 = input("Dime un producto")
compras.append(pro3)
pro4 = input("Dime un producto")
compras.append(pro4)
pro5 = input("Dime un producto")
compras.append(pro5)

print(f"la lista es: {compras}")

elim_1 = input("Elimine un producto de la lista:")
compras.remove(elim_1)
compras.sort()
print(f"la lista es: {compras}")