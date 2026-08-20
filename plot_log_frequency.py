import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("word_statistics.csv")

plt.scatter(
    np.log10(df["length"]),
    np.log10(df["frequency"]),
    alpha=0.3
)

plt.xlabel("log10(Word Length)")
plt.ylabel("log10(Frequency)")
plt.title("Log Word Length vs Log Frequency")

plt.savefig("log_length_frequency.png", dpi=300)
plt.show()
