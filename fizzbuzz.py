print("voici le jeu fizzbuzz !")

prenom = input(print("hello, veuillez entrer votre prénom :"))

print("hello", prenom, "!")

max = input(print("Veuillez entrer la valeur jusqu'à laquelle le programme doit compter :"))

liste = []

for index in range(1, int(max)):
    
    liste.append(index)
    print(index)

for index, nombre in enumerate(liste) :
    if nombre % 3 == 0 and nombre % 5 == 0 :
        nombre = "FizzBuzz"
        liste[index] = nombre
    elif nombre % 3 == 0 :
        nombre = "Fizz"
        liste[index] = nombre
    elif nombre % 5 == 0 :
        nombre = "Buzz"
        liste[index] = nombre
    else :
        print(nombre)
    
print(liste)