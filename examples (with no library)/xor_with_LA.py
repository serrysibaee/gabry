# implement this is numpy
import numpy as np
import math
from math import e

## did not test this code yet ^__^

xor_train = [[0,0,0],[0,1,1],[1,1,0],[1,0,1]]
np_xor = np.array(xor_train)
X = np_xor[:,0:2]
print(X.shape)
X = np.hstack([np.ones((4,1)),X])
# print(np.ones((5,1)))
print(X)

y = np_xor[:,2]
y = y.reshape((4,1))
W1 = np.random.rand(3,2)
W2 = np.random.rand(2,1)
print(X.shape, y.shape)



lr = 1e-2

def sigmoid(lst):
  return (1/(1+e**(-lst)))
epcs = 1
for ep in range(epcs):
  
  # forward
  Z = X@W1
  y_hat = Z@W2

  cost = ((y_hat.flatten() - y)**2).sum()

  print(cost)
  
  # backward
  dEy = (y_hat - y)*(2/len(y))  # (4,1)

  # dW2, dZ
  dydW2 = Z # (4,2)
  dW2 = dydW2.T * dEy # (2,4)*(4,1) --> (2,1)
  W2 = W2 - (lr*dW2)
  dEdZ = dEy * W2.T # (4,1)*(1,2) --> (4,2)
  # dydZ is dEy for next layer
  # dW1
  dW1 = dEdZ * X
  W1 = W1 - (lr*dW1) 


