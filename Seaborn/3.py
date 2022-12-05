import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('iris')
sns.jointplot(x="sepal_length",y="sepal_width",kind="hex",data=df)
plt.show()