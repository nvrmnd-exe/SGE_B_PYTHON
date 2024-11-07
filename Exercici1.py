'''
Crear dues variables i comparar-les indicant quina és més gran, quina és més petita o si son iguals.
'''

#Demana els dos números a l'usuari
var1 = int(input("Indica un número: "))
var2 = int(input("Indica un altre número: "))

#Calcula si el número és major, menor o igual
if var1 == var2:
    print(f"{var1} és igual que {var2}")
elif var1 > var2:
    print(f"{var1} és més gran que {var2}")
else:
    print(f"{var1} és més petit que {var2}")