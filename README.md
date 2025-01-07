# Stock Pair Trading

## Overview

This project identifies pairs of stocks with similar price movement patterns based on a target similarity threshold. This is to illustrate how these similar pairs of stocks can be used in pair trading strategies. Using a simple method of comparing changes in the closing prices of a collection of NASDAQ stocks, the system applies the **Min-Hash algorithm** to generate candidate pairs efficiently. This approach can be adapted to other domains requiring pattern-based similarity detection. 

## Development Process
(1) Building a dataset of stock closing prices
- Downloaded NASDAQ stock ticker symbols into a csv file
- Utilized Python's yfinance library to gather price data
- Generated a list of all tickers from the csv that can also be found in the yfinance database
- Using a multi-threaded approach, download closing price data for the stocks in a specific timeframe (Jan. 15, 2023 - Feb. 15, 2023) in batches
- Store the data in a set of CSV files, and combine the CSV files into a single dataset (faster than downloading and writing all rows to a single CSV file)

(2) Producing pairs of stocks that are similar
- Utilize pyspark RDDs to stucture stock data
- Min-Hash algorithm to generate signatures for stock pairs
- Determine similarities of stock pairs
- Filter pairs based on a similarity threshold (stock pairs with similarity greater than equal to the threshold would be of interest)
- Take a sample of the data to store locally and output as JSON

---

## Concepts Learned
- **Min-Hash and Locality Sensitive Hashing**: recognizing the role of locality sensitive hashing techniques in minimizing the size of the dataset to allow for fewer comparisons when trying to determine similar pairs 
- **Multi-Threading**: downloading large amounts of data was initially time consuming, until I implemented a multi-threaded approach to retrieve stock closing prices within a 30-day range
- **CSV Files**: reading and writing to CSV files, and performing operations to combine multiple files to produce a single, large dataset

---

## Tech Stack

- **Python**: Core logic and data processing.
- **PySpark**: Distributed computation for handling large datasets.
- **JSON**: Exporting similarity results for further analysis.

---

## Setup and Installation
(1) Clone this repository:

```git clone https://github.com/jkan2903/stock-pair-trading.git```

(2) Install required dependencies:

```pip install pyspark``` (version 3.5.3 was used for this project)

(3) Prepare a stock and closing prices dataset

Follow instructions seen in ```raw-data.py```, and run ```combine-csv.py``` next

(4) Run the script:

```python stock_similarity.py --input_file <input_csv_path> --output_file <output_json_path> --threshold 0.9 --n_bands 50 --n_rows 2```


