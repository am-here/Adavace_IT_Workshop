import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")
x = df.iloc[:, :4]
print(x.corr())
corr = x.corr()
sns.heatmap(corr, cmap=sns.diverging_palette(220, 10, as_cmap=True), linewidths=1)
plt.show()
