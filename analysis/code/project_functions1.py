import pandas as pd
import numpy as np

def load_and_process_age(url_or_path_to_csv_file):
    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .drop(['sex', 'bmi','smoker', 'region'], axis = 1)
          .dropna(axis = 0)
      )
    return df1

def load_and_process_agebmi(url_or_path_to_csv_file):
    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .drop(['sex','smoker', 'region'], axis = 1)
          .dropna(axis = 0)
      )
    return df1

def clean_and_wrangle_agecost(df):
    df1 = (
          df.groupby(['age'],as_index=False)['charges'].mean()
            .rename(columns = {'age': 'Age','charges': 'Average cost'})
      )
    return df1

def clean_and_wrangle_agebmi(df):
    df1 = (
          df.groupby(['age'],as_index=False)['bmi'].mean()
            .rename(columns = {'age': 'Age','bmi': 'Bmi'})
      )
    return df1

def clean_and_wrangle_bmi(df):
    df1 = (
          df.groupby(['bmi'],as_index=False)['charges'].mean()
            .rename(columns = {'bmi': 'Bmi','charges': 'Average cost'})
      )
    return df1

def clean_and_wrangle_ca(df):
    df1 = (
          df.groupby(['bmi'],as_index=False)['charges'].mean()
            .rename(columns = {'bmi': 'Bmi','charges': 'Average cost'})
      )
    return df1