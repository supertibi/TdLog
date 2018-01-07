# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 21:10:38 2018

@author: thibaut
"""

'''http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html'''
'''http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD'''


import numpy as np
import time

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA




mat=np.random.rand(45000,24)


pca = PCA(n_components=2)
pca.fit(mat)
print(pca.explained_variance_ratio_) 
#print(pca.singular_values_)



print('----------------les k means-------------------------------------')

X = np.array([[1, 2], [1, 4], [1, 0],[4, 2], [4, 4], [4, 0]])
kmeans = KMeans(n_clusters=4500, random_state=0).fit(mat)
print(kmeans.labels_)
#print(kmeans.predict([[0, 0], [4, 4]]))
#print(kmeans.cluster_centers_)