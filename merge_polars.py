import polars as pl
from pathlib import Path

root = Path(__file__).parent
raw_dir = root / "data" / "raw"
out_file = raw_dir / "merged_data.parquet"

csv_files = sorted(raw_dir.glob("*.csv"))
frames = []
for csv_file in csv_files:
    if csv_file.name == "merged_data.csv":
        continue
    ticker = csv_file.stem
    df = pl.read_csv(csv_file, try_parse_dates=True)
    if "Price" in df.columns:
        df = df.rename({"Price": "Date"})
    df = df.with_columns(
        pl.lit(ticker).alias("Ticker")
    )
    df = df.select(["Date", "Open", "High", "Low", "Close", "Volume", "Ticker"])
    frames.append(df)

merged = pl.concat(frames).sort(["Date", "Ticker"])
merged.write_parquet(out_file)
print(f"Wrote {len(merged)} rows to {out_file}")
