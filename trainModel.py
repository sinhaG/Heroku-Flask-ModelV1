import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import pickle
from sklearn.preprocessing import StandardScaler

def createmodel_Contact():
    path = './data/contacts1.csv'
    data = pd.read_csv(path)
    #print("df shape:", data.shape)

    # droppping the Columns

    # Remove column name 'A'
    data = data.drop(['FirstName', 'LastName', 'MobilePhone', 'email', 'city', 'county_name', 'state_id'], axis=1)

    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # statistics of scaled data
    pd.DataFrame(data_scaled).describe()

    # defining the kmeans function with initialization as k-means++
    kmeans = KMeans(n_clusters=2, init='k-means++')

    # fitting the k means algorithm on scaled data
    kmeans.fit(data_scaled)

    SSE = []
    for cluster in range(1, 20):
        kmeans = KMeans(n_jobs=-1, n_clusters=cluster, init='k-means++')
        kmeans.fit(data_scaled)
        SSE.append(kmeans.inertia_)

    kmeans = KMeans(n_jobs=-1, n_clusters=5, init='k-means++')
    kmeans.fit(data_scaled)
    pred = kmeans.predict(data_scaled)

    frame = pd.DataFrame(data_scaled)
    frame['cluster'] = pred
    frame['cluster'].value_counts()

    #print(frame)

    # save the model to disk
    filename = 'contact_model.sav'
    pickle.dump(kmeans, open(filename, 'wb'))

def createmodel_Wholesale():
    """
    https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/
    We will be working on a wholesale customer segmentation problem. You can download the dataset using this link.
    The data is hosted on the UCI Machine Learning repository.

    The aim of this problem is to segment the clients of a wholesale distributor based on their annual spending on diverse
    product categories, like milk, grocery, region, etc. So, let’s start coding!
    """
    path = './data/clustering.csv'
    data = pd.read_csv(path)
    #print("df shape:", data.shape)

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # statistics of scaled data
    pd.DataFrame(data_scaled).describe()

    # defining the kmeans function with initialization as k-means++
    kmeans = KMeans(n_clusters=2, init='k-means++')

    # fitting the k means algorithm on scaled data
    kmeans.fit(data_scaled)

    SSE = []
    for cluster in range(1, 20):
        kmeans = KMeans(n_jobs=-1, n_clusters=cluster, init='k-means++')
        kmeans.fit(data_scaled)
        SSE.append(kmeans.inertia_)

    kmeans = KMeans(n_jobs=-1, n_clusters=5, init='k-means++')
    kmeans.fit(data_scaled)
    pred = kmeans.predict(data_scaled)

    frame = pd.DataFrame(data_scaled)
    frame['cluster'] = pred
    frame['cluster'].value_counts()

    # save the model to disk
    filename = 'finalized_model.sav'
    pickle.dump(kmeans, open(filename, 'wb'))

