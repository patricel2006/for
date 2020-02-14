# programme qui compte les mots d'une phrase :
phrase = "je suis tombé malade."
nb_mots = 1

for mot in phrase :
    if mot == ' ' :
        nb_mots = nb_mots + 1

print("Le nombre de mots de cette phrase est :", nb_mots)