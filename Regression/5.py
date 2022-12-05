import numpy as np
from sklearn.linear_model import LinearRegression

yoe = np.array([3, 2, 1, 3, 4, 5, 5, 3, 2, 1, 1]).reshape(-1, 1)
level = np.array([2, 1, 0, 3, 4, 4, 5, 2, 1, 0, 0]).reshape(-1, 1)
leow = np.array([5, 3, 2, 5, 5, 8, 8, 4, 3, 2, 0]).reshape(-1, 1)
city = np.array([1, 1, 2, 5, 4, 3, 6, 7, 4, 2, 3]).reshape(-1, 1)
Y = np.array([5, 4, 3, 6, 7, 8, 9, 5, 4, 3, 1])
X = np.array([yoe, level, leow, city]).reshape(11, 4)
model = LinearRegression()
model.fit(X, Y)
print("\nX = [yoe, level, leow, city]:")
print("R-squared: ", model.score(X, Y))
print("\nX = [yoe]:")
X = yoe
model = LinearRegression()
model.fit(X, Y)
print("R-squared: ", model.score(X, Y))
print("Intercept: ", model.intercept_)
print("Slope: ", model.coef_)
b0 = (model.intercept_).round(4)
b1 = (model.coef_[0]).round(4)
print("Equation: ", b0, "+", b1, "* X ")
print("\nX = [level]:")
X = level
model = LinearRegression()
model.fit(X, Y)
print("R-squared: ", model.score(X, Y))
print("Intercept: ", model.intercept_)
print("Slope: ", model.coef_)
b0 = (model.intercept_).round(4)
b1 = (model.coef_[0]).round(4)
print("Equation: ", b0, "+", b1, "* X ")
print("\nX = [leow]:")
X = leow
model = LinearRegression()
model.fit(X, Y)
print("R-squared: ", model.score(X, Y))
print("Intercept: ", model.intercept_)
print("Slope: ", model.coef_)
b0 = (model.intercept_).round(4)
b1 = (model.coef_[0]).round(4)
print("Equation: ", b0, "+", b1, "* X ")