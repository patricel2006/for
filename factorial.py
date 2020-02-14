number = int(input("Enter a number: "))

factorial = 1

if number < 0 :
    print("sorry, this number is negative !")
elif number == 0 :
    print("factorial of 0 is 1.")
else :
    for index in range(1, number + 1) :
        factorial = factorial * index
    print("factorial of", number, "is :", factorial )



