num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
parells = 0
imparells = 0

for i in num:
    if i % 2 == 0:
        parells = parells + i
    else:
        imparells = imparells + i

print(f"Suma de tots els parells: {parells}")
print(f"Suma de tots els imparells: {imparells}")