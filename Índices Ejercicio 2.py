#En este ejercicio debo combinar el slicing, insert, y sort
Lista = ["Eiden", "Billy", "Anby", "Nicole", "Nekomata", "Wise", "Belle", "Hada"]
print("Bueno, es hora de tomar poner esto en práctica. Primero, debo pensar en Rina"
      "\nsi quiero agregarla a mi catalogo mental.")
Añadir = input("\nSolo debo pensar en Rina, y con eso bastará..."
               "\n"
               "\n").title()
#Este while no necesita de un if. Debo recordar que ya funciona solo hasta que se cumpla su condición
while Añadir != "Rina":
    Añadir = input("\nNo debo distraerme con tonterías. Piensa en Rina, Eiden...\n").title()
#Acá debo usar el insert, append no me sirve porque lo que hace es añadir el elemento al final de la lista.
Lista.insert(3, Añadir)
print("\nBien, ahora he de repasar bien a quién tengo en mis índices mentales. Aquí vamos...\n")
print(Lista[-4:])
print("\nEspera, creo que eso no está bien. Quiero mucho a los chicos, pero he de hacerle espacio a Rina también."
      "\nIntentemos eso de nuevo.\n")
Lista.sort()
print(Lista[2:6])
print("\nUgh, sigue sin estar bien. Además de que no debería contarme a mí mismo."
      "\nA ver, repasemos de vuelta mi lista...\n")
#Aquí removí a Rina para poder volver a imprimir a lista organizada pero sin ella.
Lista.remove("Rina")
print(Lista)
print("\nBien, vamos de vuelta con añadir a Rina. Hagamos algo más chico, como empezar por Nekomata hasta Wise...\n")
#Aquí la vuelvo a insertar, esta vez en dónde originalmente habría estado si hubiera sido organizada.
Lista.insert(6, "Rina")
print(Lista[5:])
print("\nOle los caracoles, ahí tenemos a Rina. Je, este pequeño ejercicio mental me ha servido para"
      "organizarme mejor.")