import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year of Production': ['2018','2019','2020','2021'],
    'Production Quantity': [50000,70000,60000,90000]
}

df = pd.DataFrame(data)
x = df['Year of Production']
y = df['Production Quantity']
plt.pie(y,labels=x)
plt.legend()
plt.show()