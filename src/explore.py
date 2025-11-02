"""explore.py — quick EDA helpers"""
import argparse
import pandas as pd

def describe_df(df: pd.DataFrame) -> dict:
    return {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "null_counts": df.isna().sum().sort_values(ascending=False).to_dict(),
        "types": df.dtypes.astype(str).to_dict(),
        "type_counts": df["type"].value_counts(dropna=False).to_dict() if "type" in df.columns else {},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    args = ap.parse_args()

    df = pd.read_csv(args.inp)
    summary = describe_df(df)
    print("Shape:", summary["shape"]) 
    print("Columns:", summary["columns"]) 
    print("Top nulls:", list(summary["null_counts"].items())[:10])
    print("Dtypes:", summary["types"]) 
    if summary["type_counts"]:
        print("Type counts:", summary["type_counts"]) 

if __name__ == "__main__":
    main()