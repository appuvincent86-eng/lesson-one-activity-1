import random

turn = input("Enter your choice (rock, paper, scissors): ").lower()

computer_number = random.randint(1, 3)
if computer_number == 1:
    computer_action = "rock"
elif computer_number == 2:
    computer_action = "paper"
else:
    computer_action = "scissors"

print(f"Computer chose {computer_action}.")

if turn == computer_action:
    print("It's a tie!")
elif turn == "rock":
    if computer_action == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif turn == "paper":
    if computer_action == "rock":
        print("You win!")
    else:
        print("You lose!")
elif turn == "scissors":
    if computer_action == "paper":
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid choice. Please enter rock, paper, or scissors.")
