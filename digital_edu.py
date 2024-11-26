import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

data = pd.read_csv("train.csv")

data["bdate"] = data["bdate"].fillna("01.01.1900")
data["bdate"] = pd.to_datetime(data['bdate'], format='%d.%n.%Y', errors='coerce')

current_year = pd.read_csv
data["age"] = current_year = data['bdate'].dt.year
data["age"] = data['age'].fillna(data['age'].median())
data.drop(columns=['bdate'], inplace=True)

data['num_langs'] = data['langs'].apply()