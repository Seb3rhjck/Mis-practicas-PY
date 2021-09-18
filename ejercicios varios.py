#Ejercicios practica
from os import system as S
from time import sleep as ZZ
import  json
import os


Track = []

def guardado_texto():
    print("wait")

def texto_varios():
    print("wait")

def  busqueda():
    print("wait")

def  guardado():
    musica1 = input("Ahora ingresa el tema musical")


def musica(musica, genero, artista):
    print("- - - -INICIEMOS CON INGRESAR UNOS DATOS- - - -")
    print("- o - 0 - o -" *15)
    musica = input("Ingresa tu tema : ")
    Track.append(musica)
    ZZ(3)
    S("cls")
    opcion1 =input("Si sabes el genero del tema ingresa C, si no ingrsa N: ")
    C = True
    N = False
    if opcion1 is C:
        genero = input("Ingrese el genero del tema: ")
        Track.append(genero)
    ZZ(3)
    S("cls")    
    opcion2 = input("Si sabe el nombre del artista oprime C si no N")
    if opcion2 is C:
        artista = input("Ingrese el nombre del artista o el grupo olo que sea")
        Track.append(artista)
    texto_varios()
    
    
    
    print("OKAY, datos guardados.")
    print(" -o - 0 - o -" * 15)

    input("Genial, es hora de volver. Oprime ENTER")


def menu():
    print("Saludos bienvenidos a este programa")
    print(" \ o / " * 15)
    print(" - - - " * 15)
    print("ºoºoºoº" * 15)
    print("HORA DE MUSICA")
    print(" \ o / " * 15)
    print(" - - - " * 15)
    print("ºoºoºoº" * 15)

    print("Veamos ahora las opciones")

    print("[G]uardar tema musical")
    print("[B]uscar tema musical")
    print("[S]alida")


def main():
    print("wait")

if __name__ == "__main__":
    main()
