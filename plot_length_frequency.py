import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("word_statistics.csv")

plt.scatter(df["length"], df["frequency"], alpha=0.3)

plt.xlabel("Word Length")
plt.ylabel("Frequency")
plt.title("Word Length vs Frequency")

plt.savefig("length_frequency.png", dpi=300)
plt.show()
