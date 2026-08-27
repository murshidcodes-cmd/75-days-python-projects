"""
DAY 3/75
PYTHON PROJECT JOURNEY
"""

import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for _ in range(length):
    password += random.choice(characters)

print(f"Generated Password: {password}")
