#CLASES EN PYTHON
#Ya vamos con lo que es con la programacion en objetos en Python
#Primero vamos con las estructuras para definir una clase simpe:
#Ejemplo:
class ClassSimple:
    pass
#Por el momento es ta simple sin nada mas, nada de propiedades
#ni actividades.

#Ahora vamos con un objeto, el cual el programa seria asi:
#Ejemplo:
miPrimerObjeto = ClassSimple

#Ahora vamos a hablar de las PILAS
#Que es? -  Es una estructura desarrollada para almacenar datos de una manera 
#muy especifica
#En el TI se le llama con unas siglas UEPS en español LIFO en ingles.
#UEPS significa Ultimo en Entrar, Primero en Salir, 
#LIFO Last In - First Out

#Esta tiene dos operadores Elementales deniminadas:
#Push - cuando se coloca un elemento se coloca en la parte superios
#Pop - Cuando un elemento existente se retira de la parte superior

#Estructura de creacion---
#De por si la pila ya esta creada --- 
#pila = []
#Ahora estamoslistos para definir una funcion que pone el valor de la pila:
# - El nombre para la funcion es "push"
# - La funcion obtiene un parametro
# - La funcion no devuelve nada
# - La funcion agrega el valor del parametro al final de la pila
#EJEMPLO
#def push(val):
#    pila.append(val)

#Ahora es tiempo de que una funcion quite un valor de la pila, de la siguiente forma:
# - El nombre de la funcion es pop
# - La funcion no obtiene ningun parametro
# - La funcion devuelve el valor tomado de la pila
# - La funcion lee el valor de la parte superior de la pila y lo elimina

#Ahora se mostrara la funcion esta aqui:

pila = []

def push(val):
    pila.append(val)

def pop():
    val = pila[-1]
    del pila[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())

#Ahora es tiempo de usar las pilas enfocados a objetos
#Se comienza usando una clase - class Pila:
# - Queremos que la clase tenga una propiedad como el almacenamiento de la pila
#    tenemos que "instalar" una lista dentro de cada objeto de la clase
# - Despues, queremos que la lista este oculta de la vista de los usuarios de la clase

#Y como se hace?
#En Python no hay medios para declarar una propiedad como esa, En su lugar, se debe
#agregar una instruccion especifica  de manera manual.
#Tienes que equipar al aclase con una funcion especifica
# - Tiene que ser nombrada de forma estricta
# - Se invoca implicitamente cuando se crea el nuevo objeto
#Esta funcion se llama constructor, ya que su proposito es construir un nuevo objeto
#EJEMPLO:
class Pila:    # define la clase Pila
    def __init__(self):    # define la función del constructor
        print("¡Hola!")

objetoPila = Pila()    # instanciando el objeto

# - El nombre del constructo es siempre __init__
# - Tiene que tener al menos un parametro; el parametro se usa para representar
#el objeto recien creado: puede usar parametros para manipular el objeto y enriqueserlo
# - El parametro obligatorio generalmente se denomina "self" el cual simplifica 
#el proceso de lectura y comprension del codigo

#Cualquier cambio que se realice dentro del constructor que modifique el estado del
#parametro "self " se vera reflejado en el objeto recien creado.
#Ahora se agregaran solo una propiedad al nuevo objeto:
#EJEMPLO - 
class Pila:
    def __int__(self):
        self.listaPila = []

objetoPila = Pila()
print(len(objetoPila.listaPila))

# - Se ha usado la notacion punteada, al igual que cuando se invocan metodos. Esta es la manera
#    general para acceder a las propiedades de un objeto: se debe nombrar el objeto, poner un punto( . )
#    despues de el, y especificar el nombre de la propiedad deseada, NO USAR PARENTESIS, no se 
#    desea invocar un metodo, lo que se desea es acceder a una propiedad.

# - Si establecemos el valor de una propiedad por primera vez (como en el constructor ), lo 
#    estamos creando; a partir de ese momento, el objeto tiene propiedad y esta listo para usar su valor

# - Hemos hecho algo mas en el codigo: hemos intentado acceder a la propiedad "listaPila" desde
#   fuera de la clase inmediantamente despues de que se haya creado el objeto; queremos verificar
#   la longitud verificar la longitud de la pila. Lo cual se a logrado ya que el resultado es 0

#Ahora agregaremos dos guiones bajos antes del nombre "listaPila"
#En cambio invalida el programa. ¿Por que?
#Cuando cualquier componente de la clase tiene un nombre que comienza con dos guiones bajos (__)
#se vuelve privado - eso significa que solo se puede acceder desde la clase.
#EJEMPLO DEL ERROR ANTERIORMENTE DICHO
class Pila:
    def __init__(self):
        self.listaPila = []

objetoPila = Pila()
print(len(objetoPila.__listaPila))


# = Traceback (most recent call last):
 # File "main.py", line 6, in <module>
  #  print(len(objetoPila.__listaPila))
#AttributeError: 'Pila' object has no attribute '__listaPila'

#Vamos con el enfoque orientado a objetos con una pila desde cero
#Ahora es el momento de usar las funciones "push" y "pop" este tipo deberia estar 
#inmensa dentro del cuerpo de la clase. Lo que queremos es agregar "push" y quitar "pop"
#Tal componente es llamado publico, por ello no puede comenzar su nombre con dos o mas guiones bajos
#ademas el nombre no debe tener mas de un guion bajo
#EJEMPLO
class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


objetoPila = Pila()

objetoPila.push(3)
objetoPila.push(2)
objetoPila.push(1)

print(objetoPila.pop())
print(objetoPila.pop())
print(objetoPila.pop())

#Aca es obligatorio el parametro "self", todos los metodos deben  tener este parametro. Esto permite que 
#el metodo acceda a entidades (propiedades y actividades/metodos) del objeto.
#El metodo esta obligado a tener al menos un parametro, que Python mismo utiliza

#Nuevo Ejemplo para ver lo que pasa
class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


objetoPila1 = Pila()
objetoPila2 = Pila()

objetoPila1.push(3)
objetoPila2.push(objetoPila1.pop())

print(objetoPila2.pop())

#Aca existen dos pilas creadas a partir de la misma clase base. Trabajan independientemente
#Se pueden crear mas si se quiere

#Ahora vamos a  agregar una nueva clase para manejar pilas
#La nueva clase deberia poder evaluar la suma de todos los elementos almacenados
#actualmente en la pila
class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val  

class SumarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0
#Primero  - Solo se define una nueva subclase que apunte a la clase que se usara 
#como superclase. Asai se ve - "class SumarPila(Pila):"
#La clase aun no define ningun componente nuevo, pero eso nosignifica que este vacia
#Obtiene todos los componentes definidos por su superclase
#Al contrario de muchos otros lenguajes, Python te obliga a invocar explicitamente el constructor de una superclase
#Omitir esto generaria efectos nocivos: el objetivo se veria privado de la lista "__listaPila"
#Esta es la unica vez que se puede invocar a cualquiera de los constructores disponibles explicitamente
#Eso si hay que tener en cuenta la sintaxis:
# - Se especifica el nombre de las superclases
# - Se pone un punto ( . ) despues del nombre
# - Se especifica el nombre del constructor
# - Se debe señalar al objeto que debe ser inicializado por el constructor; Es por eso que se debe especificar el argumento y
#   utilizar la variable "self" aqui. Hay que recordar que invocar cualquier metodo desde fuera de la clase nunca requiere colocar
#   el argumento "self" en la lista de argumentos

#Segundo - Agregaremos dos metodos. Significa que vamos a cambiar la funcionalidad de los metodos, no sus nombres
#Lo que se espera de la funcion "push" aca, es: agregar el valor a la variable "__sum" y agregar el valor de la pila
#Hay que tomar en cuenta la forma en que hemos invocado la implementacion anterior del metodo "push":
# - Tenemos que especificar el nombre de la superclase asi indicamos claramente la clase quecontiene el metodo
# - Tenemos que especificar el objetivo de destino y pasarlo como primer argumento
class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val  

class SumarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0

def push (self, val):
    self.__sum += val
    Pila.push(self, val)

#Hasta ahora hemos definido la funcion "__sum", pero no le hemos proporcionado un metodo para obtener su valor.
#Como lo mostramos y lo protegemos de modificaciones
#Tenemos que definir un nuevo metodo el cual nombraremos "getSuma" el cual su unica tarea sera devolver el valor de "__sum"
#EJEMPLO
class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val  

class SumarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0


    def getSuma(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Pila.push(self, val)

    def pop(self):
        val = Pila.pop(self)
        self.__sum -= val
        return val


objetoPila = SumarPila()

for i in range(5):
    objetoPila.push(i)
print(objetoPila.getSuma())

for i in range(5):
    print(objetoPila.pop())

#Como se puede ver se agregaron 5 valores subsiguientes en la pila, imprimimos su suma
#y sacamos todos de la pila.
