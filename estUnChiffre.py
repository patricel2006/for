def estUnChiffre(car) :
    "renvoie vrai si le caractere est un chiffre"
    if car in "0123456789" :
        return "vrai"
    else :
        return "faux"

# corps du programme :

if __name__ == '__main__' :
    caracteres = "d75è8b0à1"
    print("caractères à tester :", caracteres)
    for car in caracteres :
        print(car, estUnChiffre(car))

        