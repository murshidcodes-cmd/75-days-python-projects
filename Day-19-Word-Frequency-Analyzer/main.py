"""
DAY 19/75
PYTHON PROJECT JOURNEY
"""

from collections import Counter
import re

text = input("Enter your text: ")

words = re.findall(r"\b\w+\b", text.lower())
frequency = Counter(words)

print("\n📊 WORD FREQUENCY")

for word, count in frequency.most_common(5):
    print(f"{word:<12} → {count}")
