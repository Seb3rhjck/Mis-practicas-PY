'''
#ALMACENAMIENTO LISTAS CSV
#SE USA PARA CREAR Y GUARDAR LISTAS
#Para ingresarlo se usa IMPORT CSV
#Elementos a usar:
# whit = permite abrir un archivo dentro de un bloque
# newline = indica el caracterde salto de linea que deos usar
# writer = es un escritor que creamos para trabajar
# delimiter = es un delimitador que usamor para separar los valores
# writerow = sirve para escribir una fila en el archivo csv

import csv
from os import write
def EscribirArchivo():
    contactos = [
        ("sebastian", "dj", "genial"),
        ("iris", "ama de casa", "samalat"),
        ("elizabeth", "hija", "hola")
    ]
    with open("contactos.csv", "w", newline="\n", encoding="utf8") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for contacto in contactos:
            writer .writerow(contacto)
if  __name__ == "__main__":
    EscribirArchivo()            

#reader= es unlector y sirve para leer cada fila del archivo csv
# LECTURA DE LISTA EN CSV
# importar el modulo de csv para poder trabajar con este tipo de archivos
import csv
from os import system as s
def LeerArchivo():
  s("cls")
  # reader es un lector y sirve para leer cada fila del archivo csv
  with open("contactos.csv", "r", newline="\n", encoding="utf8") as csvfile:
      reader = csv.reader(csvfile, delimiter=",")
      # Imprimir los valores como una lista
      for contacto in reader:
          print(contacto)
      # Imprimir por asignación multiple
      #for nombre, empleo, email in reader:
      #    print(nombre, empleo, email)

if __name__ == "__main__":
    LeerArchivo()

#ESCRITURA DICCIONARIOS
from os import system as sy
def leerLista_EscribirDict():
    sy("cls")
    import csv
    contactos = [
        ("Sebastian Ordoñez Arias", "Dj", "soadj118@gmail.com"),
        ("Cristian Alexander Rodriguez", "Director de doblaje", "alexro89@hotmail.com"),
        ("Santiago Rodriguez Ordoñez",  "Manofactura", "santiagoRo@hotmail.com"),
        ("Maria Fernanda Rodriguez", "Fotografia", "mariatarrito11@hotmail.com")
    ]
    #dicwriter = Es el escritor para colecciones de datos de tipo diccionario
    #fieldnames = indica nombre de las claves o campos en el arrchivo csv que contiene el diccionario
    #writerheader = sirve para escribir  los campos  o claves en el archivo csv
    with open("contactos.csv", "w", newline="\n", encoding="utf8")as csvfile:
        campos = ["Nombre", "Empleo", "Email"]
        writer = csv.DictWriter (csvfile, fieldnames=campos)
        writer.writerow()
        for Nombre, Empleo, Email in contactos:
            writer.writerow({
                "Nombre" : Nombre, "Empleo" : Empleo, "Email" : Email
            })
if __name__ == "__main__":
    leerLista_EscribirDict()            

#LECTURA DE DICCIONARIO CSV
#DictReader = Es un lector para leer cada fila de un archivo csv escrito en forma de diccionario
from os import system as sy
import csv
def LeerDict():
    sy("cls")
    with open("contacto.csv", "r", newline="\n", encoding="utf8") as csvfile:
        reader= csv.DictReader(csvfile)
        for contacto in reader:
            print(contacto)

if __name__ =="__main__":
    LeerDict()

#Ejercicio juegos
from os import system as sy
import csv

def LeerVideoJuegos():
    sy("cls")

    with open("videojuegos.csv", "r", newline="\n", encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")        
        next(reader, None)
        nombreJuego = 0
        acumuladorCalificacion = 0
        acumuladorPrecios = 0
        contador = 0

        for videojuego in reader:
            nombreJuego = videojuego[0]
            calificacionJuego = int(videojuego[1])
            precioJuego = float(videojuego[2])

            acumuladorCalificacion = acumuladorCalificacion + calificacionJuego
            acumuladorPrecios = acumuladorPrecios + precioJuego
            contador = contador + 1

        promedioCalificacion = acumuladorCalificacion / contador
        promedioPrecios = acumuladorPrecios / contador
        print(f"El promedio de precios es: {promedioPrecios} y el promedio de calificación es: {round(promedioCalificacion, 2)}")

if __name__ == "__main__":
    LeerVideoJuegos(

#ARCHIVOS JSON
#Se debe importar el modulo JSON
#JASON = Java Script Object Notation - Notacion de objeto de JavaScript
#Se requiere de doble comillas
from os import system as sy  
import json

def escribirJson():
    contactos = [
        ("Sebastian Ordoñez Arias", "Dj", "soadj118@gmail.com"),
        ("Cristian Alexander Rodriguez", "Director de doblaje", "alexro89@hotmail.com"),
        ("Santiago Rodriguez Ordoñez",  "Manofactura", "santiagoRo@hotmail.com"),
        ("Maria Fernanda Rodriguez", "Fotografia", "mariatarrito11@hotmail.com")
    ]   
    datos=[]
    for nombre, empleo, email in contactos:
        datos.append({"nombre":nombre, "empleo":empleo, "email":email})
    with open("contactos3.json", "w") as jsonfile:
        json.dump(datos, jsonfile, indent=4)

if __name__ == "__main__":
    escribirJson()

#Lectura

import json
with open("contastos2.json") as jsonfile:
    datos = json.load(jsonfile)
    for contacto in datos :
        print(contacto)   

import json
data = {}

data['clientes'] = []

data['clientes'].append({
    'nombre': 'Ingrid',
    'apellido': 'Martinez',
    'edad': 27,
    'estatura': 1.62})

data['clientes'].append({
    'nombre': 'Jhon',
    'apellido': 'Hernandez',
    'edad': 31,
    'estatura': 1.78})

data['clientes'].append({
    'nombre': 'Tomas',
    'apellido': 'Rivera',
    'edad': 36,
    'estatura': 1.84})

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4) 
    
#ejemplo lectura json
import json
with open('data.json') as file:
    data = json.loa(file)
    for cliente in data['cliente']:
        print(cliente)
        print(' ')
'''
#Ejemplo escritura
import json

def escribirJson():
    contactos = [
        ("Miguel Restrepo", "Desarrollar Web", "miguel.restrepo@o365.unab.edu.co"),
        ("Jesús Londoño", "Gerente de Proyectos", "jesus.londono@o365.unab.edu.co"),
        ("Yuri Salinas", "Analista de Datos", "yuri.salinas@o365.unab.edu.co"),
        ("Andrea Palacios", "experta en python", "andrea.palacios@o365.unab.edu.co")
    ]

    datos = [ ]
    for nombre, empleo, email in contactos:
        datos.append({"nombre":nombre, "empleo":empleo, "email":email})
    with open("contactos3.json", "w") as jsonfile:
        json.dump(datos, jsonfile, indent=4, ensure_ascii=False)

def leerJson():
    with open("contactos3.json") as jsonfile:
        datos = json.load(jsonfile)        
    return datos

def escribirNuevoElemento(contactos):
    contactos.append(
            {
                "nombre": "Miguel Angel Londoño", 
                "empleo": "Desarrollar Web", 
                "email": "miguel.londono@o365.unab.edu.co"
            }
        )

    with open("contactos3.json", "w") as jsonfile:
        json.dump(contactos, jsonfile, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    escribirJson()
    contactos = leerJson()
    escribirNuevoElemento(contactos)
#Los modulos anteriores son modulos sencillos y utiles de lectura y escritura.