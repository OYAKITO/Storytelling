"""
ROCK, PAPER, SCISSORS PROGRAM

This Python program will simulate playing the classic game Rock, Paper, Scissors against the computer. The program will ask the user how many rounds of the game they would like to play, simulate each round, keep score, and determine an overall winner. The program will also print the classic phrases such as "Paper covers rock" or "Scissors cut paper".
"""

import random

print("Rock, Paper, Scissors Program")

import random

# Prompt user for the number of rounds
rounds = int(input("Enter the number of rounds you want to play: "))

# Initialize scores
user_score = 0
computer_score = 0

# Define game choices
choices = ["Rock", "Paper", "Scissors"]

# Simulate each round
for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}")

    # Prompt user for their choice
    user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

    # Generate computer's choice
    computer_choice = random.choice(choices)

    # Determine the winner of the round and print classic phrases
    if user_choice == computer_choice:
        result = "It's a tie!"
        phrase = "No one wins."
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"
        phrase = f"{user_choice} covers {computer_choice}."
        user_score += 1
    else:
        result = "Computer wins!"
        phrase = f"{computer_choice} covers {user_choice}."
        computer_score += 1

    # Print choices, result, and classic phrases
    print(f"You chose {user_choice}. Computer chose {computer_choice}. {result}")
    print(phrase)

# Determine the overall winner
if user_score > computer_score:
    print("\nYou are the overall winner!")
elif user_score < computer_score:
    print("\nComputer is the overall winner!")
else:
    print("\nIt's a tie in the overall score!")

# Display final scores
print(f"\nYour Score: {user_score}")
print(f"Computer's Score: {computer_score}")
