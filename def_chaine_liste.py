def chaine_liste(chaine) :
    "fonction qui converti une phrase en une liste de mots"
    if len(chaine) == 0 :
        return 0

    liste_mot = []
    chaine_prov = ""
    for car in chaine :
        if car == " ":
            liste_mot.append(chaine_prov)
            chaine_prov = ""
        else :
            chaine_prov = chaine_prov + car

    if chaine_prov :
        liste_mot.append(chaine_prov)
    return liste_mot
    

# programme principal 

chaine = "voici la liste des courses."
print(chaine_liste(chaine))
print(chaine_liste(chaine[5:]))

