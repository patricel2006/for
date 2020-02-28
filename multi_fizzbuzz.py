# programme qui doit placer le nom de chaque joueur devant chaque ligne du fizzbuzz :

# importation de toutes les fonctions du module random :

import random 

# annonce du titre de la partie :

print("Bienvenue dans notre jeu !\n")
print("\n#######################################################################\n")

# initialisation de la liste des prénoms des joueurs + taux de concentration :
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
liste_prenom = [("marc", 50) , ("alain", 80) , ("patrice", 60) , ("paul", 20)]

print("Voici la liste des participants :\n\n", liste_prenom)
print("\n#######################################################################\n")

max = input("Veuillez indiquer jusqu' à quel nombre voulez-vous compter : ")
print("\n\n####################################################################\n")
print("La partie peut commencer !\n")
print("Que le meilleur gagne !\n")
print("\n\n######################################################################\n")

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

# Initialisation de la variable IndexPrenom en dehors de la boucle for :
IndexPrenom = 0

# gestion de l'élimination des joueurs et des nouvelles parties :
while len(liste_prenom) > 1 :

# version de la boucle for avec un deuxieme index "IndexPrenom" incrémenté en fin de boucle :
    for index in range(1, int(max) + 1) :
# initialisation des variables prenom et taux de concentration :
        prenom = liste_prenom[IndexPrenom][0]
        taux_concentration = liste_prenom[IndexPrenom][1]
# tirage d'un nombre aléatoire entre un et 100 pour introduire une part de hasard dans la fiabilité de la 
# réponse donnée :
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
# Dans le cas d'une bonne réponse il faut passer au joueur suivant pour la 2ème itération :
            IndexPrenom += 1
            
        else :
# si le tirage est supérieur au taux de concentration du joueur, alors la réponse donnée est mauvaise
            print(prenom, alea, taux_concentration, "a donné une mauvaise réponse !\n")

# dans le cas où la réponse est mauvaise il faut supprimer le joueur :
            del liste_prenom[IndexPrenom]

# on vérifie que le joueur ayant donné une mauvaise réponse est supprimé du jeu :
            print("Le joueur ayant donné une mauvaise réponse vient d'être supprimé du jeu !\n \
            \n\n#############################################################################\n\n \
             Voici la liste des joueurs encore en lisse :\n\n", liste_prenom)
            print("\n\n############################################################################\n\n")
    
# On recommence le jeu à partir du premier joueur de la liste :
if IndexPrenom > 0 :
    IndexPrenom = 0
    
# vérification de quel joueur a la main :    
print("Recommençons à jouer avec :", liste_prenom[IndexPrenom], "\n")
print("\n\n####################################################################\n\n")

# retour en debut de liste lorsque les joueurs ont tous participé sans être éliminés et déclaration du vainqueur après \
# élimination de tous les joueurs jusqu'au dernier : 
if IndexPrenom > 3 :
    IndexPrenom = 0
if len(liste_prenom) == 1 :
    print("Le joueur", liste_prenom[IndexPrenom], "a gagné la partie !\n\n")
    print("#######################################################################\n\n")
    print("BRAVO !!! BRAVO !!! BRAVO !!!")
    print("\n\n###################################################################\n\n")
    rep = input("Voulez-vous recommencer à jouer ?\n\n Veuillez répondre par oui ou par non, merci : ")
    if rep == "oui" :
        break
        print("\n\nVoici une nouvelle partie !\n\n##############################################################\n\n")
        liste_prenom = [("marc", 50) , ("alain", 80) , ("patrice", 60) , ("paul", 20)]
    
    else :
        print("\n\nLa partie est terminée !\n\n A bientôt !\n")
        exit()

