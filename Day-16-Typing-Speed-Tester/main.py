"""
DAY 16/75
PYTHON PROJECT JOURNEY
"""

import time

print("⌨️ TYPING SPEED TEST\n")

input("Press Enter to start...")

start = time.time()

text = input("\nType anything: ")

end = time.time()

time_taken = end - start

words = len(text.split())

wpm = (words / time_taken) * 60

accuracy = 100

print("\n📊 RESULT")

print(f"⏱️ Time: {time_taken:.2f}s")
print(f"⚡ Speed: {wpm:.0f} WPM")
print(f"🎯 Accuracy: {accuracy:.0f}%")
