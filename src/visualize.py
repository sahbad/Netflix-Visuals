"""visualize.py — plotting functions for Netflix visuals (Python)"""
# Using horizontal bars since genre names are long and easier to read sideways thereby preventing overlapping and making the chart cleaner.
import argparse
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_context("talk")


def plot_top_genres(df: pd.DataFrame, top_n: int = 10, outdir: Path | None = None):
    # Prepare exploded genres
    genres = (df.assign(listed_in=df["listed_in"].fillna("Unknown"))
                .assign(listed_in=df["listed_in"].str.split(","))
                .explode("listed_in")
                .assign(genre=lambda d: d["listed_in"].str.strip()))

    counts = (genres["genre"].value_counts().head(top_n)
                                .reset_index())
    counts.columns = ["genre", "count"]

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=counts, x="count", y="genre", ax=ax)
    ax.set_title(f"Top {top_n} Genres (Catalog Prevalence as Watch Proxy)")
    ax.set_xlabel("Number of Titles")
    ax.set_ylabel("Genre")
    plt.tight_layout()

    if outdir:
        outdir.mkdir(parents=True, exist_ok=True)
        p = outdir / "top_genres.png"
        fig.savefig(p, dpi=150)
        print(f"Saved {p}")
    return fig


def plot_rating_distribution(df: pd.DataFrame, outdir: Path | None = None):
    counts = (df["rating"].value_counts().reset_index())
    counts.columns = ["rating", "count"]

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=counts, x="rating", y="count", ax=ax)
    ax.set_title("Ratings Distribution")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Number of Titles")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    if outdir:
        outdir.mkdir(parents=True, exist_ok=True)
        p = outdir / "rating_distribution.png"
        fig.savefig(p, dpi=150)
        print(f"Saved {p}")
    return fig


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--outfig", dest="outfig", default="outputs")
    ap.add_argument("--topn", dest="topn", type=int, default=10)
    args = ap.parse_args()

    df = pd.read_csv(args.inp)
    outdir = Path(args.outfig)

    plot_top_genres(df, top_n=args.topn, outdir=outdir)
    plot_rating_distribution(df, outdir=outdir)

if __name__ == "__main__":
    main()