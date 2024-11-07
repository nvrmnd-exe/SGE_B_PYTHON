'''
Crear un arxiu nou per a que retorni per pantalla la resposta adeqüada. Crear 1 variable per dia de la setmana. Exemple: dia_setmana = “dilluns”
'''

#Demana el dia a l'usuari
dia_setmana = input("Introdueix quin dia és [Dilluns - Dimarts - ...]: ")

#Mostra a pantalla quin dia és
if dia_setmana == "Dilluns":
    print("Avui és dilluns")
elif dia_setmana == "Dimarts":
    print("Avui és dimarts")
elif dia_setmana == "Dimecres":
    print("Avui és dimecres")
elif dia_setmana == "Dijous":
    print("Avui és dijous")
elif dia_setmana == "Divendres":
    print("Avui és divendres")
elif dia_setmana == "Dissabte":
    print("Avui és dissabte")
elif dia_setmana == "Diumenge":
    print("Avui és diumenge")
else:
    print("Dia no vàlid.")