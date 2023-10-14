import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv('DATASET.csv')

X = df.drop("Placed",axis = 1)
Y = df["Placed"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
regressor = RandomForestRegressor(random_state=42, n_jobs=-1, max_depth=5, n_estimators=100, oob_score=True)
regressor.fit(X_train, Y_train)

pickle.dump(regressor, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))

print(model.predict([[100,100,67,89,100,100,100,60,90,100,100,100,100,100,100]]))
