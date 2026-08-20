import re
import pandas as pd

def extract_scores(filename):
    scores = []

    with open(filename, "r") as f:
        for line in f:
            if "logprob=" in line:
                match = re.search(r"logprob=([-0-9.]+)", line)
                if match:
                    scores.append(float(match.group(1)))

    return scores


df = pd.read_csv("bnc.csv")

df["unigram_logprob"] = extract_scores("unigram_scores.txt")
df["bigram_logprob"] = extract_scores("bigram_scores.txt")
df["trigram_logprob"] = extract_scores("trigram_scores.txt")

print(df[[
    "text",
    "mean_rating",
    "unigram_logprob",
    "bigram_logprob",
    "trigram_logprob"
]].head())

df.to_csv("bnc_scores.csv", index=False)