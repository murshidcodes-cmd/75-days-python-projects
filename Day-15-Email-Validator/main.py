"""
DAY 15/75
PYTHON PROJECT JOURNEY
"""

email = input("Enter your email: ")

if (
    "@" in email
    and "." in email
    and email.count("@") == 1
    and not email.startswith("@")
    and not email.endswith(".")
):
    print("\n✅ Valid Email")
else:
    print("\n❌ Invalid Email")
