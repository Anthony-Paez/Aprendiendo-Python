mensualprecio = 15000
trimestralprecio = 40000
anualprecio = 140000
nombre = input("Introduzca su nombre de usuario. "
               "\n")
contraseñauser = input("\nIntroduzca una contraseña."
                   "\n")
contraseñaconfirm = input("\nConfirme su contraseña."
                          "\n")
intentos = 0
while contraseñauser != contraseñaconfirm and intentos < 3:
    print("\nLas contraseñas no coinciden. Intente de nuevo"
          "\n")
    contraseñauser = input("Introduzca una contraseña."
                           "\n")
    contraseñaconfirm = input("\nConfirme su contraseña."
                              "\n")
    intentos = intentos + 1
if contraseñauser != contraseñaconfirm and intentos == 3:
    print("Demasiados intentos fallidos. Cerrando acceso.")
else:
    print("\nSeleccione su tipo de plan:")
    planes = ("\nMensual", "\nTrimestral", "\nAnual")
    for plan in planes:
        print(plan)
    planusuario = input("\n").lower()
    while planusuario not in ("mensual", "trimestral", "anual"):
        planusuario = input("\nIngrese un dato válido.\n").lower()
    if planusuario == "mensual":
            edadvalida = False
            while edadvalida == False:
                try:
                 edad = int(input("\nIngrese su edad: "))
                 edadvalida = True

                except:
                 print("Ingrese un dato válido.")
            if edad < 18:
                print("\nNecesitas autorización de un mayor de edad para acceder.\n")
                    
            elif edad >= 18 and edad < 60:
                print("\nEl precio del plan mensual es de " + str(mensualprecio) + " pesos.")
                    
            elif edad >= 60:
                preciofinal = int(mensualprecio*0.8)
                print("\nEl precio del plan mensual es de " + str(preciofinal) + " pesos (Descuento Senior aplicado).")
                    
    elif planusuario == "trimestral":
            edadvalida = False
            while edadvalida == False:
                try:
                    edad = int(input("\nIngrese su edad: "))
                    edadvalida = True
                except:
                    print("Ingrese un dato válido.")
            if edad < 18:
                print("\nNecesitas autorización de un mayor de edad para acceder.\n")
                    
            elif edad >= 18 and edad < 60:
                print("\nEl precio del plan trimestral es de " + str(trimestralprecio) + " pesos.")
                    
            elif edad >= 60:
                preciofinal = int(trimestralprecio*0.8)
                print("\nEl precio del plan trimestral es de " + str(preciofinal) + " pesos (Descuento Senior aplicado).")
                    


    elif planusuario == "anual":
        edadvalida = False
        while edadvalida == False:

            try:
                edad = int(input("\nIngrese su edad: "))
                edadvalida = True
            except:
                print("Ingrese un dato válido.")
        if edad < 18:
            print("\nNecesitas autorización de un mayor de edad para acceder.\n")
        elif edad >= 18 and edad < 60:
            print("\nEl precio del plan anual es de " + str(anualprecio) + " pesos.")
        elif edad >= 60:
            preciofinal = int(anualprecio*0.8)
            print("\nEl precio del plan anual es de " + str(preciofinal) + " pesos (Descuento Senior aplicado).")


