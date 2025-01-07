import argparse
import json
import time
import pyspark
import random

from itertools import combinations
from datetime import datetime


def price_pattern(price_lst):
  prev = price_lst[0]
  k = 1
  length = len(price_lst)
  result = [0]
  while(k<length):
    if(price_lst[k] < prev):
      result.append(-1)
    
    if(price_lst[k] > prev):
      result.append(1)
    
    if(price_lst[k] == prev):
      result.append(0)
    
    prev = price_lst[k]
    k += 1

  return result

# number of hash functions; defined in main()
num_hashes = 0
A_vals = []
B_vals = []

A_vals_bc = []
B_vals_bc = []


P = 114883
M = 100000


def generate_minhash(matrix_row):
  signature = [float('inf')] * num_hashes
  for i in matrix_row:
    hash_vals = [(A * i + B) % P % M for A, B in zip(A_vals, B_vals)]
    signature = [min(s, h) for s, h in zip(signature, hash_vals)]
  return signature

def split_into_bands(row, n_bands, n_rows):
  bands = []

  k = 0
  i = 0
  while(i < n_bands):
    bands.append(row[k : k + n_rows])
    k += n_rows
    i += 1

  remaining_users = len(row) % n_bands
  if remaining_users:
    final = [row[i] for i in range(k, len(row))]
    bands.append(final)
  
  return bands


def similarity(s_list1, s_list2):
  # u_set1 = set(u_list1)
  # u_set2 = set(u_list2)

  # print(u_set1)
  # print(u_set2)

  shared = 0
  k = 0
  length = len(s_list1)
  while(k<length):
    if(s_list1[k] == s_list2[k]):
      shared += 1
    
    k += 1

  return (shared / length)

def gen_vals(iterator):

  rows = list(iterator)

  k = 0
  for row in rows:

    b_id = row[0]
    if(k==0):
      print(b_id)
    
    k = 1
    u_lst = row[1]

    for item in u_lst:
      yield (tuple(item), [b_id])



def main(input_file, output_file, thr, n_bands, n_rows, sc):

  global num_hashes
  global A_vals
  global B_vals

  num_hashes = n_bands * n_rows
  A_vals = [random.randint(1, 1000) for _ in range(num_hashes)]  # Random A values
  B_vals = [random.randint(1, 1000) for _ in range(num_hashes)]  # Random B values

  data_rdd = sc.textFile(input_file)

  header = data_rdd.first()
  columns = header.split(",")
  rows = data_rdd.filter(lambda row: row!= header)

  # map each row to be listed with the date, stock ticker, and closing price for that day
  structured_rdd = rows.map(lambda row: {(row[0:10], (columns[i], value)) for i,value in enumerate(row.split(",")[1:])})
  structured_rdd = structured_rdd.flatMap(lambda x: x)

  # restructure the RDD and sort rows in order of date; each row contains a tuple: (stock_ticker, list_of_prices sorted by date)
  structured_rdd = structured_rdd.map(lambda row: (row[1][0], [(row[0], row[1][1])])).reduceByKey(lambda a,b: a+b)
  sorted_by_date = structured_rdd.map(lambda row: (row[0], sorted(row[1], key=lambda tuple: datetime.strptime(tuple[0], "%Y-%m-%d"))))

  # extract only the price lists
  price_lst_rdd = sorted_by_date.map(lambda row: (row[0], [tup[1] for tup in row[1]]))

  # create a pattern for each ticker based on price increases / decreases using the price_pattern function
  matrix_rdd = price_lst_rdd.map(lambda row: (row[0], price_pattern(row[1])))

  # dictionary with tickers as keys and the pattern as values
  stock_price_dict = matrix_rdd.collectAsMap()

  # use the min-hash algorithm to generate signatures for each stock
  minhashes = matrix_rdd.map(lambda x: (x[0], generate_minhash(x[1])))

  # split min-hash sigs into n_bands : RDD map
  minhash_bands = minhashes.map(lambda x: (x[0], split_into_bands(x[1], n_bands, n_rows)))

  # find stocks that share a given band
  similarity_rdd = minhash_bands.mapPartitions(lambda x: gen_vals(x)).reduceByKey(lambda x,y: x+y).filter(lambda x: len(x[1]) > 1)

  # form candidate pairs of stocks based on lists of stocks that contain a band
  candidates = similarity_rdd.mapPartitions(lambda x: (pair for _, items in x for pair in combinations(items,2)))

  # finding similarity for each of the candidate stock pairs
  sim = candidates.map(lambda x: (x, similarity(stock_price_dict[x[0]], stock_price_dict[x[1]])))
  
  # filter based on the threshold value
  sim = sim.filter(lambda x: x[1] >= thr and x[1]<1)

  # extract a sample of data formatted in json
  output_rdd = sim.map(lambda x: {"stock_1":x[0][0], "stock_2": x[0][1], "sim":x[1]})
  sectioned_data = output_rdd.map(lambda x: json.dumps(x)).take(10000)  

  # Write the collected data to a single JSON file
  with open(output_file, "w") as f:
    for line in sectioned_data:
      f.write(line + "\n")  # Each JSON object on a new line
  


if __name__ == '__main__':
  start_time = time.time()
  sc_conf = pyspark.SparkConf() \
    .setAppName('similarities_stocks') \
    .setMaster('local[*]') \
    .set('spark.driver.memory', '8g') \
    .set('spark.executor.memory', '4g')
  sc = pyspark.SparkContext(conf=sc_conf)
  sc.setLogLevel("OFF")

  parser = argparse.ArgumentParser(description='A1T1')
  parser.add_argument('--input_file', type=str, default='../combined_all.csv')
  parser.add_argument('--output_file', type=str, default='../outputs/similarities.out')
  parser.add_argument('--threshold', type=float, default=0.9)
  parser.add_argument('--n_bands', type=int, default=50)
  parser.add_argument('--n_rows', type=int, default=2)
  args = parser.parse_args()

  main(args.input_file, args.output_file, args.threshold, args.n_bands, args.n_rows, sc)
  sc.stop()

  print('The run time is: ', (time.time() - start_time))


