import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CSV_FILES\_nba.csv")
x = df[['Age','Weight']].plot(kind='box',title='Box-plot')
plt.show()