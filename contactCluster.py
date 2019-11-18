import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import pickle

path = './data/contacts1.csv'
data = pd.read_csv(path)
print("df shape:", data.shape)


from sklearn.preprocessing import StandardScaler

# droppping the Columns

# Remove column name 'A'
data = data.drop(['FirstName','LastName','MobilePhone','email','city','county_name','state_id'], axis = 1)


scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# statistics of scaled data
pd.DataFrame(data_scaled).describe()

# defining the kmeans function with initialization as k-means++
kmeans = KMeans(n_clusters=2, init='k-means++')

# fitting the k means algorithm on scaled data
kmeans.fit(data_scaled)

SSE = []
for cluster in range(1,20):
    kmeans = KMeans(n_jobs = -1, n_clusters = cluster, init='k-means++')
    kmeans.fit(data_scaled)
    SSE.append(kmeans.inertia_)

# converting the results into a dataframe and plotting them
frame = pd.DataFrame({'Cluster':range(1,20), 'SSE':SSE})
plt.figure(figsize=(12,6))
plt.plot(frame['Cluster'], frame['SSE'], marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')


kmeans = KMeans(n_jobs = -1, n_clusters = 5, init='k-means++')
kmeans.fit(data_scaled)
pred = kmeans.predict(data_scaled)


frame = pd.DataFrame(data_scaled)
frame['cluster'] = pred
frame['cluster'].value_counts()

print(frame)


def prediction(param):
    print("in prediction================")
    print(param)
    print(kmeans.predict(param))

prediction(data.iloc[[2]])

# save the model to disk
filename = 'contact_model.sav'
pickle.dump(kmeans, open(filename, 'wb'))