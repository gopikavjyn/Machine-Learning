print("20 Gopika Vijayan")
import numpy as np
#import matplotlib.pyplot as plt
#import sklearn as sl
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import BernoulliNB
data = pd.read_csv("iris.csv")
x = data.iloc[:, :-1].values
y = data.iloc[:, 4].values
print(data.head())
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
print("x\n", x)
print("y\n", y)
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit(x_test)
classifier = GaussianNB()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(y_test)
cm = confusion_matrix(y_test, y_pred)
print("Accuracy is:", accuracy_score(y_test, y_pred))
print(cm)
df = pd.DataFrame({'Real value=', y_test, 'Predicted value=', y_pred})
print(pd)
classifier = BernoulliNB
classifier.fit(x_train, y_train)
y_pred = classifier.predict(y_test)
cm = confusion_matrix(y_test, y_pred)
print("Accuracy is:", accuracy_score(y_test, y_pred))
print(cm)
df = pd.DataFrame({'Real value=', y_test, 'Predicted value=', y_pred})
print(pd)



#https://github.com/gopikavjyn/Machine-Learning.git


