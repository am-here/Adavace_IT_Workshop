from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

X = np.arange(10).reshape(-1, 1)
Y = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 1])

model = LogisticRegression(C=1)
model.fit(X, Y)
Y_pred = model.predict(X)
print("Accuracy for C=1: ", (accuracy_score(Y, Y_pred) * 100), "%")

model = LogisticRegression(C=3)
model.fit(X, Y)
Y_pred = model.predict(X)
print("Accuracy for C=3: ", (accuracy_score(Y, Y_pred) * 100), "%")

model = LogisticRegression(C=5)
model.fit(X, Y)
Y_pred = model.predict(X)
print("Accuracy for C=5: ", (accuracy_score(Y, Y_pred) * 100), "%")
