print(list(range(10)))
print(list(range(10, -10, -3)))
proverbe = ['La', 'raison', 'du', 'plus', 'fort', 'est', 'toujours', 'la', 'meilleure']
print(proverbe)
for elts in proverbe :
    print(elts, end=" ")
print("\n")

for nombre in range(10, 20, 2) :
    print(nombre, nombre**2, nombre**3)

fable = ['Maitre', 'corbeau', 'sur', 'un', 'arbre', 'perché']
for index in range (len(fable)) :
    print(index, fable[index])
    