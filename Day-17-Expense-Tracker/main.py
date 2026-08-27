"""
DAY 17/75
PYTHON PROJECT JOURNEY
"""

expenses = []

while True:
    print("\n💰 EXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("\nChoose: ")

    if choice == "1":
        name = input("Expense: ")
        amount = float(input("Amount: ₹"))

        expenses.append((name, amount))
        print("✅ Expense added!")

    elif choice == "2":
        total = 0

        print("\n📊 EXPENSES")

        for name, amount in expenses:
            print(f"{name}: ₹{amount:.2f}")
            total += amount

        print(f"\nTotal: ₹{total:.2f}")

    elif choice == "3":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice!")
