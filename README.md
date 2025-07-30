# Stock Analysis

This repository contains utilities and Jupyter notebooks for downloading,
processing and analyzing stock market data. The notebooks walk through a
workflow that fetches historical prices, explores stationarity of features,
builds forecasting models with Prophet and gathers sentiment information.

## Project Structure

- `data/` – raw and processed CSV/Parquet files.
- `merge.py` – merge raw CSV data into a single file using pandas.
- `merge_polars.py` – merge raw CSV data using Polars.
- `notebooks/` – analysis notebooks in sequential order:
  1. **01_data_ingest.ipynb** – download historical prices with `yfinance`.
  2. **02_EDA.ipynb** – exploratory data analysis of the prices.
  3. **03_Stationarity_and_Differencing.ipynb** – checks stationarity and applies differencing.
  4. **04_prophet_baseline_updated.ipynb** – baseline Prophet forecasting model.
  5. **05_fetch_sentiments.ipynb** – fetch news sentiment data.
  6. **06_Finbert.ipynb** – apply FinBERT for text sentiment analysis.
  7. **07_prophet_final.ipynb** – final Prophet model with extra features.

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Launch JupyterLab to run the notebooks:

```bash
jupyter lab
```

## Merging CSV Data

Place individual ticker CSV files under `data/raw/`. Run either of the merge
scripts to combine them:

```bash
python merge.py        # pandas implementation
python merge_polars.py # polars implementation producing Parquet
```

The merged dataset will be written back to `data/raw/`.
