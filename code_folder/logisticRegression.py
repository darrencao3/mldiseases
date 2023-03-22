import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle


training = pd.read_csv(r'C:\Users\kyuusarii\PycharmProjects\P3\code_folder\sim2.csv')

trainingX = training.loc[:, training.columns != "Disease"]
trainingY = training.loc[:, training.columns == "Disease"]

lr = LogisticRegression(max_iter=1000000)
lr.fit(trainingX, trainingY)

filename = 'code_folder/logisticRegression.pkl'
pickle.dump(lr, open(filename, 'wb'))
