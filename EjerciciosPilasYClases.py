#PILAS
#EJEMPLO DE COMO FUNCIONA UNA PILA
'''
#Ingresar
pila = [1,2,3]
print (pila)

pila.append(4)
print (pila)

pila.append(5)
print(pila)

#Sacar elementos

n = pila.pop()

print("El elmento que sacamos es {n}")
print("El elemento que sacamos es: ", n)
print(pila)

#PILA BASICA CON FUNCIONES
 
 #forma basica

def  pila_ingresa(pila, elemento):
    pila.append(elemento)
    return elemento

def pila_sacar(pila):
    elemento = pila.pop()
    return pila

def cola_ingresar(cola, elemento):
    cola.append(elemento)
    return cola

def cola_sacar(cola):
    elemento= cola.pop(0)
    return elemento

#*********************************

pila = [1,2,3]
pila = pila_ingresa(pila, 4)
print (pila)

elemento = pila_sacar(pila)
print("Sacamos el elemento")
print(pila)

#COLAS
#Ejemplo basico de funcionamiento

cola =  ["Jose", "Pablo", "Juan"]
print(cola)
cola.append("Victor")
print(cola)

habitante = cola.pop(0)
print(habitante)

#COLAS CON FUNCIONES

print("El habitante que se atiende es  ", habitante, "y los que quedan son ", cola)

cola = cola_ingresar(cola, "victor")
print(cola)

habitante = cola_sacar(cola)
print(f"El habitante que se atiende es {habitante} y la cola es {cola}")

#CLASES --

class Cerveza:
    def __init__(self, nombre):
        self.nombre = nombre

    def añejar(self, tiempo):
        print("Tu serveza se ha añejado en el tiempo  10 dias")

MiCerveza = Cerveza("Caucazo")        
MiCerveza.añejar()
print(MiCerveza.nombre)
'''
#Ejercicios y Ejemplos

#Pila en clase con funciones definidas Incluir  - Extraer 

#Creacion de la clase pila
class Pila:

    #Definicion de la clase con __int__ y self
    def __init__(self) :
        self.items = []

#Definicion de vacio 
    def estaVacia(self):
        return self.items == []

 #Definicion de incluir objetos
    def incluir(self, item):
        self.items.append(item)

#Definicion de extracion de objetos
    def extraer(self):
        return self.items.pop()

#definicion de busqueda de objetos
    def inspeccionar(self):
        return self.items[len(self.items)-1]

#Definicion del tamaño de la lista    
    def tamaño(self):
        return len(self.items)

#Ahora se hara uso de la pila que se creo importandolo

# from pythoned.basicas .pila import Pila

#En este caso no es necesario importar

#Se implementa la pila creada para ingresar y sacar objetos mientras 
#se revisa el tamaño y objetos dentro

p = Pila()

print(p.estaVacia())
p.incluir(4)
p.incluir('perro')
print(p.inspeccionar())
p.incluir(True)
print(p.tamaño())
print(p.estaVacia())
p.incluir(8.4)
print(p.extraer())
print(p.extraer())
print(p.tamaño())

