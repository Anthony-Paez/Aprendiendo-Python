npc_equipo = ["Eiden"]
npcs = ("Nicole","Anby", "Billy")
print("¿Quien debería acompañarme?")
for personaje in npcs:
    print("\n" + personaje)
npcjugable = []
for personaje in npcs:
    npcjugable.append(personaje.lower())
elección = input("\n").lower()
while elección not in npcjugable:
    print("\nSería estúpido no ir con nadie a la cavidad. Tengo que elegir...")
    elección = input("\n").lower()
if elección == "nicole":
    npc_equipo.append("Nicole")
    print("\nSupongo que para una misión como esta conviene ir con mi nueva jefa. Así al menos veré si es de fíar...")
elif elección == "anby":
    npc_equipo.append("Anby")
    print("\nBueno, Anby no es mala opción. No habla mucho, pero al menos sabré que no va a dejar que me rebanen por la mitad. Creo.")
elif elección == "billy":
    npc_equipo.append("Billy")
    print("\nSi lo elijo a él corro el riesgo de que se distraiga jugando a ser el heroe y nos maten a ambos. Pero hey, al menos entretiene.")