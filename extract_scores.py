import re
import pandas as pd


def extract_scores(filename, expected_count):
    scores = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            match = re.search(r"logprob=\s*([-0-9.]+)", line)

            if match:
                scores.append(float(match.group(1)))

    # Keep only scores corresponding to the sentences in bnc.csv
    return scores[:expected_count]


df = pd.read_csv("bnc.csv")

expected_count = len(df)

unigram = extract_scores("unigram_scores.txt", expected_count)
bigram = extract_scores("bigram_scores.txt", expected_count)
trigram = extract_scores("trigram_scores.txt", expected_count)

print("BNC sentences:", len(df))
print("Unigram scores:", len(unigram))
print("Bigram scores:", len(bigram))
print("Trigram scores:", len(trigram))

if not (
    len(unigram) == expected_count
    and len(bigram) == expected_count
    and len(trigram) == expected_count
):
    raise ValueError("Number of scores does not match number of BNC sentences.")

df["unigram_logprob"] = unigram
df["bigram_logprob"] = bigram
df["trigram_logprob"] = trigram

df.to_csv("bnc_scores.csv", index=False)

print("\nSaved bnc_scores.csv")
print()
print(df[
    [
        "text",
        "mean_rating",
        "unigram_logprob",
        "bigram_logprob",
        "trigram_logprob"
    ]
].head())