"""
1. choose K random points as init centers
2. assign each points to its closest center
3. re-compute the centers
4. if centers are unchanged, stop the algorithm
5. back to step 2

O(n * K * I * d)

n : number of points
K : number of clusters
I : number of iterations
d : number of attributes

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

means = [[0,0], [1,8], [5,2]]
N = 500
cov = [[1,0], [0,1]]
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)
X = np.concatenate((X0,X1,X2),axis=0)


def kmeans_display(X, label):
    X0 = X[label == 0, :]
    X1 = X[label == 1, :]
    X2 = X[label == 2, :]

    plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize=4, alpha=.8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize=4, alpha=.8)
    plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize=4, alpha=.8)

    plt.axis('equal')
    plt.plot()
    plt.show()

def init_center(X, k):
    return X[np.random.choice(X.shape[0], k, replace=False)]

def assign_labels(X, centers):
    D = cdist(X, centers)
    return np.argmin(D, axis=1)

def update_centers(X, labels, K):
    centers = np.zeros((K, X.shape[1]))
    for k in range(K):
        Xk = X[labels == k,:]
        centers[k,:] = np.mean(Xk,axis=0)

    return centers

def is_converged(centers, new_centers):
    return(set([tuple(a) for a in centers]) ==
           set([tuple(a) for a in new_centers]))

def kmean(X,K):
    centers = init_center(X,K)
    labels = []
    count = 0
    while True:
        labels = assign_labels(X, centers)
        new_centers = update_centers(X, labels, K)
        if is_converged(centers, new_centers):
            break

        count +=1
        centers = new_centers

    return centers, labels, count

centers , labels, count = kmean(X,3)

print count
kmeans_display(X, labels)

