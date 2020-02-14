def compte_mots(chaine) :
    if len(chaine) == 0 :
        return 0

    nb_mots = 1
    for mot in chaine :
        if mot == " " :
            nb_mots = nb_mots + 1
    return nb_mots

chaine = "je sens le vent tourner."
print(compte_mots(chaine))