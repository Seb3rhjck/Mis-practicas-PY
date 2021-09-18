#Programacion Funcional
#Va para funciones puras, funciones que no tienen 
#efectos secundarios.
#Se usa el lenguaje Haskell
#Porque el funcional: Facil de probar y depurar
#big data, computacion concurrente y paralela
#Modulos en python:
#-INTERTOOL  -OPERATOR -FUNCTOOLS -FN -CYTOOLZ -MACROPY
'''
#Operadores sobre lista 
#MAP

#se crea la lista
items = list(range((1, 11)))
print(items)

#se hace de forma imperactiva
cuadrados = []
for i in items:
    cuadrados.append(1**2)
print(cuadrados)

#Ahora cuadrados usa MAP
#funcional
cuadrados = map(lambda x: x **2, items)
print(list(cuadrados))

#Esto ayuda a simplificar
#Lambda es una funcion anonima

#Ejemplo2
#se puede usar con mas funciones como pow(potencia)

from math import pow as potencia

print(potencia(2, 3))

numeros =[2, 3, 4]
potencias = [3, 2, 4]

potenciados = map(potencia, numeros, potencias)
print(list(potenciados))
#cuando se usa map en el print siempre debe tener un argumento antes de la variable

#EJERCICIO

from math import sqrt as raiz, pow as potencia
from random import randint

def PotenciaDeNumero(x, y):
    return pow(x, y)

def RaizDeNumero(x):
    return raiz(x)

def imprimir(n, r, p, x):
    print("La raiz del numero {} es: {}".format(n, r))
    print("La potencia del numero {} elevado a la {} es: {}".format(n, x, p))
    print("-", 50)

def principal():
    for x in range(2, 5):
        valorRecibido = randint(1, 20)
        raiz = RaizDeNumero(valorRecibido)
        potencia = PotenciaDeNumero(valorRecibido, x)
        imprimir(valorRecibido, raiz, potencia, x)

def imprimirMap(n, r, p, x):
    print("la raiz del numero {} es: {}".format(n, r))
    print("La potencia del numero {} elevado a la {} es: {}".forma(n, x, p))
    print("-"*50)

def principal():
    listaPotencias = list(range(2, 5))
    listaValores  = list(map(lambda x: randint(1,20), listaPotencias))
    valPotencias = list(map(pow, listaValores, listaPotencias))
    valRaices = list(map(raiz, listaValores))
    imprimirMap(listaValores, valRaices, valPotencias, listaPotencias)

if __name__ == "__main__":
    principal()

#Tarea hacer CIclo de las lista con el anterior codigo es decir
#En imprimirMap sacar las lista por separado e individual
#HACERLO NADA DE VAGANCIA OJO ESTO AYUDA Y MUCHO DO IT FOR HER
'''
