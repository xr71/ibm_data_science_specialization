import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge

## cars data
path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)
df.head()

# init lr
lr = LinearRegression()

X_data = df.drop("price", axis=1)
y_data = df.price

X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.33)

lr.fit(X_train[["horsepower", "city-mpg", "highway-mpg", "engine-size"]], y_train)

lr.score(X_test[["horsepower", "city-mpg", "highway-mpg", "engine-size"]], y_test)


lr.predict(X_test[["horsepower", "city-mpg", "highway-mpg", "engine-size"]])


## for ridge regression
# training on multiple values of alpha
# low alpha is likely to overfit
# high alpha is likely to underfit 

rr = Ridge(alpha=0.1)
rr.fit(X_train[["horsepower", "city-mpg", "highway-mpg", "engine-size"]], y_train)

rr.score(X_test[["horsepower", "city-mpg", "highway-mpg", "engine-size"]], y_test)