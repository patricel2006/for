max = input("Veuillez entrer la valeur jusqu'à laquelle le programme doit compter :")

index = 0

while (index < int(max)) :
    if index % 5 == 0 and index % 3 == 0 :
        print("FizzBuzz")
    if index % 3 == 0 :
        print("Fizz")
    if index % 5 == 0 :
        print("Buzz")
    #if index % 5 != 0 and index % 3 != 0 :
    index = index + 1