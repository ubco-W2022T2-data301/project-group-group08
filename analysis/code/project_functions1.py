import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .drop(['sex', 'bmi','children', 'smoker', 'region'], axis = 1)
          .dropna(axis = 0)
      )
    return df1

def clean_and_wrangle(df):
    df1 = (
          df.groupby(['age'],as_index=False)['charges'].mean()
            .rename(columns = {'age': 'Age','charges': 'Average cost'})
      )
    return df1