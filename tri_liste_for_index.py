liste = [32, 5, 12, 8, 3, 75, 2, 15]

max = 0

for nombre in range(0, len(liste)) :
    print("nombre =", nombre)
    print("liste[nombre] =", liste[nombre])
    if liste[nombre] > max :
        max = liste[nombre]

print("le plus grand élément de cette liste est :", max)

pair = []
impair = []
for nombre in range(0, len(liste)) :
    if liste[nombre] % 2 == 0 :
        pair.append(liste[nombre])
    else :
        impair.append(liste[nombre])

print("voici la liste des nombres pairs :", pair)

print("voici la liste des nombres impairs :", impair)