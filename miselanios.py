vacio = "-"
objeto = "#"
zona = []

for i in range(10):
    fila =[vacio for i in range(10)]
    zona.append(fila)

zona[0][0] = objeto
zona[0][4] = objeto
zona[0][9] = objeto
zona[4][0] = objeto
zona[9][0] = objeto
zona[4][9] = objeto
zona[9][9] = objeto

print(zona)