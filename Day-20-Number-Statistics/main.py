"""
DAY 20/75
PYTHON PROJECT JOURNEY
"""

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

total = sum(numbers)
average = total / len(numbers)
largest = max(numbers)
smallest = min(numbers)

print("\n📊 NUMBER STATISTICS")
print(f"Largest:  {largest}")
print(f"Smallest: {smallest}")
print(f"Average:  {average:.2f}")
print(f"Total:    {total}")
