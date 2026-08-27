"""
DAY 11/75
PYTHON PROJECT JOURNEY
"""

bill = float(input("Enter bill amount: ₹"))
people = int(input("Number of people: "))

tip = float(input("Tip percentage: "))

tip_amount = bill * tip / 100
total = bill + tip_amount
share = total / people

print("\n🧾 BILL SUMMARY")
print(f"Total: ₹{total:.2f}")
print(f"Each person pays: ₹{share:.2f}")
