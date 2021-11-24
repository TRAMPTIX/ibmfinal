import os
import pickle
import numpy as np 
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV


DATA_PATH = '/content/Crop_recommendation.csv'
df = pd.read_csv(DATA_PATH)
df.head()
df.describe(include="all")
df['label'].value_counts()

X = df.iloc[:,:-1]     
y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state =2)
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)
print('y_train shape:', y_train.shape)
print('y_test shape:', y_test.shape)

KNN_model = KNeighborsClassifier()
KNN_model.fit(X_train,y_train)

y_pred = KNN_model.predict(X_test)

file = open('KNN_model_crop_prediction.pkl', 'wb')

pickle.dump(KNN_model, file)
