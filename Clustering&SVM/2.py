import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

df = pd.read_csv("CSV_FILES/fruits.csv")

# USING 2 PARAMETERS
X = df.iloc[:, 1:3]
Y = df.iloc[:, 3:]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=4)
cf = SVC(kernel="rbf")
cf.fit(X_train, Y_train)
Y_pred = cf.predict(X_test)
print("Taking 2 parameters:")
print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_pred))
print("Classification Report:\n", classification_report(Y_test, Y_pred))
print("Accuracy Score: ", (accuracy_score(Y_test, Y_pred) * 100), "%")

# USING 1 PARAMETER
X = df.iloc[:, 1:2]
Y = df.iloc[:, 3:]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=4)
cf = SVC(kernel="rbf")
cf.fit(X_train, Y_train)
Y_pred = cf.predict(X_test)
print("Taking 1 parameter:")
print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_pred))
print("Classification Report:\n", classification_report(Y_test, Y_pred))
print("Accuracy Score: ", (accuracy_score(Y_test, Y_pred) * 100), "%")
