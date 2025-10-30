# notebooks/demo_analysis.py
"""
Demo analysis: load data and show simple stats.
Run: python notebooks/demo_analysis.py
"""
import pandas as pd
df = pd.read_csv('../data/sample_dirty.csv')
df.columns = [c.strip().lower() for c in df.columns]
df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0)
print("Summary:")
print(df.describe(include='all'))
