liste = [32, 5, 12, 8, 3, 75, 2, 15]

max = 0

for nombre in liste :
    print("nombre =", nombre)
    #print("liste[nombre] =", liste[nombre])
    if nombre > max :
        max = nombre

print("le plus grand élément de cette liste est :", max)

pair = []
impair = []
for nombre in liste :
    if nombre % 2 == 0 :
        pair.append(nombre)
    else :
        impair.append(nombre)

print("voici la liste des nombres pairs :", pair)

print("voici la liste des nombres impairs :", impair)