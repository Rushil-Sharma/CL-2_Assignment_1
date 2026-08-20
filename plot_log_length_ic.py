import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("word_statistics.csv")

plt.scatter(
    np.log10(df["length"]),
    df["information_content"],
    alpha=0.3
)

plt.xlabel("log10(Word Length)")
plt.ylabel("Information Content")
plt.title("Log Word Length vs Information Content")

plt.savefig("log_length_information.png", dpi=300)
plt.show()
