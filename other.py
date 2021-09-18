#Sonar

import random
import sys

def dibujarTablero(tablero):
    # Dibujar la estructura de datos del tablero.

    lineah = '   ' # espacio inicial para los numeros a lo largo del lado izquierdo del tablero
    for i in range (1,6):
        lineah += (' ' * 9) + str(i)
    
    # imprimir los numeros a lo largo del borde superior
    print(lineah)
    print('   ' + ('0123456789' * 6))
    print()

    # imprimir cada una de las 15 filas
    for i in range(15):
        #los numeros de una sola cifra deben ser precedidos por un espacio extra
        if i < 10:
            espacioExtra= ' '
        else:
            espacioExtra= ''
        print('%s%s %s %s' % (espacioExtra, i, obtenerFila(tablero, i), i))

    #imprimir los numeros a lo largo del borde inferior
    print()
    print('   ' + ('123456789'*6))
    print(lineah)


def obtenerFila(tablero, fila):
    #Crear una cadena con la estructura de datos de un tablero para una fila determinada.
    filaTablero= ''
    for x in range (60):
        filaTablero += tablero[x][fila]
    return filaTablero

def obtenerNuevoTsblero():
    #Crear una nueva estructura de datos para un tablero de 60x15.
    tablero =[]
    for x in range(60): #la lista principal es una lista de 60 listas
        tablero.append([])
        for y in range(15): # cada lista en la lista principal tiene 15 cadenas de un solo caracter
            # usar diferentes caracteres para el oceanopara hacerlo mas facil de leer.
            if random.randint(0, 1) == 0:
                tablero[x].append('~')
            else:
                tablero[x].append('`')
    return tablero
