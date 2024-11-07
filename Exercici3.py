'''
En aquest exercici caldrà modificar la nota en número i mostrar-la en text. Es crearà una variable on es guardarà la nota numèrica i amb condicionals es mirarà la nota i segons la nota numèrica sortirà per pantalla la nota (S - suspès, A - aprovat, N - notable, E - excel·lent)
'''

#Demana la nota a l'usuari
nota = float(input("Introdueix una nota: "))

#Calcula el resultat d'aquesta nota
if nota < 5:
    print("S")
elif nota <= 6.5:
    print("A")
elif nota <= 8:
    print("N")
else:
    print("E")