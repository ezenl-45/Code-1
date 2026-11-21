#########################################Variables 
PIN = 0
intentos = 3
acceso = True
menu   = True
bienvenida = True
saldo    = 0
ingDinero= 0
extDinero= 0
opciones = ""
movimientos = True
registroMov = ""
############################### Inicio del Programa solo se muestra al inicio: 
print ("=========================================")
print ("==                                     ==")
print ("==          CAJERO AUTOMATICO          ==")
print ("==                                     ==")
print ("=========================================")
print ("")
print ("")
print ("======== INGRESAR PIN DE ACCESO ========")
##################################### PIN de acceso, Una vez ingresado el correcto sale del while de acceso y va a bienvenida. 

while acceso:
        print ("")
        PIN = input("PIN de acceso: ")
        print ("")
        if (PIN > "9643" or PIN < "9643") :
                if(intentos <= 1 ):
                         print ("ACCESO RECHAZADO!,Ha superado el limite de intentos.")
                         print ("Su tarjeta queda retenida, Por favor comuniquese con su banco")
                         acceso = False
                         menu = False
                         bienvenida = False 
                         break
        elif (PIN == "9643"):
                print ("")
                print ("PIN Correcto.")
                print ("")
                acceso = False
                break
        
        intentos = intentos - 1
        print ("Pin Incorrecto, Ingrese nuevamente.")
        print ("Intentos restantes",intentos)



###################################### Bienvenida solo se muestra 1 vez y sale a while Menu.            
while bienvenida :
    print ("==========================================")
    print ("Bievenido al sistema de Cajero Automatico.")
    print ("")
    break


##################################### Menu repetitivo. Se muestra hasta que el usuario finalice el pograma  
while menu:
        print 
        print ("============================")
        print ("===== Menú de Opciones =====")
        print ("============================")
        print ("")
        print ("1. Consultar Saldo\n2. Ingresar Dinero\n3. Extracción de dinero\n4. Consulta de movimientos\n5. Salir")
        print ("=========================================")
        opciones = input("Ingrese una opción: ")
        if (opciones == "1"):
                        print ("")
                        print ("=====       SALDO  DISPONIBLE    =====")
                        print ("")
                        print ("Su Saldo es $",saldo)
                        print ("=========================================")
                        input ("Presione Enter para continuar....")
                        print ("")
        elif (opciones == "2"):
                        print ("")
                        print("=====       INGRESO DE DINERO       =====")
                        print ("")
                        ingDinero = int(input("Ingrese el montó de Dinero: "))
                        if (ingDinero >= 1):
                                saldo = saldo + ingDinero
                                registroMov = registroMov + "\nIngDinero : $" + str (ingDinero) + "            " + "Saldo: $" + str (saldo)
                                print ("")
                                print ("====  MONTO INGRESADO CORRECTAMENTE  ====")
                                print ("")
                        elif (ingDinero <= 0):
                                print ("INGRESAR UN MONTO VALIDO, VUELVA A INTENTARLO!.")
                                print ("")
                        input ("Presione Enter para continuar....")
                        print ("=========================================")
                        print ("")
        elif (opciones == "3"):
                        print ("")
                        print ("=====       EXTRACCIÓN DE DINERO       =====")
                        print ("")
                        extDinero= int(input("Ingrese el montó que desea extraer: "))
                        if   (extDinero >= 1 and extDinero <= saldo):
                                saldo = saldo - extDinero
                                registroMov = registroMov + "\nExtracción: $-" + str (extDinero) + "           " + "Saldo: $" + str (saldo)
                                print ("")
                                print ("==========MONTÓ EXTRAIDO CORRECTAMENTE.==========")
                                print ("")
                        elif (extDinero > saldo):
                                        print ("")
                                        print ("SALDO INSUFICIENTE, VUELVA A INTENTARLO!.")
                                        print ("")
                        elif (extDinero <= 0):
                                print ("")
                                print ("INGRESE UNA EXTRACCIÓN VALIDA.")
                                print ("")
                        input ("Presione Enter para continuar....")
                        print ("=========================================")
                        print ("")
                        
        elif (opciones == "4"): 
                        if (saldo >= 1): 
                                        print ("")
                                        print ("===== MOVIMIENTOS REALIZADOS =====")
                                        print ("")
                                        print (registroMov)
                                        print ("")
                                        print ("=========================================")
                        else :
                                print ("")
                                print ("========= No hay movimientos disponibles! =========")
                                print ("")
                        input ("Presione Enter para continuar....")
                        print ("=========================================")
                        print ("")
        elif (opciones == "5"):
                print ("")
                print("YA PUEDE RETIRAR SU TARJETA. GRACIAS POR ELEGIRNOS!\nHASTA LA PROXIMA!")
                menu = False
                break
                
        elif (opciones >= "1" or opciones <= "5"):
                        print ("")
                        print ("Opción incorrecta, Intenta nuevamente.")
                        print ("")


     
        
