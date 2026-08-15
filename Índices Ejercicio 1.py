#Aquí estoy mezclando el recorrido de índices con valores negativos y positivos.
Lista = ["Eiden", "Billy", "Anby", "Nicole", "Nekomata", "Wise", "Belle", "Hada"]
print("\n" + str(Lista[2:-2]))
print("\n" + str(Lista[-5:7]))

#Aquí voy a practicar el comando insert
Lista = ["Eiden", "Billy", "Anby", "Nicole", "Nekomata", "Wise", "Belle", "Hada"]
Lista.insert(5, "Piper")
print("\n" + str(Lista[4:7]))

#Practica del comando sort. En teoría me va a dejar todo en orden alfabético.
Lista.sort()
print("\n" + str(Lista))