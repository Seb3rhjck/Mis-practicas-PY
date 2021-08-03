#calculo de factura

listadofactura = []

print("-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-")

while (True):
    try:
        cantFact = int(input("Ingrese el numero de facturas : "))
        break    
    except:
        print("En serio -_- , por favor ingrese un numero") 

print("-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-")

numeroFacturas = 1 

while (True):
    try:
        facturacion = [] 
        subtotal = int(input("Por favor ingrese el subtotal de la factura " +  str(numeroFacturas ) + " :"))
        iva = int(input("Por favor ingrese el IVA de la factura " + str(numeroFacturas ) + " :"))
        retefuente = subtotal * 3.5 / 10
        reteica = subtotal * 5 / 1000
        reteiva = iva * 15 / 100

        
        print("Valor retefuente " + str(numeroFacturas ) + " $ : " + str(retefuente) )
        print("Valor reteica " + str(numeroFacturas ) + " $ : " + str(reteica) )
        print("Valor rete iva " + str(numeroFacturas) + " $ : " + str(reteiva))
        
        print("-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-")

        facturacion.append(numeroFacturas)
        facturacion.append(retefuente)
        facturacion.append(reteica)
        facturacion.append(reteiva)

        listadofactura.append(facturacion)

        if(numeroFacturas == cantFact):
            break
        numeroFacturas += 1
    
    except:
        print("En serio -_- , por favor ingrese un numero")
        pass
print("-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-")
print(listadofactura)

totalsumatoria = []

for x in range(len(listadofactura[0])):
    sumatoria = sum([listadofactura[x] for listadofactura in listadofactura])
    totalsumatoria.append(sumatoria)

print("El valor total de la retefuente es : $ ", totalsumatoria[1])
print("El valor total del reteica : $ ", totalsumatoria[2])
print("El valor total del reteiva es : $ ", totalsumatoria[3])

print("-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-")
print("Gracias por usarme XD")