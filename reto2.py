#Reto 2
#conventidor de monedas Col. Chil. Arg. Mx. a USD.

#CLP
clp = 1
#COP
cop = 2 
#ARS
ars = 3
#MXN
mxn = 4
#Salida
salida = 0

print("Ingrese la moneda que quiere convertir a dolares (USD): ")
print("[1] Moneda Chilena a Dolar")
print("[2] Moneda Colombiana a Dolar")
print("[3] Moneda Argentina a Dolar")
print("[4] Moneda Mexicana a Dolar")
print("[0] Salida")

convercion = 9

print("   \ | /   \ | /   \ | /   \ | /   \ | /   \ | /   \ | /   \ | /   \ | /   \ | /   \ | /   ")
print(" -   o   -   o   -   o   -   o   -   o   -   o   -   o   -   o   -   o   -   o   -   o   - ")
print("   / | \   / | \   / | \   / | \   / | \   / | \   / | \   / | \   / | \   / | \   / | \   ")

while convercion != 0:

     convercion = int(input("Selecciona: "))

     if convercion is clp:
          cifra = float(input("Ingrese la cantidad de pesos Chilenos que quieres convertir: "))
          print("Los ", cifra, "pesos Chilenos equivalen a:", float(round(cifra / 721)), "dolares" )

     elif convercion is cop:
          cifra = float(input("Ingrese la cantidad de pesos Colombianos que quiere convertir: "))               
          print("Los ", cifra, "pesos Colombianos equievalen a: ", float(round(cifra / 3730.40)), "dolares")

     elif convercion is ars:
          cifra = float(input("Ingrese la cantidad de pesos Argentinos que quieres convertir: "))
          print("Los ", cifra, "pesos Argentinos equivalen a: ", float(round(cifra / 94.20)), "dolares" )

     elif convercion is mxn:
          cifra = float(input("Ingrese la cantidad de pesos Mexicanos que quiere convertir: "))
          print("Los", cifra, "pesos Mexicanos equivalen a: ", float(round( cifra / 19.95)), "dolares")

     elif convercion is salida:
          cifra = print("Gracias por usar el conversor de monedas")
          print("   \ o /   \ o /   \ o /   \ o /   \ o /   \ o /   \ o /   \ o /   \ o /   \ o /   \ o /   ")
          break
