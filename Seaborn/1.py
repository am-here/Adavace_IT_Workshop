import seaborn as sns
import matplotlib.pyplot as plt
# print(sns.get_dataset_names()) 
df = sns.load_dataset('iris')
df.describe().plot(kind = "area")
plt.show()