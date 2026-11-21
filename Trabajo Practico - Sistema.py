capacidades = [120, 30, 200, 80, 50]
pedidos = [
    "Pepita - Otamendi 123",
    "Juan   - Balcarce 432",
    "Mirtha - Perón 443",
    "Carlos - San Martín 900",
    "Laura  - Mitre 120",
    "Pedro  - Rivadavia 1500",
    "Ana    - Belgrano 321",
    "Luis   - Moreno 654",
    "Sofía  - Independencia 789",
    "Martín - Callao 111"
]
pesos = [10, 20, 50, 15, 30, 80, 40, 25, 60, 35]
despachados = [False, False, False, False, False, False, False, False, False, False]
menu = True
opcion = "0"
print ("")
print ("--------------------------------------------------------------")
print ("--   BIEVENIDO AL SISTEMA DE CARGAS DE VEHICULOS PESADOS   ---")
print ("--------------------------------------------------------------")
print ("")
while menu:
        print ("")
        print ("--------------------------------------------------------------")
        print ("---             SISTEMA DE GESTIÓN DE PEDIDOS              ---")
        print ("--------------------------------------------------------------")
        print ("")
        print ("------------------------------------------------------")
        print ("1. Agregar vehiculo")
        print ("2. Mostrar vehiculos")
        print ("3. Vehiculo con menor capacidad")
        print ("4. Vehiculo con mayor capacidad")
        print ("5. Dar de baja un vehiculo")
        print ("")
        print ("6. Agregar pedido")
        print ("7. Mostrar pedidos pendientes")
        print ("8. Promedio de peso de pedidos")
        print ("9. Cantidad de pedidos pendientes")
        print ("")
        print ("10. Armar despacho")
        print ("")
        print ("0. Salir")
        print ("")
        print ("------------------------------------------------------")
        print ("")

                         ## Parte 1 – Gestión de vehículos 

        opcion = input ("----. Ingresé una opción: ")
        if opcion == "1":
            print ("------------------------------------------------------")
            print ("---------------    AGREGAR   VEHICULO   --------------")
            print ("")
            capaNew = int(input("----. Agregue un vehiculo: "))                                                        
            if capaNew >= 1 :
                    capacidades.append(capaNew)                                                 ##Añade al list capacidades
                    print ("")
                    print ("---. Vehiculo ingresado correctamente.")
                    print ("")
                    input ("---. Presione enter para continuar........")
                    print ("------------------------------------------------------")
            else:
                                                                                                ##Validacion  menor a 0
                    print ("Valor invalido, Ingrese de nuevo.")
                    print ("")
                    print ("------------------------------------------------------")        
        elif opcion == "2":
            print ("------------------------------------------------------")
            print ("----.         Vehiculos Cargados       .----")
            print ("")
            for i in range (len(capacidades)):
                print ("El vehículo Nro",i + 1 ," tiene un peso de", capacidades [i],"KG")                      ##Muestra indice del vehiculo y peso
            print ("")    
            input ("---. Presione enter para continuar........")                                           
            print ("------------------------------------------------------")
        elif opcion == "3":
                cargaMin = 1000000
                for j in range (len(capacidades)):
                        if capacidades[j] < cargaMin:                                           ##Saca el minimo tanto de su Kg y su indice
                            cargaMin = capacidades[j]
                            indiceMin = j 
                print ("------------------------------------------------------")
                print ("---. El vehiculo con menor capacidad es el Nro", indiceMin + 1 ,"con" ,cargaMin, "KG") 
                print ("")
                input ("---. Presione enter para continuar........")                                           
                print ("------------------------------------------------------")
        elif opcion == "4":
                cargaMax = -1
                for g in range (len(capacidades)):
                        if capacidades[g] > cargaMax:                                            ##Saca el Maximo tanto de su kg y su indice
                            cargaMax = capacidades[g]
                            indiceMax= g                                        
                print ("------------------------------------------------------")
                print ("El vehiculo con mayor capacidad es el Nro", indiceMax + 1,"con", cargaMax,"KG")
                print ("")
        elif opcion == "5":
                print ("")
                print ("----. VEHICULOS DISPONIBLES .----")
                print ("")
                for h in range (len(capacidades)):
                        print ("Nro:", h + 1 ,"Con",capacidades [h] ,"KG")
                print ("")
                eliminar =(input ("Ingrese el Nro del vehiculo que desea eliminar: "))
                if eliminar >= "1":
                        eliminar = int (eliminar)
                        capacidades.pop(eliminar - 1)                                           ##Elimina el vehiculo por indice restando - 1 a su valor  
                        print ("")   
                        print ("----. Vehiculo eliminado correctamente. ")
                        print ("") 
                        input ("---. Presione enter para continuar........")                                           
                        print ("------------------------------------------------------")
                elif eliminar == "":
                        print ("Valor nulo, vuelva a intentarlo.")
                else:
                        print ("")
                        print ("----. Ingrese un numero de vehiculo valido.")


                                        ## Parte 2 – Gestión de pedidos   

        elif opcion == "6":
                agrePedidos = input ("----. Ingresé nombre completo (Cliente - Calle y Altura) del pedido :")
                pedidos.append(agrePedidos)
                while True:
                        agrePesos = int(input ("----. Ingresé el peso del pedido:"))       ## Se repite hasta que ingrese un numero valido.
                        if agrePesos >= 1 :                                                ## Solo se agrega a pesos si es valido el numero ingresado. de otra manera no lo hace y se repite.
                                pesos.append(agrePesos)
                                break 
                        elif agrePesos <= 0 :
                                print ("----. El valor no puede ser negativo")
                        else:
                                print("----. El valor no puede ser nulo.")

                agreDesp    = input ("----. Ingresé estado de despacho del pedido False o True:")
                despachados.append(agreDesp)
        
               

        elif opcion == "7":
                print ("-----------------------         PEDIDOS PENDIENTES          ------------------------------------")
                print ("")
                for k in range (len(pesos)):
                        print ("Pedido Nro",k + 1 ,pedidos [k],"\tPeso:", pesos [k] ,"\tDespacho:", despachados [k])
                print ("")
                input ("Presione enter para continuar........")
                print ("-----------------------------------------------------------")
        elif opcion == "8":
                print ("-----------------------         PROMEDIO DE PEDIDOS          ------------------------------------")
                print ("")
                suma = 0
                for l in range (len(pesos)):                             
                        suma = suma + pesos [l]                                           ## Realiza la suma acumulando los datos y se le suma + 1 al for para que sea el numero real de los numeros
                l = l + 1  
                promedio = suma / l                                                       ## Se realiza el promedio
                print ("El promedio de los pesos registrados es: ", promedio)
        elif opcion == "9":
                print ("-----------------------         CANTIDAD DE PEDIDOS PENDIENTES         ------------------------------------")
                print ("")
                for z in range (len(pedidos)):                                          ##muestra los pedidos pendientes
                        print (pedidos[z])                              
                print ("La cantidad de pedidos pendientes es:", z + 1)                  ##muestra el indice ya que es el total que hay en el vector de pedidos y + 1 porque arranca del 0
                print ("")
                input ("---. Presione enter para continuar........")                                           
                print ("------------------------------------------------------")       

                                        #Parte 3 - Armado de despacho
        elif opcion == "10":
                pesoTo = 0
                DespGrl= []
                pedidoElegido = []
                eliminar = []
                print ("======= Vehiculos disponibles =======")
                for i in range(len(capacidades)):
                    print ("Nro",i + 1 ,"capacidad", capacidades[i],"KG")
                vehiEle = int(input("Elija el Nro del vehiculo que quiere utilizar: "))
                if vehiEle  >= 1:
                        print ("=========================================================================================")
                        print ("====================           DESPACHO GENERADO               ==========================")
                        print ("=========================================================================================")
                        print ("Vehículo seleccionado:",vehiEle)                        ## Aca muestro el numero del input ingresado
                        indiceVehi = vehiEle - 1                                        ##guardo el indice antes de modificar su valor.
                        vehiEle = capacidades[vehiEle - 1]                                 ## Actualizo la variable con la capacidad y el indice ingresado 
                        print ("Capacidad del vehiculo:",vehiEle)                          ## Utilizo la misma variable ya actualizada con el valor del vehiculo en KG
                        print ("")
                        print ("Detalle de la carga:")
                        print ("")
                        for z in range(len(pedidos)):
                            if vehiEle >= pesos[z] and despachados[z] == False:          ##compara y verifica que el despacho este en false asi no saca un pedido ya hecho.
                                pedidoElegido.append (pedidos [z])
                                DespGrl.append(pesos[z])
                                vehiEle -= pesos[z]
                                pesoTo+= pesos[z]
                                despachados[z] = True                                   ##aca ya lo marca como True 
                        for u in range (len(pedidoElegido)):
                           print(u + 1,"-",pedidoElegido [u],"-", DespGrl[u], "KG")
                        print ("")
                        print ("Peso total:", pesoTo,"KG")        
                        print ("Peso libre:", vehiEle,"KG")
                        print ("")
                        input ("---. Presione enter para continuar........")                                           
                        print ("------------------------------------------------------")
                        capacidades.pop(indiceVehi)                                   ##elimina el vehiculo por ultimo.
                else:
                        print ("")
                        print ("Ingrese un numero valido, Pruebe mas tarde.")
                        print ("")
                        input ("---. Presione enter para continuar........")                                           
                        print ("------------------------------------------------------")
        else:
                print ("=========================================================================================")
                print ("") 
                print ("") 
                print ("Gracias por utilizar nuestro programa, Espero volver a verte pronto!.")
                print ("=========================================================================================")
                break 
