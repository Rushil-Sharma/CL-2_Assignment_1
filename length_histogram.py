import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("word_statistics.csv")

counts = df["length"].value_counts().sort_index()

plt.bar(counts.index, counts.values)

plt.xlabel("Word Length")
plt.ylabel("Number of Words")
plt.title("Distribution of Word Lengths")

plt.savefig("word_length_histogram.png", dpi=300)
plt.show()
