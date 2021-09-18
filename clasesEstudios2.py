'''
#continuacion de funciones
#Funcion DEF
def menu(*platos):
    #El asterisco sirve como multi parametro
    print('Hoy tenemos: ', end= '')
    for plato in platos:
        print(plato, end=', ')
    return

menu('pasta', 'pizza', 'ensalada')
#Se puede invocar mas listas
menu('frijoles', 'chicharro', 'huevos')


#Hay funciones locales y globales
#Las locales son las que estan dentro de DEF
#Las globales estan fuera de la funcion

def bienvenida(nombre):
    lenguaje = 'Python'
    print('Bienvenido a ', lenguaje, nombre + '!')

bienvenida('Sebastian')
#Mostrara error por que esta fuera de
#la funcion y no existe fuera de la funcion

# print (lenguaje)


#añadir variables
primer_curso = ['Matematicas', 'Fisica']

def añade_asignatura(curso, asignatura):
    curso.append(asignatura)
    

añade_asignatura(primer_curso, 'Quimica')
print(primer_curso)


#definir el proposito de la funcion
#sirve para especificar funciones de creacion propia
#OJO VA EN EL RETO 4

def area_triangulo(base, altura):
    """Funcion que calcula el area de un triangulo.
    Parametros:
        -base: Un numero real con la base del triangulo
        -altura: Un numero real con la altura del triangulo
    Salida:
        Un numero real con el area del triangulo de base y altura especifico.
    """
    return base * altura / 2

help(area_triangulo)

#Funciones recursivas, contiene una llamada a si mismo

def factorial(n):
    if n == 0 :
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
#OJO ESTAS FUNCIONES RECURSIVAS SON MUY PESADAS PARA PROCESAR!!!

#metodos ordenativos iterativos

#organizar las listas sin usar metodos nativos de python
#Ordenar 
sueldos = []

#Se debe crear una lista donde almacenar 5 sueldos
#el valor mas alto en el ultimo lugar
for x in range(5):
    valor=int(input("Ingrese el valor del sueldo: "))
    sueldos.append(valor)

print("Lista sin ordenar")
print(sueldos)

for x in range(4):
    if sueldos[x] > sueldos [x+1]:
        temporal = sueldos[x]
        sueldos[x] = sueldos[x+1]
        sueldos[x+1] = temporal
print("final")
print(sueldos)

sueldos = []
for x in range(5):
    valor=int(input("Ingrese sueldos : "))
    sueldos.append(valor)
print("lista 1")
print(sueldos)

for y in range(4):
    for x in range(0, 4):
        if sueldos[y] < sueldos[x]:
            temporal = sueldos[x, y]
            

print(sueldos)  
      
#Ordenar paises

PaisesLA =[]
for x in range (5):
    pais = str(input("ingrese paises Latinos :"))
    PaisesLA.append(pais)
print("Paises Latam")
print(PaisesLA)

PaisesLA.sort()
print(PaisesLA)
#Arreglar codigo para que funcionen

lista=[]
for i in range(0,5):
    salario=int(input('Ingrese los elementos : '))
    lista.append(salario)
print('Lista de elementos enteros ')
print(lista)
for x in range (len(lista)-1):
    for y in range (len(lista)-1):
        if lista[y]>lista[y+1]:
            temporal= lista[y]
            lista[y] = lista [y+1]
            lista[y+1] = temporal 
                
print ('Lista de elementos ordenado de menor a mayor: ')
print(lista)
for x in range (len(lista)-1):
    for y in range (len(lista)-1):
        if lista[y]<lista[y+1]:
            temporal= lista[y]
            lista[y] = lista [y+1]
            lista[y+1] = temporal 
print ('Lista de elementos ordenado de mayor a mayor: ')
print(lista)


#Busqueda binaria como se hace la busqueda
def busquedaBinaria(lista, valorBuscar):
    primero = 0
    ultimo = len(lista)-1
    encontrado = False

    while primero<=ultimo and not encontrado:
        puntoMedio = (primero + ultimo) // 2
        if lista[puntoMedio] == valorBuscar:
            encontrado = True
        else:
            if valorBuscar < lista[puntoMedio]:
                ultimo = puntoMedio-1
            else:
                primero = puntoMedio+1

    return encontrado

listaBusqueda = [3, 5, 6, 11, 12, 14, 15, 17, 18]
print(busquedaBinaria(listaBusqueda, 8))

#ejemplo de DEF MAIN() - RETO 4

def main (): 
    op = pintarMenu()
    while op != str.upper("s"):
        if op == "A":
            solicitarDatos()
        elif op ==    

#MODULOS
#Biblioteca Random

import random

dado1=random.randint(1,21)
dado2=random.randint(1,21)
print("Primer dado: ",dado1)
print("Segundo dado: ",dado2)
suma=dado1+dado2
if suma ==18:
    print("Gano")
else:
    print("Perdio")
    
#Ejercicio

#Hacer que cargue 10 enteros
# en rango de 0 - 1000

import random

def cargar():
    lista=[]
    for x in range(10):
        lista.append(random.randint(0,1000))
    return lista

def imprimir(lista):
    print(lista)

def mezclar(lista):
    random.shuffle(lista)

def ordenarLista(lista):
    for x in range (len(lista)-1):
        for y in range (len(lista)-1):
            if lista[y]>lista[y+1]:
                temporal= lista[y]
                lista[y] = lista [y+1]
                lista[y+1] = temporal
    print(lista)

#bloque principal
lista=cargar()
print("Lista generada aleatoriamente")
imprimir(lista)
mezclar(lista)
print("La misma lista luego de mezclar")
imprimir(lista)

#Ejercicio 2

print('Adivina el número!')
import random
numero = random.randint(1,20)
cont = 0
for x in range (0,3):
    variable = int(input('¿Cual cree que es el número?: '))
    if variable == numero:
        print('¡Ganaste!')
        break

    elif variable > numero:
        print('Ingrese un valor menor')
    elif variable < numero:
        print('Ingrese un valor mayor')

    cont += 1
    if cont == 2:
        print('\nUltima oportunidad\n')
    if cont == 3:
        print('\nPerdiste :(')

#Ejemplo 3
import random
m = 20
cont = 1
num = random.randint (1,20)
for cont in range (3) :
    
    x = int(input("Ingrese un número entre 1 y 20: "))
    print ("*"*m*3)
    if x < num :
        print (f'{x} es menor al número, intente de nuevo')
        print ("*"*m*3 + "\n")
    elif x > num :
        print (f'{x} es mayor al número, intente de nuevo')
        print ("*"*m*3 + "\n")
    elif x == num :
        print ("*"*m + " GANASTE " + "*"*m)
        break
    cont += 1
    if cont == 3:
        print ("*"*m + " PERDISTE " + "*"*m)
        print (f'El número ganador era: {num}')
        break

#Ejemplo 4
import random
numero=random.randint(1,20)
for x in range (1,3+1):
    n=int(input("Ingrese un numero entero, intento " + str(x)+ ": "))
    if numero==n:
        print("Ganaste! \ 0.0 /")
        break
    elif numero>n:
            print("Intente de nuevo, digite un numero mayor ")
            print("*****************************************")
    elif numero<n:
            print("Intente de nuevo, digite un numero menor ")
            print("*****************************************")          
print("Perdiste!  (=.=) ")
print("*****************************************")
print("el numero generado fue:"+ str(numero))


#Funcion Import
#Para evitar el uso de random antes de la funcion


#ejercicio simple

from math import sqrt as raiz, pow as elevar

valor = int(input("Ingrese un valor: "))
r1 = raiz(valor)
r2 = elevar(valor, 3)
print("La raiz cuadrada es: ",r1)
print("El cubo es: ", r2)


from random import randint, shuffle
numerosGenerados = randint(1,20)
masNumeros = shuffle(1,20)
print(numerosGenerados)
print(masNumeros)


#sqrt => raiz.  (de la libreria Math)
#pow => potencia. (de la libreria Math)

import random 
from math import sqrt, pow
numero =random.randint(1,20)

raiz = sqrt(numero)
potencia = pow(numero,2)
       
print("La raiz del numero {} es: {}".format(numero, raiz))
print("La potencia del numero {} es: {}".format(numero, potencia))

#Ejercicio
#Hay que aprender a usar definiciones

from math import sqrt, pow
from random import randint

def PotenciaDeNumero(x, y):
    return pow(x, y)

def RaizDeNumero(x):
    return sqrt(x)

def imprimir(n, r, p, x):
    print("La raiz del numero {} es: {}".format(n, r))
    print("La potencia del numero {} elevado a la {} es: {}".format(n, x, p))
    print("-", 50)

def principal():
    for x in range(2, 5):
        valorRecibido = randint(1, 20)
        raiz = RaizDeNumero(valorRecibido)
        potencia = PotenciaDeNumero(valorRecibido)
        imprimir(valorRecibido, raiz, potencia, x)

if __name__ == "__main__":
    principal()


#Definir ALIAS a la funcion
'''

from math import sqrt as raiz, pow as elevar
from random import randint
from os import system
from time import sleep

def PotenciaDeNumero(x, y):
    return elevar(x, y)

def RaizDeNumero(x):
    return raiz(x)

def imprimir(n, r, p, x):
    sleep(3)
    print("La raiz del numero {} es: {}".format(n, r))
    sleep(3)
    print("La potencia del numero {} elevado a la {} es: {}".format(n, x, p))
    sleep(3)
    print("-", 50)

def principal():
    for x in range(2, 5):
        valorRecibido = randint(1, 20)
        raizde = RaizDeNumero(valorRecibido)
        potencia = PotenciaDeNumero(valorRecibido, x)
        imprimir(valorRecibido, raizde, potencia, x)

if __name__ == "__main__":
    principal()


#Modulo OS.SYSTEM("CLS")
#Al ejercicio anterior usar el time.sleep(3)
#Y el os.system("cls")
#HAY QUE HACERLO SI O SI NO HAY QUE SER VAGO

