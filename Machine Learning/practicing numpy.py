import numpy as np
from numpy import linalg as la
# a = np.arange(20).reshape(4,5)
# print a
# print a.ndim
# print a.shape[0]
# print a.size
#
# b = np.array([[5,6],[1,2,3]])
# print b
#
# c = np.zeros((3,4))
# print c
#
# d = np.ones((3,4))
# print d
#
# e = np.arange(10,20,3)
# print e
#
# print np.pi

a = np.arange(15).reshape(3,-1)
# print a.astype(float)
#
# print np.random.random((3,4))
# print np.random.rand(3)
print a.ravel()
print a
print a.T

c = np.floor(10*np.random.random((2,4)))
d = np.floor(10*np.random.random((2,4)))
# print c
# print d
# print np.vstack((c,d))
# print np.vstack((d,c))

# print np.concatenate((c,d), axis=1)

a = np.floor(10*np.random.random((4,4)))
print a
print la.inv(a)
print np.eye(5,5)
print np.dot(a,a)
print np.trace(a)