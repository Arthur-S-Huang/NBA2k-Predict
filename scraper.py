import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as seabornInstance

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.options.mode.chained_assignment = None

#stats_page = requests.get('https://www.basketball-reference.com/leagues/NBA_2020_per_game.html')
#page = stats_page.content
#soup = BeautifulSoup(page, 'html.parser')
#table = soup.find('table', id='per_game_stats')
#html_str = str(table)
#df = pd.read_html(html_str)[0]
#df.drop(df.index[[20, 41, 62, 83, 104, 125, 146, 167, 188, 209, 230, 251, 272,
                  #293, 314, 335, 356, 377, 398, 419, 440, 461, 482]], inplace=True)
#df.drop(["Rk", "Age", "Pos", "MP", "FGA", "FG", "FG%", "eFG%",
         #"G", "GS", "FTA", "ORB", "DRB", "TOV", "PF"], axis=1, inplace=True)

#df.fillna(0, inplace=True)
#df.to_csv('datasets/results.csv')

#playground
df2 = pd.read_csv('datasets/statsRatings.csv', float_precision='round_trip')
df2.drop("Unnamed: 0", axis=1, inplace=True)

X = df2[['3P','3P%','2P','2P%','FT','FT%','TRB','AST','BLK']].values
y = df2['ratings'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
df3 = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df3)
print(r2_score(y_test, y_pred))
print(regressor.predict([[3, 0.327, 6.4, 0.62, 7.4, 0.803, 9.6, 8.9, 0.1]]))

df3.plot(kind='bar',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

#print(df2)
'''
reg = linear_model.LinearRegression()
reg.fit(df2[['3P','3P%','2P','2P%','FT','FT%','TRB','AST','BLK','PTS']], df2.ratings)
print(reg.coef_)
print(reg.intercept_)
#print(reg.predict([[8.9, 2.1, 22.6]]))#zion duke

print(reg.predict([[1.9, 0.338, 1.9, 0.43, 0.6, 0.5, 4.8, 5.3, 0.3, 10.1]]))#Lonzo Pelicans
print(reg.predict([[2.2, 0.412, 3, 0.732, 1.8, 0.673, 6, 7.6, 0.8, 14.6]]))
print(reg.predict([[5.1, 0.367, 5.9, 0.559, 11.2, 0.878, 5.8, 7.4, 0.7, 38.6]]))#James Harden
print(reg.predict([[2.2, 0.356, 7.8, 0.558, 3.6, 0.667, 7.5, 10.6, 0.7, 25.8]]))#LBJ
print(reg.predict([[3, 0.327, 6.4, 0.62, 7.4, 0.803, 9.6, 8.9, 0.1, 29.3]]))#Luka
print(reg.predict([[0.6, 0.462, 0.7, 0.194, 1.1, 0.917, 1.1, 0.9, 0.4, 4.3]]))#Jacob Evans
print(reg.predict([[0, 0, 5, 0.627, 1.4, 0.486, 9.9, 2.8, 1.2, 11.5]]))#Steven Adams
print(reg.predict([[0, 0, 6.7, 0.8, 6.3, 0.704, 10.7, 0.3, 3, 19.7]]))#James Wiseman
print(reg.predict([[1.2, 0.28, 3.1, 0.617, 3, 0.773, 5.7, 5, 0.4, 12.8]]))#Luka Euro
print(reg.predict([[0.7, 0.338, 8.2, 0.747, 3.9, 0.64, 8.9, 2.1, 1.8, 22.6]]))#zion duke
print(reg.predict([[1.7, 0.25, 4.6, 0.458, 2.8, 0.723, 7.6, 6.8, 0.1, 17]]))#melo
print(reg.predict([[1.6, 0.401, 4.3, 0.532, 2.7, 0.754, 3.2, 2.7, 0.5, 16.1]]))

print(r2_score([77, 97, 97, 96, 71, 83], [78.902689, 97.63361874, 92.62667606, 95.05080874,71.5880308, 82.08700444]))
'''
