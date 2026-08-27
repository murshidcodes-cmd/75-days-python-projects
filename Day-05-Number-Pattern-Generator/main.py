"""
DAY 5/75
NUMBER PATTERN GENERATOR
"""

print("1. Number Pattern")
print("2. Repeated Number Pattern")

choice = int(input("Choose pattern: "))
n = int(input("Enter number: "))

if choice == 1:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

elif choice == 2:
    for i in range(1, n + 1):
        print(str(i) * i)

else:
    print("Invalid choice!")
