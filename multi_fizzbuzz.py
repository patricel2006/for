# programme qui doit placer le nom de chaque joueur devant chaque ligne du fizzbuzz :

#nb_joueurs = int(input("combien de joueurs êtes vous ? "))

# importation de toutes les fonctions du module random :

import random
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
liste_prenom = [("marc", 50) , ("alain", 80) , ("patrice", 60) , ("paul", 20)]

# constitution de la liste des prenoms :
#for prénom in range(1, nb_joueurs + 1) :
#    prénom = input("veuillez appuyer sur entrer après chaque prénom, en commençant par le prénom du premier joueur :")
#    liste_prenom.append(prénom)

print("voici la liste des participants :", liste_prenom)

max = input("veuillez indiquer jusqu' à quel nombre voulez-vous compter : ")

# version de la boucle for utilisant le modulo :

#for index in range(1, int(max) + 1) :
#    if index % 15 == 0 :
#        print(liste_prenom[(index - 1) % 4], "a dit :" + "FizzBuzz")
#    elif index % 3 == 0 :
#        print(liste_prenom[(index - 1) % 4], "a dit :" + "Fizz")
#    elif index % 5 == 0 :
#        print(liste_prenom[(index - 1) % 4], "a dit :" + "Buzz")
#    else :
#        print(liste_prenom[(index - 1) % 4], "a dit :", index)

IndexPrenom = 0
prenom = liste_prenom[IndexPrenom][0]
taux_concentration = liste_prenom[IndexPrenom][1]



# version de la boucle for avec un deuxieme index "IndexPrenom" incrémenté en fin de boucle :
for index in range(1, int(max) + 1) :
    # tirage d'un nombre aléatoire entre un et 100
    alea = random.randint(1, 100)

    # comparaison entre tirage et taux de concentration :
    if alea <= taux_concentration : 
        # la réponse donnée est la bonne réponse :
        if index % 15 == 0 :
            print(prenom, alea, taux_concentration, "a dit : " + "FizzBuzz")
        elif index % 3 == 0 : 
            print(prenom, alea, taux_concentration, "a dit : " + "Fizz")
        elif index % 5 == 0 : 
            print(prenom, alea, taux_concentration, "a dit : " + "Buzz")
        else :
            print(prenom, alea, taux_concentration, "a dit :", index)

    else :
        # la réponse donnée est mauvaise
         print(prenom, alea, taux_concentration, "a donné une mauvaise réponse !")
         # del liste_prenom[IndexPrenom][0]
         IndexPrenom = 0
         #len(liste_prenom) = len(liste_prenom) - 1

        
# incrémentation de l'index de la liste des prénoms et remise à zéro au-delà de trois :
    
    IndexPrenom += 1
    if IndexPrenom > 3 :
        IndexPrenom = 0
