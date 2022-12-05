import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CSV_FILES\dirtydata.csv")
x = df[['Duration']].plot(kind='box',title='Box-plot')
plt.show()