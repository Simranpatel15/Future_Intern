#task 3
import random

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")

while True:
    # Player's choice
    player = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()

    if player == "quit":
        print("Thanks for playing!")
        break

    if player not in choices:
        print("Invalid choice! Try again.")
        continue

    # Computer's choice
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    # Determine winner
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("You win!")
    else:
        print(" Computer wins!")

    print("-" * 30)
