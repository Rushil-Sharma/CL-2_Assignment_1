import re
import pandas as pd
from collections import Counter

with open("combined.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

# Extract alphabetic words only
words = re.findall(r"[a-z]+", text)

freq = Counter(words)

data = []

for word, count in freq.items():

    length = len(word)

    data.append({
        "word": word,
        "frequency": count,
        "length": length
    })

df = pd.DataFrame(data)

df.to_csv("word_statistics.csv", index=False)

print(df.head())
print("\nNumber of unique words:", len(df))
print("\nShortest words:")
print(df.sort_values("length").head(20))
