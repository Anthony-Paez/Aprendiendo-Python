membresias = ("\nBásica", "\nPremium")
print("Seleccione tipo de membresía.")
for membresia in membresias:
    print(membresia)
membresia = input("\n")
while membresia not in ("básica", "basica", "premium"):
    print("\nIngrese un dato valido.")
    membresia = input("\n")
if membresia in ("basica", "básica"):
        print("\nDisfrute de nuestros servicios limitados.")
elif membresia == "premium":
    edadvalida = 18
    edad = 0
    while edad < edadvalida:
                try:
                    edad = int(input("\nIngrese su edad: "))
                    if edad < edadvalida:
                        print("\nNo puedes acceder siendo menor.")
                    else:
                            print("\nDisfrute nuestros servicios exclusivos.")
                            break
                except:
                    print("\nIngrese un dato valido.")