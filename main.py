from collections import Counter

with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

words = text.split()
counter = Counter(words)

top_5 = counter.most_common(5)

print("Eng ko‘p ishlatilgan 5 ta so‘z:")
for word, count in top_5:
    print(f"{word} -> {count} marta")
