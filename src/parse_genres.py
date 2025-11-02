#Optional script to parse genres to help verify which enres are most common after cleaning
import pandas as pd

f = "data/Netflix_clean.csv"
df = pd.read_csv(f)
# explode genres from 'listed_in'
genres = (df.assign(listed_in=df["listed_in"].fillna("Unknown"))
            .assign(listed_in=df["listed_in"].str.split(","))
            .explode("listed_in")
            .assign(genre=lambda d: d["listed_in"].str.strip()))
print(genres["genre"].value_counts().head(12))