max = input("Veuillez entrer la valeur jusqu'à laquelle le programme doit compter :")

for index in range(0, int(max) + 1):
    output = ""
    if(index % 3 == 0):
        output += "Fizz"
    if(index % 5 == 0):
        output += "Buzz"
    if(output == ""):
        output += str(index)
    print(output)