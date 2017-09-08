import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt

X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
y = np.array([[49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T
plt.plot(X,y,'ro')
plt.axis([140, 190, 45, 75])
#plt.show()

one = np.ones((X.shape[0],1))

X = np.hstack((one,X))

#print X

A = np.dot(X.T,X)
b = np.dot(X.T,y)
w = np.dot(la.pinv(A),b)

print "w= " + str(w)

x0 = np.linspace(145,185,2)
y0 = w[0][0] + w[1][0]*x0

plt.plot(x0,y0)
plt.show()