# Spark Stock Analytics Pipeline

A PySpark pipeline that processes stock market data and generates 
analytics summaries using distributed computing.

## What it does

Reads 6 months of stock price data for AAPL, MSFT, GOOGL, and AMZN,
processes it with Apache Spark, and outputs a summary table with 
average, max, and min closing prices per ticker.

## Architecture

```
stock_prices.csv
↓
PySpark reads and schemas the data
↓
Transformations (groupBy, aggregations)
↓
Stock summary output (Parquet)
```

## Stack

- Apache Spark 4.1.1 (PySpark)
- Python 3.12
- Java 17 (OpenJDK)

## Setup

This project uses the venv from `airflow-stock-pipeline`. 
Clone that repo first and activate its venv:

```bash
source ~/airflow-stock-pipeline/venv/bin/activate
pip install pyspark
```

## How to run

```bash
source ~/airflow-stock-pipeline/venv/bin/activate
python spark_etl.py
```

## Output

| Ticker | Days | Avg Close | Max Close | Min Close |
|--------|------|-----------|-----------|-----------|
| AAPL | 118 | $265.24 | $285.92 | $246.47 |
| AMZN | 118 | $226.00 | $254.00 | $198.79 |
| GOOGL | 118 | $309.39 | $343.45 | $267.11 |
| MSFT | 118 | $443.01 | $539.83 | $356.77 |

## What I learned

- How Spark differs from Pandas for large-scale data
- Creating SparkSession and reading CSV files
- Using Spark DataFrame API for aggregations
- Saving results in Parquet format
