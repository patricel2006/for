max = input("Veuillez entrer la valeur jusqu'à laquelle le programme doit compter :")

index = 0

while (index < int(max)) :
    if index % 5 == 0 and index % 3 == 0 :
        print("FizzBuzz")
    elif index % 3 == 0 :
        print("Fizz")
    elif index % 5 == 0 :
        print("Buzz")
    else :
        print(index)
    index = index + 1