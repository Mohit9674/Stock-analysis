
# Stock Analysis Project

This repository demonstrates a complete workflow for collecting stock market data, generating technical indicators and building forecasting models using Prophet and FinBERT sentiment features. All code is provided as Jupyter notebooks so you can reproduce the results on your own machine.

## Repository Layout

- **data/**
  - **raw/** – individual CSV files for each ticker and the merged dataset.
  - **processed/** – feature engineering outputs produced by the notebooks.
- **merge.py** – merge multiple ticker CSVs into one consolidated file using pandas.
- **merge_polars.py** – alternative merge implementation using polars that outputs Parquet.
- **notebooks/** – seven notebooks that should be run in order:
  1. `01_data_ingest.ipynb` – download historical prices with `yfinance`.
  2. `02_EDA.ipynb` – exploratory analysis and volatility modelling.
  3. `03_Stationarity_and_Differencing.ipynb` – stationarity checks and differencing.
  4. `04_prophet_baseline_updated.ipynb` – initial Prophet model.
  5. `05_fetch_sentiments.ipynb` – download news via Polygon.io (requires API key).
  6. `06_Finbert.ipynb` – score news headlines with FinBERT.
  7. `07_prophet_final.ipynb` – final forecasting model with sentiment features.

## Requirements

Python 3.9 or newer is recommended. Install all dependencies with:
=======
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


Some packages (e.g. Prophet) may need build tools on your system. On Linux, make sure `gcc` and `g++` are available.

## Quickstart

1. **Clone the repository**


2. **Create a virtual environment** (optional but recommended)

3. **Install Python packages**


4. **Launch JupyterLab**


5. **Run the notebooks** in the `notebooks/` folder sequentially. The first notebook downloads data to `data/raw/`.

   - To fetch news with `05_fetch_sentiments.ipynb`, set your Polygon API key inside the notebook or export it as an environment variable named `POLYGON_API_KEY`.

## Merging Data

If you already have individual CSVs for each ticker, you can merge them without running the first notebook:



The merged file will be stored in `data/raw/`.

## Reproducibility

All notebooks were executed with the packages listed in `requirements.txt`. The `data/` directory already contains example outputs so you can inspect the results without re-running the full pipeline.
=======
3. Launch JupyterLab to run the notebooks:



## Merging CSV Data

Place individual ticker CSV files under `data/raw/`. Run either of the merge
scripts to combine them:



The merged dataset will be written back to `data/raw/`.

