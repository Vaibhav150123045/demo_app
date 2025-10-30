# src/demo_app.py
import pandas as pd
import sys
from pathlib import Path

def clean_data(df):
    # simple cleaning example: strip whitespace, lowercase column names
    df.columns = [c.strip().lower() for c in df.columns]
    if 'amount' in df.columns:
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0)
    return df

def main(path='data/sample_dirty.csv'):
    f = Path(path)
    if not f.exists():
        print(f"No data at {path}", file=sys.stderr)
        return 2
    df = pd.read_csv(f)
    df = clean_data(df)
    print("Rows:", len(df))
    print(df.head().to_string(index=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
