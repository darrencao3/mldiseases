import pandas as pd
from sklearn.naive_bayes import BernoulliNB
import pickle


training = pd.read_csv(r'C:\Users\kyuusarii\PycharmProjects\P3\code_folder\sim2.csv')

trainingX = training.loc[:, training.columns != "Disease"]
trainingY = training.loc[:, training.columns == "Disease"]

bnnb = BernoulliNB()
bnnb.fit(trainingX, trainingY)

filename = 'code_folder/bernoulliBayes.pkl'
pickle.dump(bnnb, open(filename, 'wb'))



