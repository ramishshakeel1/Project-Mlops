import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import os

def preprocess():
    os.makedirs('data/processed', exist_ok=True)
    df = pd.read_csv('data/raw/game_data.csv')
    
    # Checking for missing values 
    if df.isnull().sum().sum() > 0:
        print("Missing values found. Proceeding with imputation.")
    
    # sorting categorical and numerical columns
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_columns = df.select_dtypes(include=['object']).columns
    
    # Imputing missing values
    numeric_imputer = SimpleImputer(strategy='median')
    df[numerical_columns] = numeric_imputer.fit_transform(df[numerical_columns])

    categorical_imputer = SimpleImputer(strategy='most_frequent')
    df[categorical_columns] = categorical_imputer.fit_transform(df[categorical_columns])

    # Encoding categorical variables
    df['fight_result'] = LabelEncoder().fit_transform(df['fight_result'])
    
    df.to_csv('data/processed/processed_data.csv', index=False)
    print("Data cleaned and saved to data/processed/processed_data.csv")

    return df

if __name__ == "__main__":
    df = preprocess()
    print("Data processing complete.")