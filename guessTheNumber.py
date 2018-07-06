## Guesing the name game

from random import randint

def guessTheNumber():
    while True:
        n = randint(1, 10)
        print("Guess the number from 1 to 10")
        i = int(input("> "))
        if i == n:
            print("Congratulations, you have won!")
            break
        else:
            print("I'm sorry but your guess was wrong.")
            print("Do you want to try again? ")
            p = input("> ")
            if p.lower() == "yes":
                pass
            else:
                print("Thank you for playing")
                break

guessTheNumber()
