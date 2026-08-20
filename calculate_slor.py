import pandas as pd

df = pd.read_csv("bnc_scores.csv")

df["bigram_slor"] = (
    df["bigram_logprob"] -
    df["unigram_logprob"]
)

df["trigram_slor"] = (
    df["trigram_logprob"] -
    df["unigram_logprob"]
)

df.to_csv("bnc_scores.csv", index=False)

print(df.head())
