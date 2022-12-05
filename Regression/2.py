import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

df = pd.read_csv("CSV_FILES\student-pass-fail-data.csv")
X = df.iloc[:, :2]
Y = df.iloc[:, 2:]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=4)
logistic_regression = LogisticRegression()
logistic_regression.fit(X_train, Y_train)
Y_pred = logistic_regression.predict(X_test)
print("Accuracy = ", (accuracy_score(Y_test, Y_pred)) * 100, "%")
print(confusion_matrix(Y_test, Y_pred))


print("For Half row:")
size = (int)(df.iloc[:, :1].size / 2)
print(type(size))
df = df.head(size)
X = df.iloc[:, :2]
Y = df.iloc[:, 2:]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=4)
logistic_regression = LogisticRegression()
logistic_regression.fit(X_train, Y_train)
Y_pred = logistic_regression.predict(X_test)
print("Accuracy = ", (accuracy_score(Y_test, Y_pred)) * 100, "%")
print(confusion_matrix(Y_test, Y_pred))
