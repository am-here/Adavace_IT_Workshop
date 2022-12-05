import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CSV_FILES\employee_details.csv")
x = df['Name']
y = df['Salary']
plt.bar(x,y)
plt.show()