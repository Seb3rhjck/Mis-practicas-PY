#Estudios en CISCO
'''
#Condicionales if
contadordeOvejas = 0
dormirSoñar = 0 
if contadordeOvejas >= 120: #evalua una expresion de pruebas
    dormirSoñar() #se ejecuta si la expresion de prueba es Verdadera
    

#Ejemplo de If - Else
climaEsBueno = 0
irACaminar = 0
irAlCine = 0
almorzar = 0
encontramosBuenRestaurante = 0
comerSandwich = 0
hayBoletosDisponible = 0
irDeCompras = 0
mesasLibres = 0
jugarAjedrezEnCasa = 0

if climaEsBueno:
    irACaminar()
else:
    irAlCine()

#if-else encadenados

if climaEsBueno:
    if encontramosBuenRestaurante:
        almorzar()
    else:
        comerSandwich()
else:
    if hayBoletosDisponible:
        irAlCine()
    else:
        irDeCompras()

#Elif se usa para verificar mas de una opcion

if climaEsBueno:
    irACaminar()
elif hayBoletosDisponible:
    irAlCine()
elif mesasLibres:
    almorzar()
else:
    jugarAjedrezEnCasa()    
'''
#Ejemplos de codigo
#Ejemplo 1 - Identificar el numero Mayo

#Lee dos numeros
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))
#Elegir el numero mas grande
if numero1 > numero2:
    nmasGrande = numero1
else:
    nmasGrande = numero2
print("El numero mas grande es: ", nmasGrande)

#Ejemplo 2 - Otro estilo del mismo codigo

if numero1 > numero2 : nmasGrande = numero1
else: nmasGrande = numero2

print("El numero mas grande es: ", nmasGrande)
#Se puede agregar mas opciones

#PYTHON ES COMPATIBLE CON LOS SUGUIENTES OPERADORES LOGICOS:
#and =si ambos son verdaderos, la condicion es verdadera ej =
print("(True and true), es True")
#or = si alguno de los operadores es verdadero, la condicion es verdadera ej =
print("(True or False) es True")
#not = devuelve False si el resultado es verdadero y devuelve True si es falso ej =
print("not True es False")
#Se puede usar operadores bit a bit para manipular bits de datos individuales ej
#x = 15 el cual es - 0000 1111 - En binario
#y = 16 el cual es - 0001 0000 - En binario
#Se utilizan para ilustrar el significado de operadores bit a bit en Python.
# & - hace un bit a bit and(y), por ejemplo = x & y =0, el cual es 0000 0000 en binario
# | - hace un bit a bit or (o) por ejemplo = x | y = 31, el cual es 0001 1111 en binario
# ~ - hace un bit a bit not (no), por ejemplo = ~x = 240, el cual es 1111 0000 en binario
# ^ - hace un bit a bit xor, por ejemplo = x ^ y = 31, el cual es 0001 1111 en binario
# >> hace un desplazamiento bit a bit a la derecha por ejemplo =  y >> 1 = 8 el cual es 0000 1000 en binario
# << hace un dezplasamiento bit a bit a la izquierda  = y << 3 = , el cual es 1000 0000 en codigo binario

#En el ordenamiento de lista esta el metodo sort() para ordenar los elemento-
lst = (5, 3, 1, 2, 4)
print(lst)

lst.sort()
print (lst)

#Tambien se puede usar el reverse() para invertir una lista

lst1 = (5,3, 1, 2, 4 )
print(lst1)

lst1.reverse()
print(lst1)

#Rodajas - se usa para tomar una parte de la lista se usa el ( : )
#Se pueden usar las palabras claves in o not in, para ver si hay elementos existente en la lista

# Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

tabla = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(tabla)
print(tabla [0][0]) # salida: ':('
print(tabla [0][3]) # salida: ':)'

# Cubo - un arreglo tridimensional (3x3x3)

cubo = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cubo)
print(cubo [0][0][0]) # salida: ':('
print(cubo [2][2][0]) # salida: ':)'

#Instruccion "return"
#"return" sin una expresion- Se emplea para terminar las actividades de una funcion
#antes de que el control llegue a la ultima linea de la funcion 
#Ejemplo:

def felizAñoNuevo (deseos = True):
    print ("Tres...")
    print("Dos...")
    print("Uno...")
    if not deseos:
        return

    print("Feliz Año nuevo!") 

#Cuando se invoca sin ningun argumento - felizAñoNuevo - la funcion produce un poco de
#ruido, la salida se vera asi
#Tres...
#Dos...
#Uno...

#"return" con una expresion - en esta se extiende con una expresion.
#funcion():
    #return expresion

#Hay dos concecuencias de usarla:
#- Provoca la terminacion inmediata  de la ejecucion de la funcion
#- la fincion evaluara el valor de la expresion y lo devolvera
#Ejemplo-

def funcion_aburrida():
    return 123

x = funcion_aburrida()
print("La funcion_aburrida ha devuelto su resultado. Es:", x)

#Da como resultado - La funcion_aburrida ha devuelto su resultado. Es: 123

#Se puede enviar una lista a una fincion como un argumento? - Claro que se puede
#Entonces, si se pasa una lista una funcion, la funcion que manejaria como una lista.
#Ejemplo
def sumaDeLista(lst):
    sum = 0

    for elem in lst:
        sum+= elem
    return sum
#Y se invoca asi:
print(sumaDeLista([5, 4, 3]))
#Regresa "12" como resultado, pero habra problemas si la invocas de esta manera riesgosa:
#print(sumaDeLista(5))
#La respuesta de Python sera la siguiente:
#TypeError: 'int' object is not iterable
#Esto se debe al hecho de que el bucle "for" no puede iterar un solo valor entero.
#Puede una lista ser el resultado de una funcion?
#Cualquier entidad por Python puede se un resultado de funcion
#Ejemplo  --
def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    return strangeList

print(strangeListFunction(5))

#El resultado es [4, 3, 2, 1, 0]
#En resumen - Puedes emplear la palabra "return"  para decirle a nuna funcion que devuela
# un valor. La instruccion "return" termina la funcion.
def multiply(a, b):
    return a * b
print(multiply(3, 4))    # salida: 12
def multiply(a, b):
    return
print(multiply(3, 4))    # salida: None 
#-El resultado de una funcion se puede asignar facilmente a una variable, por ejemplo:
def deseos():
    return "¡Felíz Cumpleaños!"
d = deseos()
print(d)    # salida: ¡Felíz Cumpleaños!

#Ejemplos:
# Ejemplo 1
def deseos():
    print("Mis deseos")
    return "¡Felíz Cumpleaños!"

deseos()    # salida: Mis deseos


# Ejemplo 2
def deseos():
    print("Mis Deseos")
    return "¡Feliz Cumpleaños!"

print(deseos())    # salidas: Mis Deseos
                   #          ¡Feliz Cumpleaños!

#-Se puede usar una lista como argumento de una funcion
def HolaaTodos(myList):
    for nombre in myList:
        print("Hola,", nombre)

HolaaTodos(["Adam", "John", "Lucy"])

#Una lista tambien puede ser un resultado de funcion 
def createList(n):
    myList = []
    for i in range(n):
        myList.append(i)
    return myList

print(createList(5))
#-scopes
#El alcance de un nombre es la la parte del codigo donde el nombre es reconocido correctamente.
#El alcance del parametro de una funcion es la funcion en si misma. El parametro es
#inaccesible fuera de la funcion.
#FUNCIONES SIMPLES - Calcular el IMC
#Definamos el Indece de Masa Corporal (IMC)
#Seria: IMC= PESO(KG) / ALTURA(M)elevado a la 2
#La nueva funcion tendra dos parametros. Su nombre sera  "imc"
#Hora de codificar:
def imc(peso, altura):
    return peso/altura **2
print (imc(52.5, 1.65))
#el resultado seria - 19.283746556473833
# Calcular el IMC y convertir unidades del sistema metrico ingles al sistema metrico
def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None
    return peso / altura ** 2
print(imc(352.5, 1.65))
#El simbolo de diagonal invertido ( \ ) es empleado, si termina con esto se entendera que
#la linea continua en la siguiente
#Esto es util cuando se tienen lineas de codigo largas y se desea que  sean mas legibles

#Ahora se escribre dos funciones sencillas para convertir unidades del sistema 
#ingles al sistema metrico., comensando con las pulgadas, pero antes veamos con 
#las libras == 1 Lb = 0.46 Kg y se puede demostrar con la siguiente funcion la cual llamaremos "lbAkg":
def lbakg(lb):
    return lb * 0.45359237

print(lbakg(1))
#El cual el resultado es  0.45359237
#Ahora vamos con los pies y pulgadas == 1 pie = 0.3048m, y 1 pulgada =2.54 cm=0.0254m
#Y la funcion seria:
def piepulgam(pie, pulgada):
    return pie * 0.3048 + pulgada * 0.0254

print(piepulgam(1, 1))
#El resultado seria 0.3302
#Si uno quisiera usar pies sin pulgadas se deberia modificar el codigo asi.
def piepulgam(pie, pulgada=0.0):
    return pie * 0.3048 + pulgada * 0.0254

print(piepulgam(6))
#Ahora la pulgada tendra como valor definido 0.0 el cual da como resultado  1.83
#Ahora se puede buscar el IMC de una persona con el siguiente codigo:
def piespulgam(pies, pulgadas = 0.0):
    return pies * 0.3048 + pulgadas * 0.0254

def lbsakg(lb):
    return lb * 0.45359237

def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None    
    return peso / altura ** 2

print(imc(peso = lbsakg(176), altura = piespulgam(5, 7)))
#El resultado es 27.57 (obviamente estos son resultados redondeados)
# - Funciones con mas de tres parametros:
#En este caso la funcion tendra tres parametros uno para cada lado
#Regresa "True" si todos los lados pueden formar un triangulo, y "False" de lo contrario
#En este caso "esUnTriangulo"  sera el nombre de la funcion.
#Para que funcione los resultados deben ser "True" o "False"
#Una version compacta seria asi:
def esUnTriangulo(a, b, c):
    if a + b <= c or b + c <= a or \
    c + a <= b:
        return False
    return True

print(esUnTriangulo(1, 1, 1))
print(esUnTriangulo(1, 1, 3))

#Y se puede acortar aun mas:
def esUnTriangulo (a, b, c):
    return a + b > c and b + c > a and c + a > b

print(esUnTriangulo (1, 1, 1))
print(esUnTriangulo (1, 1, 3))

#Se remplazan  los "or" con  "and" obteniendo universal para probar triangulos
#Y en una funcion mas grande seria asi:
def esUnTriangulo(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(esUnTriangulo (1, 1, 1))
print(esUnTriangulo (1, 1, 3))

# - Otras funciones como triangulos y teorema de pitagoras
#Ahora teniendo la definicion del triangulo usaremos el teorema de pitagoras para poder
#sacar un triangulo rectangulo.
#Teniendo en cuenta que c**2 = a**2 + b**2 es el teorema de pitagoras
#Asi que el codigo seria:
def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

def esUnTrianguloRectangulo(a, b, c):
    if not esUnTriangulo  (a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

print(esUnTrianguloRectangulo(5, 3, 4))
print(esUnTrianguloRectangulo(1, 3, 4))

#Se establece una relacion entre la hipotenusa y los dos catetos.
#Se eligio el lado mas largo y se le aplico el teorema de pitagoras para verificar que estuviese en orden
#Otra funcion - Evaluando el campo de un triangulo 

#Formula de Heron == S= (a+b+c)/2  -  A= raiz de s(s -a)(s - b)(s - c)

#Vamos a emplear el operador de exponenciacion para calcular la raiz cuadrada == raiz de x = x**(1/2)
#Acontinuacion el codigo de esta expresion

def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

def campoTriangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        return None
    return heron(a, b, c)

print(campoTriangulo(1., 1., 2. ** .5))

#Ahora el resultado es 0.499999999999983 - Es cercano a 0.5 pero no es extactamente 0.5
#Es un error? nop es un flotante

#Factoriales:
#Los factoriales, son una expresion matematica de numeros enteros positivos acompañadas
#de la expresion "!", el cual, el numero que va con el numero es igual a la multiplicacion
#de 1 hasta el numero con la expresion.
#Ejemplo == 7! = 1*2*3*4*5*6*7 = 5040
#Ahora esta es la funcion:

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    producto = 1
    for i in range(2, n + 1):
        producto *= i
    return producto

for n in range(1, 6): # probando
    print(n, factorialFun(n))

#Estar pendiente  de como el bucle "for" se emplea

#Funcion fibonacci:
#Son una secuencia de numeros enteros los cuales siguen una sencilla regla:
# - el primer elemento de la secuencia es igual a uno (Fib1 = 1)
# - el segundo  elemento es tambien igual a 1 (Fib2 = 1)
# - Cada numero despues de ellos son la suma de los dos numeros anteriores (Fib¡ = Fib¡-1 + Fib¡+2)

#Aca una funcion para esta serie
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10): # probando
    print(n, "->", fib(n))

#Hay que analizar el bucle "for"
#Esta es una manera mas recursiva de hacerlo:
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
    