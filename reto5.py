from time import sleep as zzz
from os import system as sy
import json
import os

contactos =[]

def IngresoContacto(Nombre, Celular, Cumpleanos, Email):    
    Contacto = {
        "Nombre" : Nombre,
        "Celular" : Celular,
        "Cumpleaños" : Cumpleanos,
        "Email" : Email
    }
    contactos.append(Contacto)
    with open("Contactos_Agenda.json", "w") as jsonfile:
        json.dump(contactos, jsonfile, indent=4, ensure_ascii=False)
        
    print("Su contacto a sido agregado con exito, \(^ o ^)/")
    print("'-..-'"*10)
    input("Apachurrale enter para volver")

def BuscarContacto():
    sy("cls")
    print("--CONTACTOS MISIONTIC--")
    print("-o-o"*10)
    print("---BUSQUEDA DE CONTACTOS---")
    print("o-o-"*10)
    Buscar= input("Ingresa el nombre para ver si esta, s(-_o)7: ")
    if os.path.exists("Contactos_Agenda.json"):
            with open("Contactos_Agenda.json") as jsonfile:
                contactos = json.load(jsonfile)  

    for x in contactos:
        if  x.get("Nombre") == Buscar:
            print(x)   
            print("'-..-'"*10)
            break
        else:
            print("Lo siento bro, no se encuentra  v(u_u')v")
            return main
    print("'-..-'"*10)    
    input("Apachurrale enter para volver")        

def visualizarTodos():
    sy("cls")
    print("--CONTACTOS MISIONTIC--")
    print("-o-o" * 10)
    print("---CONTACTOS---")
    print("o-o-" * 10)
    
    try:    
        if os.path.exists("Contactos_Agenda.json"):
            with open("Contactos_Agenda.json") as jsonfile:
                contactos = json.load(jsonfile)        
            print(contactos)
    except:
        print("Lo siento no hay nada u(~_~)u")           
        zzz(3)
        sy("cls")
    print("'-..-'" * 10)    
    input("Apachurrale enter para volver")
    
def SolicitarCumpleanos():
   while (True):
        try: 
            cumpleanos=[]
            dia = int(input("Ingrese el dia del cumple plz: "))
            mes = int(input("Ingrese el mes del cumple plz: "))
            anos = int(input("Ingrese el año del cumple plz: "))
            for dia in range(1, 31):
                cumpleanos.append(dia)
            for mes in range(1, 12):              
                cumpleanos.append(mes)
            for anos in range(1940, 2005):                           
                cumpleanos.append(anos)
            else:
                print("Ingresa una fecha valida  v( º- º )v")
                return dia
        except:
            print("Ingrese valores validos ( -_- )")     
            return cumpleanos

def SolicitarDatos ():
    print("--VAMOS A INGRSAR TU CONTACTO--")
    print("-o-o"*10)
    print("o-o-"*10)
    Nombre = str(input("Ingrese el Nombre plz: "))
    Celular = str(input("Ingrese su Numero Celular plz: "))
    Cumpleanos = SolicitarCumpleanos()
    Email = str(input("Ingrese su Email, plz: "))
    IngresoContacto(Nombre, Celular, Cumpleanos, Email)

def PintarMenu():
    sy("cls")
    print("- - - AGENDA DE CONTACTOS MISIONTIC - - -")
    print("-o-o"*10)
    print("- - "*10)
    print("o-o-"*10)
    print("[A]gregar Contacto (~ + _ +)~")
    print("[B]uscar Contacto (-_o)7")
    print("[V]isualizar Contacto s(* o *)7")
    print("[S]alir del programa (T n T) /")
    print("-o-o"*10)
    print("- - "*10)
    print("o-o-"*10)

def main():
    sy("cls")
    while (True):
        PintarMenu()
        Inicio = str.upper(input("Escoge una opcion plz:"))
        if Inicio ==  "A":
            sy("cls")
            SolicitarDatos()
        elif Inicio == "B":
            sy("cls")
            BuscarContacto()
        elif Inicio == "V":
            sy("cls")
            visualizarTodos()
        elif  Inicio == "S":
            print("Esto se acabo, BYE , (^u^)/")
            break
        else:
            print("En serio, Escoge una de las opciones plz. (-_- ')")
            zzz(2)
            sy("cls")
            main()

if __name__ == "__main__":
    main()