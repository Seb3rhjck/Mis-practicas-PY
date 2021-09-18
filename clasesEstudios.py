'''
nombre = "Sebastian"
print(len(nombre))

#Numeros

#suma
print(3+2)

#resta
print(3-2)

#multiplicacion
print(3*2)

#division
print(4/2)

#modulo
print(3%2)

#potencia
print(3**2)

#variables
numero1 = 8
numero2 = 9.35

print((numero1 + numero2) * 18)

numero1 = 10
numero2 = 50
resultado = 0

resultado = numero1 * 200
print(resultado)

#boleanos

existenEstudiantes = True
print(existenEstudiantes)
existenEstudiantes = False
print(existenEstudiantes)

nombre = input("Digite nombre: ")
edad = int(input("Digite edad: "))
telefono = int(input("Digite telefono: "))
documento = int(input("Digite documento: "))
direccion = input("Digite direccion: ")
email = input("Digite email: ")
promedio =  float(input("Digite promedio anterior: "))
print(edad + 5)

#condicionales
puntaje1 = 8
puntaje2 = 3
puntaje3 = 7

promedio = ((puntaje1 + puntaje2 + puntaje3) / 3)

if promedio >= 7 :
    print("Tu puntaje es muy bueno")
elif promedio >= 4:
    print("Veo que necesitas mejorar tu puntaje")
else:
    print("Estamos graves")

contador2 = 0 

while contador2 <= 5:
    contador2 +=1
    if(contador2 ==4):
        print("Esto es todo amigous: ", contador2)
        break
        print("todo esta en: ", contador2)
    else :
        print("Esto se acaba: ", contador

lista = [1,2,3]

print (lista)



if len(lista) > 0:

    lista.pop()

    print (lista)

if len(lista) > 0:

    lista.pop()

    print (lista)

if len(lista) > 0:

    lista.pop()

    print (lista)

if len(lista) > 0:

    lista.pop()

    print (lista)

else:

    print("No existen más elementos para eliminar")
'''

#Manejo de excepciones.
#Con ciclo hasta vlor numerico
while (True):
    try:
        n1 = float(input("ingresa numero: "))
        n2 = 4
        print("{}/{}={}".format(n1,n2, n1/n2))

    except:
        print("Hay error")
    else:
        print("Todo bien con el codigo")
        break;
    finally:
        print("Esta joda se acabo.")
'''

#Tipo de error
try:
    n1 = float(input("Meta el numero: "))
    n2 = 0
    print("{}/{}={}".format(n1,n2, n1/n2))
except Exception as e:
    print(type(e)._name_)  
#con el type e se busca el error de manera mas profundo

#Listas
#Crear una lista
lista = [1,2,3,4,5]
print(lista)
#agregando elementos
lista.append(9)
#append nos permite agregar
#Se agrega otro valor
print(lista)

#Lista interactiva
lista = [1,2,3,4,5]
contador = 1
while True:
    lista.append(contador)
    contador+=1
    if contador == 10:
        break
print(lista)    

while contador <10:
    lista.append(contador)
    contador+=1
print(contador)

#acceder a elementos de la lista
lista = [1,2,3,4,5]
print(lista[1])

#los datos se deben manejar con lots ''

#extender la lista 'Union'
lista1 = [1,2,3]
lista2 = [4,5,6]
lista1.extend(lista2)
lista3 = [7,8,9]
print(lista1)
lista1.extend(lista3)
#se puede hacer con diferentes variables para la lista

#pop() es una excepcion
#quitar un elemento a la lista

lista =[1,2,3,4,5,6]
print(lista)
lista.pop()
#pop() si un dato dentro de los parentesis significa que va por el ultimo
print(lista)
lista.pop(2)
print(lista)


#Agregar otros elementos a la lista
lista = ['a','b','c','a','d','c','b','a',' ']
#el espacio es un caracter
#uscar lacantidad de ocurrencias que hay de un valor
print(str(lista.count('a')))

#Contar la lista de elementos de una lista
lista = ['a', 'b', 'c', 'd', 'e']
print(len(lista))

#devuelve el indice del primer elemento encontrado
lista = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']
print(len(lista))
print(lista.index('c'))
#ahora con un punto de inicio
print(lista.index('c', -2))

#remover los elementos de la lista
lista = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']
lista.clear()
print(lista)

#copiar los elementos de una lista

lista1 = [1,2,3,4,5]
lista2 = []
lista2 = lista1.copy()
print("lista1= " + str(lista1))
print("lista2= " + str(lista2))


#ordenar lista de manera ascendente
listaDesordenada = [9,4,2,6,5,8,1,3,7]
listaDesordenada.sort(reverse=True)
print(listaDesordenada)

#Remover
listaDesordenada = [9,4,2,6,5,8,1,3,7]
listaDesordenada.remove(3)
print(listaDesordenada)

#remover todos los elementos

del listaDesordenada[1:-1]
print(listaDesordenada)

#insertar un objeto
listaDesordenada = [9,4,2,6,5,8,1,3,7]
listaDesordenada.insert(0, 16)
#en el parentesis la primera parte es la ubicacion y la segunda es el objeto
print(listaDesordenada)
#se puede usar tambien el .append

#operaciones con listas
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]
#Suma
print(list1+list2)
#multiplicacion
print(list2 * 3)
#se multiplica la cantidad de veces en la que se repite la lista


#convertir una cadena de caracteres en una lista
#Se usa el comando "list" para generar todo en una lista
lista = list("Iris y Sebastian se casaran")
print(lista)

#convertir de lista a texto
#se usa el comando join, las comillas son  un remplaso de parametros en este caso nohay nada
#lo cual deja al texto sin ninguna separacion
cadena ="".join(lista)
print(cadena)

#problema ejercicio
#Ver el debug para ver bien el funcionamiento
lista = []
for i in range(0, 9):
    valor=int(input("Ingrese valor: "))
    lista.append(valor)

mayor=lista[0]
for x in range(1, 9):
    if lista[x]>mayor:
        mayor=lista[x]

print("Lista completa")
print(lista)
print("El mayor de la lista es: ")
print(mayor)


#Ejercicio2

lista = []
for i in range(0, 4):
    valor=int(input("Ingrese valor: "))
    lista.append(valor)

menor=lista[0]
for x in range(1, 4):
    if lista[x]<menor:
        mayor=lista[x]

print("Lista completa")
print(lista)
print("El mayor de la lista es: ")
print(menor)
print("La ubicacion dela lista es: "(lista.index(menor)))


#ejercicio 3

lista = [8,28,18,38,48]
print(sum(lista))

suma = 0
x=0
while x < len(lista):
    suma += lista[x]
    x += 1
print("Los elementos de la lista son: ", lista)
print(suma)
print(x)
#sum es la suma de los elementos de la lista

#ejercicio 4

lista = ["enero", "febrero", "marzo", "abril"]
print(lista + lista[0])
print(lista + lista[3])
#buscar solucion debe dejar solo el primero y el ultimo


#ejercicio 5
lista = ["Sebastian", 5, 5]
print("El nombre es: ", lista[0])
print("El promedio es: ", lista[1] + lista[2] )
#buscar como sacar promedio

#listas con listas internas

nota1 = [4, 5, 7, 3, 8]
nota2 = [9, 7, 0, 5, 6]
nota3 = [3, 7, 1, 4, 2]
notas = [nota1, nota2, nota3]

#lista completa
print(notas)

#imprimir el preimer componente
print(notas[0])

#imprimir el primer componente del primer elemento
print(notas[0][0])

#imprimir con un "for" la lista contenida en el primer componente

for x in range(len(notas[0])):
    print(notas[0][x])

#Para seleccionar mas elementos de una lista sehace asi

for x in range(1, len(notas[-1])):
    print(notas[1][x])

#imprimir cada elemento entero de cada lista contenidaen la lista doble "for"

supernotas = []
for k in range(len(notas)):
    for x in range(len(notas[k])):
        print(notas[k][x])
    supernotas.append(notas[k][x])
supernotas.sort() 
print(supernotas)   

#Operaciones em listas

lista = [[1, 2, 3, 4, 5], [5, 6, 7, 8, 9, 10, 11]]


suma1 = lista[0][0] + lista[0][1] + lista[0][2]
print(suma1)

#modo simple
suma1 = 0
for x in range(len(lista[0])):
    suma1 = suma1 + lista[0][x]

suma2 = 0
for x in range(len(lista[1])):
    suma2 = suma2 + lista[1][x]

print(suma1)
print(suma2)

#Otra forma aun mas simple
#Con doble "for"

for y in range(len(lista)):
    suma = 0
    for x in range(len(lista[y])):
        suma=suma+lista[x][y]
    print(suma)

#Lista por asignacion de diferente tamaño
#Cuando hay mas de 2 listas
lista = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]

suma =0
for y in range(len(lista)):
    for x in range(len(lista[y])):
        suma=suma+lista[y][x]
print(suma)



#Remplazar los elementos internos
lista = [[18, 45, 7, 3], [56, 23, 5, 98], [47, 32, 76, 1], [12, 58, 90, 33]]
print(lista)
for y in range(len(lista)):
    for x in range(len(lista[y])):
        if lista[x][y]>50:
            lista[x][y]=0
print(lista)
#Debe tener minimo 4 elementos para que no surja un error

#Ejercicio de practica
#imprimir lista
#

lista =[[4, 12, 5, 66], [14, 6, 25], [3, 4, 5, 67, 89, 23, 1], [78, 56]]

print(lista)

for x in range(len(lista)):
    for y in range(len(lista[x])):
        if lista[x][y] > 10:
            lista[x][y] = lista[x][y] * 4

print(lista)

for x in range(len(lista)):
    for y in range(len(lista[x])):
        if lista[x][y] < 10:
            lista[x][y] = 0

print(lista)


#ejercicio

lista = [["Armin", "Ferry"], ["Orjan"], ["Yahel", "Paul", "Tijvs"]]
print(lista)
print(lista[2][2])
print(lista[2])

#otra forma

print(lista [-1])
print(lista[-1][-1])


#TUPLAS
#son listas inmutables, es una constante, no se pueden cambiar
ciudades = ("Bogota", "Cali", "Cartagena", "Medellin")
#Usamos "len" para ver la cantidad de elememtos
#Tambien se usa "index" y "count" en este tipo de lista
#Otros elementos son el "suma", "max", "min", "sorted"

numeros = (23, 45, 12, 67, 92)
print(sum(numeros))
print(max(numeros))
print(min(numeros))
print(sorted(numeros))

#ejercicio extra

lista=[]

valor=0



n=int(input("Digite la cantidad de subindices de la lista : "))

for i in range (1,n+1):

        valor=int(input("Ingrese la cantidad de componentes de la lista: " ))

        subindice=[]

        for j in range (1,valor+1):

                dato=int(input("Ingrese el valor de la lista: "))

                subindice.append(dato)

        lista.append(subindice)

print (lista)

#Funciones y Diccionarios
#Asi se declara un diccionario
diccionario = {
    'nombre':'Iris',
    'apellido':'Barrera',
    'apartamento':'118',
}
print(diccionario)

#parentesis = tuplas (...)
#corchetes = listas [...]
#llaves = disccionario {...}

#diccionario anidados
datos = {
    'nombre completo':
    {
        'Nombre': 'Iris',
        'Apellido':'Barrera'
    },
    'direccion':{
        'parte1':'carrea 24',
        'parte2':'50 - 63'
    }
}
print(datos)

#buscar para aplicar en el reto 3

#Acceso a elementos del diccionario
diccionario = {
    'Nombre':'Sebastian',
    'Apartamento': '118',
    'Genero Musical':'Trance'
}
#Se obtiene el valor con una llave especifica, si no existe hay error
print(diccionario['Nombre'])
print(diccionario['Genero Musical'])

diccionario = {
    'Nombre':'Sebastian',
    'Apartamento': '118',
    'Genero Musical':'Trance'
}
#asignar valor a un elemento buscado por llave
print(diccionario)
diccionario['Apartamento']=18
print(diccionario)

#retornar el valor del diccionario asociado a la llave con 'get'

diccionario = {
    'Nombre':'Sebastian',
    'Apartamento': '118',
    'Genero Musical':'Trance'
}

print(diccionario.get("Genero Musical"))
print(diccionario["Genero Musical"])

#Cuando no hay una llave aparecera None
diccionario = {
    'Nombre':'Sebastian',
    'Apartamento': '118',
    'Genero Musical':'Trance'
}
print(diccionario.get('universidad', 'UNAB'))
#si no hay se escribe automaticamente
print(diccionario.get('MisionTIC'))
#aca aparecera NONE

#Operaciones que no modifican un diccionario
# len(d) : Devuelve el numero de elementos del diccionario
diccionario= {
    '1':180,
    '3':204,
    '2':160
}

print("len: {}".format( len(diccionario) ))

#min: (d) devuelve la minima del valor de la llave
#max: (d) devuelve el maxiomo del valor de la llave
#NO MODIFICA EL DICCIONARIO
diccionario= {
    '1':180,
    '3':'Artic',
    '2':'true'
}
print("min: {}".format( min(diccionario) ))
print("max: {}".format( max(diccionario) ))
print("len: {}".format( len(diccionario) ))

#sum(d) : Devuelve la suma de las llaves del diccionario, siempre que las llaves se pueden sumar
diccionario= {
    '13':180,
    '36':204,
    '28':160
}
#print(sum(diccionario))
#Aca sale error por que no esta declarado como numero
diccionario= {
    1:180,
    3:204,
    2:160
}
print(sum(diccionario))


#clave in diccionario : Devuelce True si la clave pertenece al diccionario y False en lado contrario
diccionario= {
    '1':180,
    '3':'Artic',
    '2':'true'
}
print('email' in diccionario)

#d. keys() : devuelve el iterador sobre las claves de l diccionario

diccionario= {
    '1':180,
    '3':'Artic',
    '2':'true'
}
print(diccionario.keys())

#d.values() : Devuelve iterador sobre los valores 
print(diccionario.values())

#d.items(): Devuelve un iterador sobre los pares clave-valor de un diccionario
print(diccionario.items())


#Operaciones que modifican el diccionario
diccionario= {
    '1':180,
    '3':'Artic',
    '2':'true'
}

#d[clave] = valor : añade al diccionario d. el par formado por la clave clave y vlor valor
diccionario['universidad'] = 'UNAB'
print(diccionario)

diccionario= {
    '1':180,
    '3':'Artic',
    '2':'true',
    'universidad':'UNAB'
}
#D.pop(clave, alternativo): devuelve el valor asociado a la clave y lo elimina del diccionario
diccionario.pop('universidad')
print(diccionario)

diccionario= {
    '1':180,
    '3':'Artic',
    '2':'true',
    'universidad':'UNAB'
}
#D.popitem() : Devuelve la tupla formada por la clave y el valor del ultimo par añadido
#al diccionario y lo elimina.
valorEliminado=diccionario.popitem()
print(valorEliminado)
print(diccionario)

diccionario= {
    '1':180,
    '3':'Artic',
    '2':'true',
    'universidad':'UNAB'
}
#Del. d[clave]: Elimina una clave
#d.clear(): Elimina todo el dicionario
del diccionario['3']
print(diccionario)
diccionario.clear()
print(diccionario)

diccionario= {
    '1':180,
    '3':'Artic',
    '2':'true',
    'universidad':'UNAB'
}
#copia de diccionarios
#Hay varios tipos de copiar
#copia por referencia d1 = d2
a ={1:'A', 2:'B', 3:'C'}
b=a
print(a)
print(b)
b.pop(2)
print(a)
print(b)
print("..............")
print("..............")

#copia por valor d1 = dict(d2)
a={4:'D', 5:'E', 6:'F'}
b=dict(a)
print(a)
print(b)
b.pop(5)
print(a)
print(b)

#FUNCIONES
#funcion "def" es un bloque de codigo
#que tiene asociado un nombre
#def <nombre-funcion>(<parametro>):

def bienvenida():
    print('Welcome to Python')
    return
bienvenida()    

def bienvenida(nombre, apellido):
    print('Welcome to Python', nombre, apellido)
    return
#pasa los argumentos posicionalmente
bienvenida('Sebastian', 'Ordoñez')
bienvenida('Iris', 'Barrera')
#pasa los argumentos nominalente
bienvenida(apellido = 'Rodriguez', nombre = 'Mafe')

def area_triangulo(base, altura):
    return base * altura / 2
area_triangulo(2, 3)
area_triangulo(4, 5)  
print(area_triangulo(2, 3))
'''
def operacionesMatematicas(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
resultado = operacionesMatematicas(5, 4, "*")
print("El resultado es de: ", resultado)       