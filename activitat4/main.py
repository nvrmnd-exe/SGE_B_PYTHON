#Importa les classes Cotxe i colibri
from Cotxe import Cotxe
from Colibri import Colibri

#Crea instàncies de Cotxe
cotxe1 = Cotxe("Toyota", "Corolla", 2022, "Blau", 25000)
cotxe2 = Cotxe("Ford", "Mustang", 2023, "Vermell", 45000)
cotxe3 = Cotxe("Tesla", "Model 3", 2024, "Blanc", 55000)

#Crea instàncies de Colibri
colibri1 = Colibri("Amazilia tzacatl", 5.2, 11, "Bosc tropical", 3)
colibri2 = Colibri("Lophornis ornatus", 2.8, 8, "Sabana", 2)
colibri3 = Colibri("Selasphorus platycercus", 3.5, 10, "Muntanya", 4)

#Mostra getters de Cotxe
print("Cotxe:")
print(f"Marca: {cotxe1.getmarca()}")
print(f"Model: {cotxe1.getmodel()}")
print(f"Any: {cotxe1.getanyModel()}")

#Mostra getters Colibrí
print("\nColibrí:")
print(f"Espècie: {colibri1.getespecie()}")
print(f"Pes: {colibri1.getpes()} g")
print(f"Envergadura: {colibri1.getenvergadura()} cm")
print(f"Hàbitat: {colibri1.gethabitat()}")

#Modifica atributs de cotxe
cotxe1.setcolor("Negre")
cotxe1.setpreu(48000)

#Mostra les modificacions de cotxe
print("\nAtributs modificats del Cotxe 1:")
print(f"Nou color: {cotxe1.getcolor()}")
print(f"Nou preu: {cotxe1.getpreu()}")

#Modifica atributs de colibrí
colibri1.setpes(3.7)
colibri1.sethabitat("Bosc de coníferes")

#Mostra les modificacions de colibri
print("\nAtributs modificats del Colibrí 1:")
print(f"Nou pes: {colibri1.getpes()}")
print(f"Nou habitat: {colibri1.gethabitat()}")