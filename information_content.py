import pandas as pd
import numpy as np

df = pd.read_csv("word_statistics.csv")

total = df["frequency"].sum()

df["probability"] = df["frequency"] / total

df["information_content"] = -np.log2(df["probability"])

df.to_csv("word_statistics.csv", index=False)

print(df.head())
