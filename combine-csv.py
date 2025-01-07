import csv
import pandas as pd

NO_OF_FILES = 9


dataframes = []

# read all CSV files
k = 0
while(k<NO_OF_FILES):
  fname = "sample_data_"+str(k)+".csv"
  df = pd.read_csv(fname, delimiter='\t')
  dataframes.append(df)

  k += 1

# combine CSV files
k = 1
final_dataframe = dataframes[0]
while(k<NO_OF_FILES):

  df = dataframes[k]

  df_cols = set(df.columns)
  df_curr_cols = set(final_dataframe.columns)

  # only add columns that aren't already present from the previous iteration
  new_cols = df_curr_cols - df_cols.intersection(df_curr_cols)
  df_new = df[list(new_cols)]

  new_final_dataframe = pd.concat([df_new, final_dataframe], axis=1, ignore_index=False, sort=False)
  final_dataframe = new_final_dataframe

  k += 1

final_dataframe.to_csv("combined_all.csv", index=False)