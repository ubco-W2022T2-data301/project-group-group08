import pandas as pd
import numpy as np

def load1(url_or_path_to_csv_file):
    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .drop(columns = ['sex','age','children'])
          .dropna(axis = 0)
      )
    return df1
def load2(url_or_path_to_csv_file):
    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .drop(columns = ['sex','age','children','charges','bmi'])
          .groupby(['region']).value_counts()
          .dropna(axis = 0)
      )
    return df1

def load3(url_or_path_to_csv_file):
    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .drop(['sex','smoker','children'], axis = 1)
          .dropna(axis = 0)
      )
    return df1
def clean1(df):
    df1 = (
          df.groupby(['region'],as_index=False)['charges'].mean()
            .rename(columns = {'charges': 'Average cost'})
      )
    return df1
def clean2(df):
    df1 = (
          df.groupby(['region'],as_index=False)['bmi'].mean()
            .rename(columns = {'charges': 'Average bmi'})
      )
    return df1
def smoke(df):
    df1 = df[df['smoker'] == "yes"]
    return df1

def nosmoke(df):
    df1 = df[df['smoker'] == "no"]
    return df1