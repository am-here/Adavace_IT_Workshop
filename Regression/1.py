import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("CSV_FILES\position_salaries.csv")

X = df[["Level"]]
Y = df["Salary"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.25)
lin_reg = LinearRegression()
lin_reg.fit(X, Y)
plt.scatter(X_test, Y_test)
Y_pred = lin_reg.predict(X_test)
plt.plot(X_test, Y_pred, color="red")
plt.show()
print(lin_reg.score(X, Y))
