liste = [32, 5, 12, 8, 3, 75, 2, 15]

print(liste)

###################################################################

##### version de travail sur les index ############################

for index in range(0, len(liste)) :
    if liste[index] % 2 == 0 :
        liste[index] = (liste[index])**2
     
print(liste)
print()

###################################################################

##### version de travail sur les valeurs et les index de la liste ##############


for index, nombre in enumerate(liste) :
    if nombre % 2 == 0 :
        nombre = nombre ** 2
        liste[index] = nombre
        print("index = " + str(index) + ", nombre = " + str(nombre))

print(liste)
print()

####################################################################

##### version de travail avec une nouvelle liste qui prend les modifications ####
update_liste = []

for nombre in liste :
    if nombre % 2 == 0 :
        nombre = nombre ** 2
        print(nombre)
    update_liste.append(nombre)
liste = update_liste
print(liste)
print()