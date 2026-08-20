import pandas as pd
from scipy.stats import spearmanr

df = pd.read_csv("bnc_scores.csv")

# Calculate average per-word log probability
df["unigram_avg_logprob"] = df["unigram_logprob"] / df["length"]
df["bigram_avg_logprob"] = df["bigram_logprob"] / df["length"]
df["trigram_avg_logprob"] = df["trigram_logprob"] / df["length"]

# Calculate SLOR
df["bigram_slor"] = (
    df["bigram_logprob"] - df["unigram_logprob"]
)

df["trigram_slor"] = (
    df["trigram_logprob"] - df["unigram_logprob"]
)

# Save all calculated scores
df.to_csv("bnc_scores.csv", index=False)


# Calculate Spearman correlations
rating = df["mean_rating"]

scores = {
    "Unigram Log Probability": df["unigram_logprob"],
    "Bigram Log Probability": df["bigram_logprob"],
    "Trigram Log Probability": df["trigram_logprob"],

    "Unigram Average Log Probability": df["unigram_avg_logprob"],
    "Bigram Average Log Probability": df["bigram_avg_logprob"],
    "Trigram Average Log Probability": df["trigram_avg_logprob"],

    "Bigram SLOR": df["bigram_slor"],
    "Trigram SLOR": df["trigram_slor"],
}


print("\n===== SPEARMAN CORRELATIONS =====\n")

for name, score in scores.items():

    valid = score.notna() & rating.notna()

    rho, p = spearmanr(
        score[valid],
        rating[valid]
    )

    print(f"{name}")
    print(f"  Spearman rho = {rho:.4f}")
    print(f"  p-value      = {p:.6g}")
    print()