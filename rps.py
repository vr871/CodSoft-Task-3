import random

while True:
    choice1 = input("Enter a choice:\n-----------------\nrock \npaper \nscissors\n-----------------\n=> ")
    actions = ["rock", "paper", "scissors"]
    choice2 = random.choice(actions)
    print(f"\nYou chose {choice1}, computer chose {choice2}.\n")


    if choice1 == choice2:
        print(f"Both players selected {choice1}. It's a tie!")
    elif choice1 == "rock":
        if actions == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif choice1 == "paper":
        if choice2 == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif choice1 == "scissors":
        if choice2 == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


    again = input("Play again? (y/n): \n-----------------\n")
    if again.lower() != "y":
        break