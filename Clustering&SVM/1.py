import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("CSV_FILES/tips.csv")
X = df["total_bill"]
Y = df["tip"]
kmeans = KMeans(n_clusters=3)
kmeans.fit(df.iloc[:, :2])
plt.scatter(X, Y, c=kmeans.labels_)
# #to show centroids
# for i in kmeans.cluster_centers_:
#     plt.scatter(i[0], i[1], marker="*", c="black", s=100)
plt.show()
