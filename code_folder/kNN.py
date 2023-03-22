import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import pickle


training = pd.read_csv(r'C:\Users\kyuusarii\PycharmProjects\P3\code_folder\sim2.csv')

trainingX = training.loc[:, training.columns != "Disease"]
trainingY = training.loc[:, training.columns == "Disease"]

knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(trainingX, trainingY)

filename = 'code_folder/kNN.pkl'
pickle.dump(knn, open(filename, 'wb'))
