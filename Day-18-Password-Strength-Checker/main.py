"""
DAY 18/75
PYTHON PROJECT JOURNEY
"""

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.islower() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(c in "!@#$%^&*" for c in password):
    score += 1

print("\n🔐 PASSWORD STRENGTH")

if score <= 2:
    print("❌ Weak")
elif score <= 4:
    print("⚠️ Medium")
else:
    print("✅ Strong")

print(f"📊 Score: {score}/5")
