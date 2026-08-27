"""
DAY 8/75
PYTHON PROJECT JOURNEY
"""

import random

name = input("Enter your name: ").lower()
number = random.randint(10, 99)

styles = [
    name + str(number),
    name + "_dev" + str(number),
    "its_" + name,
    name + "_x"
]

print("\n✨ USERNAME GENERATOR")

for i, username in enumerate(styles, 1):
    print(f"{i}. @{username}")
