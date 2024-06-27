import random
import sys
print ("Here are the rules:\n1) Rock breaks Scissors\n2) Scissor cuts paper\n3) Paper covers Rock")
while True:
    cont = input("Do you wish to begin the game(Y/N): ").title()
    if cont == "Y":
        break
    elif cont == "N":
        print("Goodbye!")
        sys.exit(0)
while True:
    print ("Enter a number to choose your option:\n1 = Rock\n2 = Paper\n3 = Scissor")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                choice_name = "Rock"
                break
            elif choice == 2:
                choice_name = "Paper"
                break
            elif choice == 3:
                choice_name = "Scissor"
                break
            elif choice != 1 or choice != 2 or choice != 3:
                print("Enter a valid choice")
        except ValueError:
            print ("Enter a valid choice")
    print(f"You have chosen {choice_name}")

    comp_choice = random.randint(1,3)

    if choice == 1 and comp_choice == 2:
        print("The computer chose paper\nYou lost!")
    elif choice == 1 and comp_choice == 3:
        print("The computer chose scissor\nYou Win!")
    elif choice == 1 and comp_choice == 1:
        print("THe computer chose rock\nIt's a draw!")
    elif choice == 2 and comp_choice == 2:
        print("The computer chose paper\nIt's a draw!")
    elif choice == 2 and comp_choice == 3:
        print("The computer chose scissor\nYou lost!")
    elif choice == 2 and comp_choice == 1:
        print("THe computer chose rock\nYou Win!")
    elif choice == 3 and comp_choice == 2:
        print("The computer chose paper\nYou Win!")
    elif choice == 3 and comp_choice == 3:
        print("The computer chose scissor\nIts a draw!")
    elif choice == 3 and comp_choice == 1:
        print("THe computer chose rock\nYou lost!")
    while True:
        cont = input("Do you wish to continue(Y/N): ").title()
        if cont == "Y":
            break
        elif cont == "N":
            print("Goodbye!")
            sys.exit(0)