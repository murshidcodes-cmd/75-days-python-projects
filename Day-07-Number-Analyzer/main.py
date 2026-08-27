"""
DAY 7/75
PYTHON PROJECT JOURNEY
"""

n = int(input("Enter a number: "))

print("\nNumber:", n)

# Even / Odd
print("Type:", "Even" if n % 2 == 0 else "Odd")

# Positive / Negative
print("Sign:", "Positive" if n > 0 else "Negative")

# Prime check
if n < 2:
    prime = False
else:
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break

print("Prime:", "Yes ✅" if prime else "No ❌")
