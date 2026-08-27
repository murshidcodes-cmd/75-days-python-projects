"""
DAY 9/75
PYTHON PROJECT JOURNEY
"""

import time

seconds = int(input("Enter seconds: "))

while seconds > 0:
    mins, secs = divmod(seconds, 60)

    print(f"\r⏳ {mins:02d}:{secs:02d}", end="")
    time.sleep(1)

    seconds -= 1

print("\n🚀 Time's up!")
