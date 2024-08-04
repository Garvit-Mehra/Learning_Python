import random
import sys
from termcolor import cprint


def rules():
    cprint("\t\tHANGMAN", attrs=["bold"], color="blue")
    cprint(
        "Rules: \n1. Choose the amount of guesses you requires ranging from 1 to 11.\n2. Enter any letter "
        "into the input space.\n3. If the letter is part of the word the blank spaces will be filled\n4. If the "
        "letter is not part of the word, one try shall be deducted.\n5.The game ends if either your tries are over "
        "or the word I guessed correctly.\n6. Remember to have fun!\n",
        color="blue",
    )


def get_word(doc):
    i = random.randint(0, 839)
    with open(f"{doc}", "r") as file:
        lines = file.readlines()
        return lines[i].rstrip()


def tries():
    while True:
        try:
            i = int(input("Enter number of tries you would like: "))
            if i >= 12:
                print("Too many tries requested!")
                pass
            elif 1 <= i <= 11:
                break
        except ValueError:
            pass
    return i


def get_input():
    while True:
        try:
            letter = input("Enter letter: ")
            if len(list(letter)) == 1 and letter.isalpha():
                break
        except ValueError:
            pass
    return letter


def game():
    word = list(get_word("words.csv").rstrip())
    answer = "".join(word)
    tri = tries()
    guesses = []

    for i in range(len(word)):
        guesses.append("_")

    while True:
        print(f"\nYou have {tri} tries left")
        print(" ".join(guesses))
        letter = get_input()

        if letter in word:
            for x in range(len(list(answer))):
                if list(answer)[x] == letter:
                    guesses[x] = letter
                else:
                    pass
            word.remove(letter)

        if tri != 0 and "".join(guesses) == answer:
            print("\n" + f"{' '.join(list(answer))}")
            cprint("You Win!", "green")
            sys.exit(0)
        elif tri == 0:
            cprint(f"The word was {answer}\nYou Lose!", "red")
            sys.exit(0)
        if letter not in list(answer):
            tri -= 1
            if tri == 0:
                cprint(f"\nThe word was {answer}\nYou Lose!", "red")
                sys.exit(0)


def main():
    rules()
    game()


if __name__ == "__main__":
    main()
