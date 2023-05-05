import random

num = random.randrange(1,50)
count = 1
try:
    gus = int(input("Guess a number between 1 to 50 : "))
    while gus != num :
        if gus > num :
            print("Guess lower than "+str(gus))
            gus = int(input("Guess a number between 1 to 50 : "))
            count += 1
        else:
            print("Guess higher than "+str(gus))
            gus = int(input("Guess a number between 1 to 50 : "))
            count += 1

    print("You guessed the number correctly ! \n")
    print("You tried "+str(count)+" times !!! ")

except ValueError:
    print("Please enter number !!!")

