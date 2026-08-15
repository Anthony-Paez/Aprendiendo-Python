personajes = ["EIDEN"]
liebres = ("NICOLE", "ANBY", "BILLY", "NEKOMATA")
print("Elige a dos agentes para añadir a tu equipo:")
for agente in liebres:
    print("\n" + agente.title())
liebrespj = []
for agente in liebres:
    liebrespj.append(agente.upper())
elección = input("\n").upper()
miembros = 0
while elección not in liebrespj and miembros < 2:
    print("\nDebo elegir a un agente.")
    elección = input("\n").upper()
personajes.append(elección)
liebrespj.remove(elección)
miembros = miembros + 1
print("\nAhora otro...")
elección = input("\n").upper()
while elección not in liebrespj:
    print("\nDebo elegir a otro.")
    elección = input("\n").upper()
personajes.append(elección)
liebrespj.remove(elección)
miembros = miembros + 1
print("\n¿Estoy seguro de que quiero que este sea mi equipo?")
for personaje in personajes:
 print("\n" + personaje.title())
print("\nSí/No")
elección = input("\n").lower()
if elección == "si":
    print("\n" + personajes[1].title() + ", " + personajes[2].title() + ", confío en ustedes para salir airosos de esta misión.")