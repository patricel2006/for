def est_une_maj(car) :
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if car in maj :
        return True
    else :
        return False

car = "B"
print(est_une_maj(car))