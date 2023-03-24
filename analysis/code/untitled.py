import pandas as pd
import numpy as np

def load_process_clean_medical_no_sex(url_or_path_to_csv_file):
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(['children', 'smoker', 'region', 'sex'], axis = 1)
        .dropna()
    )
    return df

def load_process_clean_income(url_or_path_to_csv_file):
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(['workclass', 'fnlwgt', 'education', 'education.num','marital.status','occupation','relationship','race','sex','capital.gain','capital.loss','native.country', 'income'], axis = 1)
        .dropna()
    )
    return df

def wrangle_medical(df):
    df = (
        df.groupby(df['age'], as_index=False)
        .mean()
        .rename(columns = {'age': 'Age', 'bmi': 'BMI', 'charges':'Average Cost'})
    )
    return df

def wrangle_income(df):
    df = (
        df.groupby(df['age'], as_index=False)
        .mean()
        .rename(columns = {'age': 'Age', 'hours.per.week': 'Working Hours per Week'})
    )
    return df

def load_process_clean_medical(url_or_path_to_csv_file):
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(['children', 'smoker', 'region'], axis = 1)
        .dropna()
    )
    return df

def categorize_bmi(df):
    ranges = [0, 18.5, 25, 30, 35, 40, 100]
    lab_txt = ['Underweight', 'Normal', 'Overweight', 'Obese Class I', 'Obese Class II', 'Obese Class III']
    lab_num = [1, 2, 3, 4, 5, 6]
    df['BMI_cat'] = pd.cut('bmi', bins=ranges, labels=lab_txt, include_lowest=True)
    df['BMI_cat_num'] = pd.cut('bmi', bins=ranges, labels=lab_num, include_lowest=True)
    return df

#source: https://www.canada.ca/en/health-canada/services/food-nutrition/healthy-eating/healthy-weights/canadian-guidelines-body-weight-classification-adults/body-mass-index-nomogram.html 