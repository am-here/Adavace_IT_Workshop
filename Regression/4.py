from sklearn.datasets import make_regression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X, Y = make_regression(n_features=1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
reg = LinearRegression()
reg.fit(X_train, Y_train)
Y_pred = reg.predict(X_test)
plt.scatter(X_test, Y_test)
plt.scatter(X_test, Y_pred)
plt.show()
print("Score: ", (reg.score(Y_test, Y_pred) * 100), "%")
