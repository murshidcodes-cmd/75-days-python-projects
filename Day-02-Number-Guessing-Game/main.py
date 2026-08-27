"""
DAY 2/75
PYTHON PROJECT JOURNEY
"""

import random

secret_number = random.randint(1, 10)

guess = int(input("Guess a number (1-10): "))

if guess == secret_number:
    print("🎉 Correct! You guessed it!")
else:
    print(f"❌ Wrong! The number was {secret_number}.")
