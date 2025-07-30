# merge.py
import pandas as pd
from pathlib import Path

# 1) Paths
root    = Path(__file__).parent              # wherever merge.py lives
raw_dir = root / "data" / "raw"              # adjust if your CSVs are elsewhere
out_csv = raw_dir / "merged_data.csv"

# 2) Define tickers
tickers = ["AAPL", "GOOGL", "TSLA"]

frames = []
for t in tickers:
    file = raw_dir / f"{t}.csv"
    # 3) Read 'Price' as the date column
    df = pd.read_csv(file, parse_dates=["Price"])
    # 4) Rename it to "Date"
    df = df.rename(columns={"Price": "Date"})
    # 5) Tag the ticker
    df["Ticker"] = t
    # 6) Select & order the columns you want
    df = df[["Date", "Open", "High", "Low", "Close", "Volume", "Ticker"]]
    frames.append(df)

# 7) Concatenate vertically and sort
merged = pd.concat(frames, axis=0, ignore_index=True)
merged = merged.sort_values(["Date", "Ticker"]).reset_index(drop=True)

# 8) Write out your clean panel
merged.to_csv(out_csv, index=False)
print(f"Wrote merged_data.csv ({merged.shape[0]} rows) to {out_csv}")
