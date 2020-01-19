import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df2 = pd.read_csv('datasets/statsRatings.csv', float_precision='round_trip')
df2.drop("Unnamed: 0", axis=1, inplace=True)

X = df2[['3P','3P%','2P','2P%','FT','FT%','TRB','AST','BLK']].values
y = df2['ratings'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
#regressor.predict([[1.6, 0.401, 4.3, 0.532, 2.7, 0.754, 3.2, 2.7, 0.5]])

def predictRating(threeMade, threeAccuracy, twoMade, twoAccuracy, ft, ftAccuracy, reb, assist, blk):
    return regressor.predict([[threeMade, threeAccuracy, twoMade, twoAccuracy, ft, ftAccuracy, reb, assist, blk]])
