import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

import seaborn as sns 
import matplotlib.pyplot as plt 


## cars data set
path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)
df.head()

sns.scatterplot(x="horsepower", y="price", data=df)
sns.scatterplot(x="engine-size", y="price", data=df)
sns.scatterplot(x="highway-mpg", y="price", data=df)

Input = [
    ("scale", StandardScaler()),
    ("poly", PolynomialFeatures()),
    ("model", LinearRegression()) 
]

pipe = Pipeline(Input)

pipe.fit(df[["horsepower", "engine-size", "highway-mpg"]], df.price.values)
