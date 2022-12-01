import pandas as pd
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
athletes = pd.read_csv("datasets/athlete_events.csv")
df = pd.DataFrame(athletes)
df.head()
belg = df[df["NOC"]=="BEL"]
goud = belg[belg["Medal"]=="Gold"]
goud