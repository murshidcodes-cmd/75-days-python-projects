"""
DAY 4/75
ROCK PAPER SCISSORS
"""

import random

choices = ["rock", "paper", "scissors"]

player = input("Your choice: ").lower()
computer = random.choice(choices)

print(f"Computer: {computer}")

if player == computer:
    print("It's a tie! 🤝")
elif (player, computer) in [
    ("rock", "scissors"),
    ("paper", "rock"),
    ("scissors", "paper")
]:
    print("You win! 🎉")
else:
    print("Computer wins! 🤖")
