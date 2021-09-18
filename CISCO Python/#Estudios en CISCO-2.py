#MODULOS
"""
#Son un paquete de codigos
#Para crear modulos se tienes dos cuestiones diferentes:
#-El mas comun es que se desea usar un modulo ya existente, aca  se considera el 
#programador como usuario del modulo
#-El segundo es cuando se desea crear un nuevo modulo, ya sea para uso propio
# o para otrros, aca el programador es un modulo
#Un ejemplo seria Python:
#Viene con una gran cantida de modulos los cuales crean la biblioteca estander de Python
#como los modulos math. modulos de lectura. etc

#Importando modulos-
#Es como sacar un libro del estante, y se hace mediante una instruccion llamada "import"
#"import" tambien es una palabra reservada
#EJEMPLO: import sy,  o,  import time
#EJEMPLO2 -Con namescape conflictivo:
import math
print(math.sin(math.pi/2))
#EJEMPLO3 - Con dos namescape:
import math

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

#Tambien si queremos un namescape especifico en el "import" usamos el comando "from"
#EJEMPLO:
from math import pi
#EJEMPLO - en medio de una funcion:
from math import sin, pi

print(sin(pi/2))

pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi/2))

#IMPORTANDO UN MODULO : *
#Es un metodo agresivo e importa todas las entidades del modulo indicado
#EJEMPLO:
from math import *
#Eso si es un metodo muy arriesgado ya que si no se tiene conocimiento de los nombres de
#todos los componentes de un modulo, habra conflictos  de nombre. Esto solo es una solucion 
#temporal y no tratar de usarlo en un codigo regular

#PALABRA RESERVARA "AS" PARA DAR UN ALIAS
#Si se quiere dar un nombre distinto al modulo, para dar mas accecibilidad. se le puede 
#asignar un alias con la funcion "as"
#EJEMPLO:
import math as m
#"as" es una palabra reservada
#Tambien se puede usar para darle un alias a un namescape especifico
#EJEMPLO:
from math import pi as p, sin as sn

#Para poder conocer todos los namescape de un modulo se usa el comando "dir()" en el IDLE de Python
#Un ejemplo seria:
import math

for name in dir(math):
    print(name, end="\t")
#Usar esta funcion para conocer mas los componentes del modulo

#Intentemos con el modulo "math"
#Funciones trigonometricas
# - "sin(x)"= seno de x  - - "cos(x)" = coseno de x  - - "tan(x)" = tangente de x
#Toman un argumento en radianes y hay que tener cuidado con "tan()" ya quee no todos
#los argumenntos son aceptados
#Aca las versiones inversas:
#- "asin(x)" = arcoseno de x - - "acos(x)" = arcoseno de x - - "atan(x)" = arcotangente de x
#estas funciones toman un argumento (que sea correcto) y devuelven una medida de un angulo en radianes

#Para trabajar mejor con mediciones de angulos se usan las siguientes:
#- "pi" = una constante con un valor que es aproximacion de pi
#- "radians(x)" = convierte x de grados a radianes
#- "degress(x)" = convierte en grados

#Tan bien hay analogos hiperbolicos 
#"sinh(x)"= seno hiperbolico - "cosh(x)" = coseno hiperbolico - "tanh(x)" = tangente hiperbolico
#"asinh(x)" = arcoseno hiperbolico - "acosh(x)" = arcocoseno hiperbolico - "atanh(x)" = arcotangente hiperbolico

#Funciones relacionadas con la exponenciacion
# - "e" = Una constante con un valor que es una aprox. del numero Eular(e)
# - "exp(x)" = Encontrar el valor de "e**x"
# - "log(x)" = logaritmo natural de x
# - "log(x, b)" = logaritmo de x con base b
# - "log10(x)" =logaritmo decimal de x (mas presiso que "log(x, 10)")
# - "log2(x)" = logaritmo binario de x (pasa lo mismo que "log1()")

#hay otra funcion incorporada pero no se tiene que importar
# - "pow(x, y)" = encuentra el valor de x a la y (toma en cuenta los dominios)

#Luego hay un grupo de de funciones con proposito general
# - "ceil(x)" = devuelve el entero mas pequeño mayor o igual que x
# - "floor(x)" = el entero mas grande menor o igual que x
# - "trunc(x)" = el valor de x truncado a un entero (no es equivalente a ceil o floor)
# - "factorial(x)" = deveulve x! ( x tiene que ser un entero no negativo)
# - "hypo(x, y)" = devuelve la longitud de la hippotenusa de un triangulo con las longitudes de los catetos iguales z x e y ( este es mas preciso)

#El modulo "random"
#El modulo "random" tiene una funcion llamada "random()", el cual produce un numero flotante
#x entre el rango (0.0, 1.0).

#La funcion "seed()", establece una semilla del generador. Tiene variables:
#seed() = Establece la semilla con la hora actual
#seed(int_value) = establece la semilla con el valor entero - int_value

#Si se quiere numeros enteros, las siguientes funciones serviran:
# randrage(fin)
# randrage(inicio, fin)
# randrage(inicion, fin, incremento)
#Estos generan un numero seudoaleatorio, entero tomado de un rango

# randint(izquierda, derecha)
#Este da un numero aleatorio entero

#Las anteriores funciones, tienen una desventaja importante:
#Pueden producir valores repetidos incluso si el numero de invocaciones posteriores no es mayor 
#que el rango especifico
#Pero si se quiere un random mas especifico como para una loteria  tenemos una funcion llamada "choice" y "sample"
# - choice(secuencia) = elige un elemento aleatorio de la secuencia de entrada y lo devuelve
# - sample(secuencia, elemento_a_elegir=1) = crea una lista (de muestra) que consta del elemento "elemto_a_elegir" (por defecto 1)sorteado de la secuencia de entrada

#MODULO PLATFORM
#el modulo "platform" permite acceder a los datos de la plataforma, es decir, hardware
#sistema operativo e informacion sobre la version del interprete.
#Asi es como se invoca:
import platform
platform(alised = False, terse = False )
#Se mostraron dos funcionse de lmodulo "platform": "alised" y "terse"
# "alised" = cuando se establece a True, puede hacer que la funcion presente los nombre
#                  de cada capasubyacente alternativos en un lugar de los comunes
# "tersed" = cuando se establece True puede convercer a la funcion de presentar una forma
#                   mas breve del resultado (si lo fuera posible)

#Si se quiere conocer el nomre generico del procesador que se ejecuta el sistema operativo
#junto con Python y el codigo, una funcion llamada "machine()"
#Otra funcion es "processor()" el cual devuelve una cadena con el nombre real del procesador(si es posible)
#Otra seria "system" (no confundir con el modulo system) el cual devuelve el nombre
#generico del sistema operativo en una cadena

# "version()" = se proporciona la version del sistema operativo en una cadena

#EXCEPCIONES
#Hay veces en python que los codigos tienen errores y al ser ejecutados genera excepciones de procesamiento
#Para manejar estas excepciones se usa la palabra "try" el cual es un palabra reservada, y su funcion es de hacer un intento
# - Primero se debe intentar (try) hacer algo
# - Despues, se tiene que comprobar si todo salio bien
#Y para sacar excepciones se usa la palabra reservada "except"
#Se usan de manera vertical y siempre inicinado el codigo y por lo general van en un bucle
#Ejemplo:
b = 18
while (True):
    try:
        if b > 18:
            print("genial")
        else:
            print("Muy menor")
    except:
        print("Valor invalido")
        break
#Ejemplo2:
try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh cielos, algo salio mal...")

print("3")

#Tambien se puede usar varios excepts con los errores
#Ejemplo:
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salio mal...")

print("THE END.")

#En las excepciones hay una instruccion laamada "raise" que genera la excepcion especifica
#denominada "exc" como si fuese generada de manera natural
# "raise" es una palabra reservada

#Esta instruccion simula excepciones reales, y parcialmente maneja una excepcion y 
#hace que otra parte del codigo sea responsable de completar el manejo
#Ejemplo
def badFun(n):
    raise ZeroDivisionError

try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")

#Tambien hay otras formas de usar "raise"
#Ejemplo
def badFun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise

try:
    badFun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")

#Esta variante de la instruccion "raise" solo puede ser solamente dentro de la rama "except"
#Gracias a esto, se puede distribuir el manejo de excepciones entre diferentes partes del codigo

#Tambien hay una instrucion llamada "assert"
# - "assert" = Evalua la expresion. Si la expresion es (True), o un valor numerico distinto
#                    de cero, o una cadena no vacia, o cualquier otro valor diferente de (None),
#                    no hara nada mas. De lo contrario, automaticamente e inmediantamente genera
#                    una excepcion llamada "AssertionError"(En caso de que la afirmacion haya fallado)
#Puedes ponerlo en la parte del código donde quieras estar absolutamente a salvo de datos incorrectos, y donde no estés absolutamente seguro de que los datos hayan sido examinados cuidadosamente antes (por ejemplo, dentro de una función utilizada por otra persona).
#El generar una excepción AssertionError asegura que tu código no produzca resultados no válidos y muestra claramente la naturaleza de la falla.
#Las aserciones no reemplazan las excepciones ni validan los datos, son suplementos.

#EJEMPLO
import math

x = float(input("Ingresa un numero: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)
"""
#Cuanto hay uso de cadenas multiples el contexto anterior mentevisto lanza un error
#Para este tipo de cadenas Python ofrece una sintaxis simple, conveniente y separada

#multiLinea = '''Linea #1
#Linea #2'''

#print(len(multiLinea))

#Como se ve, la cadena comienza con tres apostrofes, esto es usa para terminar la cadena

#En la salida de este codigo es 17, contando el espacio esn blanco ya que es igual a "\n"
#Tanbien se pueden usar comillas dobles "

#Tambien se pueden hacer con operaciones con cadenas, pueden ser:
# - Concatenados(unidas)
# - Replicadas

#En estas se pueden usar el : + =se puede usar en una o mas cadenas y produce una cadena nueva
# * = Necesita una cadena y un numero como argumentos sin importar el orden, la cadena se repite x veces como indique el numero

#El metodo "capitalize()" = Crea una nueva cadena con los caracteres tomados de la cadena fuente
#El cual intenta modificalos de la siguiente manera:
# -Si el primer caracter dentro de la cadena es una letra, se convertira a mayusculas.
# -Todas las letras restantes de la cadena se convertiran a minusculas.
#EJEMPLO:
print('aBcD'.capitalize())
#Da como resultado = abcd

#Tambien se puede centrar con el metodo "center()", el cual genera una copia de la cadena
#original, tratando de centrarla dentro de un campo de un ancho especificado. eso si el centrado se 
#le agrega algunos espacios antes y despues de la cadena.
#EJEMPLO:
print('[' + 'alfa'.center(10) + ']')
#El cual el resultado es = [     alfa     ]

#La variante de dos parametros de "center()" hace uso del caracter del segundo argumento, en lugar
#de un espacio.
#EJEMPLO:
print('[' + 'gamma'.center(20, '*') + ']')
#El resultado es  = [*******gamma*******]

#El metodo "endswith()", comprueba si la cadena dad termina con el argumento especificado y
#devuelve - True o False - dependiendo del resultado.
#La subcadena se adhiere al ultimo caracter de la cadena; no se puede ubicar en 
#algun lugar cerca del final de la cadena.
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")
#da como resultado - si
# El metodo "find()", es similar al metodo "index()", el busca una subcadena ydevuelve al indice de la 
# primera aparicion de esta subcadena, pero:
#  - Es mas seguro, no genera un error para un argumento que contiene una subcadena inexistente
#  - Funciona solo con cadenas  - no se debe aplicar a ninguna otra secuencia
#Ejemplo
txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)

#El codigo imprime los indices de todas las ocurrencias del articulo "the", su resultado es
# - 15 - 80 - 198 - 221 - 238 -

#El metodo "isalnum()" es un metodo sin parametros, el cual comprueba si la cadena contiene solo digitos 
#o caracteres alfaeticas y devuelve True o False de acuerdo al resultado
#Ejemplo
t = 'Six lambdas'
print(t.isalnum())

t = 'ΑβΓδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

#Da como resultado - True - False - True
#Eso si toca tener cuidado con los espacios ya que no son letras ni digitos.

#Este metodo tiene mass metodos, uno enfocado a los digitos y el otro a letras , otro a las minusculas, a los espacios  y otro a las mayusculas
# "isalpha()" - letras
# "isdigit()" - digitos
# "islower()" - minusculas
# "isspace()" - espacios
# "isupper()" - mayusculas

#METODO "join()"
# - Realiza una union y espera un argumento del tipo lista; se dee asegurar que todos los elementos de la lista
#    sean cadenas de lo contrario genera un excepcion tipo "TypeError"
# - Todos los elementos de la lista seran unidos en una sola cadena, pero la cadena desde la que se ha invocado
#    el metodo sera utilizada como separador puesta entre las cadenas.
# - La cadena recien creada se devuelve como resultado
#EJEMPLO:
print(",".join(["omicron", "pi", "rho"]))

#Otros metodos - "lower()"=para leer solo minusculas  - "upper()"=para leer solo mayusculas
#El "lstrip()" es un metodo sin parametros devuelve una cadena recien creada formada a 
#partir de la original eliminando todos los espacios en blanco iniciales 
#Ejemplo
print("www.cisco.com".lstrip("w."))
#da como resultado = cisco.com
#El metodo "replace()", con dos parametros devuelve una copia de la cadena original en la
#que todas las aparaiciones del primer argumento han sido reemplazados por el segundo argumento
#EJEMPLO
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
#El resultado es - www.pythonintitute.org - This are it!  - Apple
# "rfind()" comienza sus busquedas desde el final de la cadena
# "rstrip()"hace casi lo mismo que "lstrip()" pero afecta el lado opuesto de la cadena
# "split()" divide la cadena y crea una lista de todas las subcadenas detectadas
print("phi       chi\npsi".split())
#Da como resultado ['phi', 'chi', 'psi']
# "starswith()" es un espejo del metodo "endswith()"- comprueba si una cadena comienza con las subcadea especificada
# "strip()" combina los efectos de "rstrip()" y "lstrip()", crea una nueva cadena quecarece de todos los espacio en blanco iniciales y finales 
# "swapcase()" crea un resultado intercambiando todas las letras mayusculas  o minusculas dentro de la cadena original y viceversa
# "title()" cambia la primera letra de cada palabra a mayusculas, y las demas en minusculas


#EJEMPLO cifrado Cesar en un codigo
text = input("Ingresa tu mensaje: ")
cifrado = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cifrado += chr(code)

print(cifrado)

#Y el codigo inverso es:
cifrado = input('Ingresa tu criptograma: ')
text = ''
for char in cifrado:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)


#Ejemplo de procesador de numeros
linea = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = linea.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")


#EJEMPLO de IBAN (cuentas bancarias internacionales)
iban = input("Ingresa IBAN, por favor: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("Has introducido caracteres no válidos.")
elif len(iban) < 15:
    print("El IBAN ingresado es demasiado corto.")
elif len(iban) > 31:
    print("El IBAN ingresado es demasiado largo.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    ibann = int(iban2)
    if ibann % 97 == 1:
        print("El IBAN ingresado es válido.")
    else:
        print("El IBAN ingresado no es válido.")
        