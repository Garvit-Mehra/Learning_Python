import random
import sys

# User sets upper and lower bound
while True:
    try:
        while True:
            lowerLimit = int(input("Enter lower limit: "))
            upperLimit = int(input("Enter upper limit: "))
            if upperLimit > lowerLimit :
                break
            else:
                print('Upper limit has to be greater than lower limit')
    except ValueError:
        print("Kindly enter a number")
    else:
        break

# Assign number to be guessed
magicNumber = random.randint(lowerLimit, upperLimit)

# User tries to guess
while True:
    try:
        while True:
            guess = int(input(f"Enter your guess ({lowerLimit} to {upperLimit}): "))
            if guess>upperLimit or lowerLimit>guess:
                print(f"Guess has to lie between {lowerLimit} and {upperLimit}")
            else:
                if magicNumber == guess:
                    sys.exit(f"Congratulations! You got it correct\nThe number was {magicNumber}")
                elif magicNumber > guess:
                    print("You guessed too low!")
                elif magicNumber < guess:
                    print("You guessed too high!")
    except ValueError:
        print("Kndly enter a number")
    else:
        break