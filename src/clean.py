"""
clean.py — Netflix dataset cleaning steps

What this script does:
1) Strip extra spaces from text columns
2) Convert ratings to uppercase
3) Convert date_added to datetime
4) Replace missing countries with 'Unknown'
5) Replace missing ratings with 'UNRATED'
6) Drop rows missing essential values (title or type)
"""
# I’m converting ratings to uppercase to make categories consistent for grouping
# I'm also dropping rows with missing titles or type to ensure we don’t plot invalid entries.

from typing import List
import argparse
from pathlib import Path
import pandas as pd


def strip_whitespace(df: pd.DataFrame, text_cols: List[str]) -> pd.DataFrame:
    """Strip leading/trailing spaces for specified text columns without turning NaN into strings."""
    df = df.copy()
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)
    return df


def clean_dataset(input_csv: str) -> pd.DataFrame:
    df = pd.read_csv(input_csv)

    # 1) Strip extra spaces from text columns
    possible_text_cols = [
        "title", "director", "cast", "country", "listed_in",
        "description", "rating", "type"
    ]
    text_cols = [c for c in possible_text_cols if c in df.columns]
    df = strip_whitespace(df, text_cols)

    # 2) Convert ratings to uppercase (preserving NaN)
    if "rating" in df.columns:
        df["rating"] = df["rating"].astype("string").str.upper()

    # 3) Convert date_added to datetime (invalids become NaT)
    if "date_added" in df.columns:
        df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

    # 4) Replace missing countries with 'Unknown' (treat empty strings as missing too)
    if "country" in df.columns:
        df["country"] = df["country"].where(
            df["country"].notna() & (df["country"].astype(str).str.strip() != ""),
            "Unknown"
        )

    # 5) Replace missing ratings with 'UNRATED'
    if "rating" in df.columns:
        df["rating"] = df["rating"].where(
            df["rating"].notna() & (df["rating"].astype(str).str.strip() != ""),
            "UNRATED"
        )

    # 6) Drop rows missing essential values (title or type)
    essentials = [c for c in ["title", "type"] if c in df.columns]
    if essentials:
        before = len(df)
        df = df.dropna(subset=essentials)
        after = len(df)
        print(f"Dropped {before - after} rows due to missing essentials: {essentials}")

    return df


def main():
    parser = argparse.ArgumentParser(description="Clean Netflix dataset.")
    parser.add_argument("--in", dest="inp", required=True, help="Path to input CSV (e.g., data/Netflix_shows_movies.csv)")
    parser.add_argument("--out", dest="out", required=True, help="Path to save cleaned CSV (e.g., data/Netflix_clean.csv)")
    args = parser.parse_args()

    cleaned = clean_dataset(args.inp)

    # Quick sanity outputs
    print("Shape after cleaning:", cleaned.shape)
    if "type" in cleaned.columns:
        print("Type counts:\n", cleaned["type"].value_counts(dropna=False))
    if "rating" in cleaned.columns:
        print("Top ratings:\n", cleaned["rating"].value_counts().head(10))


    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    cleaned.to_csv(args.out, index=False)
    print(f"Saved cleaned file to: {args.out}")


if __name__ == "__main__":
    main()