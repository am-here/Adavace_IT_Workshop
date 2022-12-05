from sklearn.linear_model import LinearRegression

X = [[3, 2], [2, 1], [1, 0], [3, 3], [4, 4], [5, 4], [5, 5], [3, 2], [2, 1], [1, 0]]
Y = [5, 4, 3, 6, 7, 8, 9, 5, 4, 3]

model = LinearRegression()
model.fit(X, Y)
print("R_squared: ", model.score(X, Y))
print("Slope: ", model.coef_)
print("Intercept: ", model.intercept_)
