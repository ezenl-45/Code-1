ingredientes = ["Harina", "Huevos", "Leche", "Azúcar"]
stock = [3000, 24, 2000, 1000]
receta = [300, 3, 200, 100]
unidades = ["g", "unidades", "ml", "g"]
menu = True
print ("=======================================================")
print ("             Bievenido a Panaderias William            ")
print ("=======================================================")
    
while menu:
    print ("=======================================================")
    print ("                        MENU                 ")
    print ("")
    print ("1. Mostrar stock")
    print ("2. Cargar stock")
    print ("3. Calcular cantidad máxima de tortas")
    print ("4. Registrar pedido de tortas")
    print ("")
    print ("5. Salir")
    print ("")
    opcion = input("Ingrese una opcion: ")
    print ("")
    print ("=======================================================")

    if opcion == "1":
        print ("                 STOCK DISPONIBLE                   ")
        print ("")
        for i in range (len(ingredientes)):
            print (ingredientes [i],":", stock [i] , unidades[i])
    elif opcion == "2":
        for g in range (len(ingredientes)):
            print (g + 1,"-", ingredientes [g])
        nroIng = input("Seleccione ingrediente:")
        if nroIng == "1":
            agreHa = input("Cantidad a agregar:")
            if agreHa < "0":
                print ("La cantidad no puede ser negativa.")
            else:
                agreHa  = int ( agreHa)
                stock[0] = stock[0] + agreHa
                print ("Stock actualizado correctamente.")
        elif nroIng == "2":
            agreHu = input("Cantidad a agregar:")
            if agreHu < "0":
                print ("La cantidad no puede ser negativa.")
            else:
                agreHu  = int (agreHu)
                stock[1] = stock[1] + agreHu
                print ("Stock actualizado correctamente.")
        elif nroIng == "3":
            agreLe = input("Cantidad a agregar:")
            if agreLe < "0":
                print ("La cantidad no puede ser negativa.")
            else:
                agreLe = int (agreLe)
                stock[2] = stock[2] + agreLe
                print ("Stock actualizado correctamente.")
        elif nroIng == "4":
            agreAz = input("Cantidad a agregar:")
            if agreAz < "0":
                print ("La cantidad no puede ser negativa.")
            else:
                agreAz = int (agreAz)
                stock[3] = stock[3] + agreAz
                print ("Stock actualizado correctamente.")
        elif nroIng <= "0" : 
            print ("Valor negativo, vuelva a intentarlo.")
        else:
             print ("Valor nulo, Ingrese algo valido.")
             
    elif opcion == "3":
        stockDisp = 10000         
        for k in range (len(stock)):  
            totalTor = stock[k] // receta[k]
            if totalTor < stockDisp:
                stockDisp = totalTor
        print ("Se pueden elaborar", stockDisp,"tortas")

    elif opcion == "4":
        cantTor = int (input("Ingrese la cantidad de tortas: "))
        stockDisp = 10000
        for g in range (len(stock)): 
            totalTor = stock[g] // receta[g]
            if totalTor < stockDisp:
                stockDisp = totalTor
        if cantTor <= stockDisp:
            for j in range(len(stock)):
                stock[j] = stock[j] - receta[j] * cantTor
            print ("Pedido cargado con exito.")
        else:
            print ("No hay suficiente stock.")
            
    else:
         print ("Gracias por elegirnos! Vuelva pronto.")
         break







 
