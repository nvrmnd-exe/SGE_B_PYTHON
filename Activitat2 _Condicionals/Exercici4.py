'''
En aquest exercici, s’aplicarà un IVA (0, 10, 21) segons el salari que s’indiqui.
Crear una variable de nom salari. Si el salari és menor de 15.000, s’aplica un 0% d’IVA. Si el salari és menor de 30.000 s’aplica un 10% de l’iva. Si el salari és menor a 60.000 s’aplica un IVA del 21%.
'''

#Demana el salari a l'usuari
salari = int(input("Indica el salari: "))

#Calcula l'IVA a aplicar i el mostra a pantalla

if salari < 15000:
    iva = salari * 0/100
elif salari < 30000:
    iva = salari * 10 / 100
elif salari < 60000:
    iva = salari * 21 / 100
    
print(f"L'IVA és {iva}")