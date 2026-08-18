#Bueno, es hora de practicar con los diccionarios. A ver como me va.
Pj_Jugables = {"Eiden":{"Nombre Completo": "Eiden Demara", "Facción": "Liebres Astutas", "Rol": "Atacante", "Elemento": "Étereo"},
               "Billy":{"Facción": "Liebres Astutas", "Rol": "Atacante", "Elemento": "Físico"},
               "Anby":{"Facción": "Liebres Astutas", "Rol": "Aturdidor", "Elemento": "Eléctrico"}}
#Aquí voy a aplicar el diccionario de características de los personajes.
#Como se ve, terminé anidando varios datos en un mismo diccionario, por lo que si
#quiero pedir la data de un personaje en específico, tiene que ser en dos corchetes distintos.
#Uno que abra la entrada del personaje, y otro que abra la stat solicitada.
#Tengo que tener en cuenta igual que de esta forma solo me va a tirar el nombre de los valores del diccionario elegido,
#no los valores en sí. Para eso hay que ver el ejercicio después de este.
for cosa in Pj_Jugables["Eiden"]:
    print(Pj_Jugables["Eiden"][cosa])
#Ahora, si lo que quiero es recorrer el diccionario entero junto con el nombre y los valores almacenados, se hace así.
for personaje, values in Pj_Jugables.items():
    print("\n" + personaje + ": ")
#Aquí se crea otro bucle con for para recorrer el valor almacenado dentro del diccionario de cada variable.
#Algo como buscar carpetas dentro de una subcarpeta.
    for stat, valor in values.items():
        print("\n" + stat + ": " + valor)
#Si lo que necesito es algo más simple, como solo mostrar el valor de una variable del diccionario pero sin el nombre, hago esto
print(Pj_Jugables["Eiden"]["Facción"])