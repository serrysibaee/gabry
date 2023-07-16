# model XOR
import random
random.seed(10)
from math import e
import math
import matplotlib.pyplot as plt

class Model:
  def __init__(self,w11,w12,w21,b1,b2,w22,z1,z2,bz):
    self.w11 = w11
    self.w12 = w12
    self.w21 = w21
    self.w22 = w22
    self.b1 = b1
    self.b2 = b2
    self.z1 = z1
    self.z2 = z2
    self.bz = bz
    # not to be from user
    self._lr = None
    self._eps = None

  def random_parameter(mada):
    return random.random()*mada

  # def init_weights(self):
  #   random_weights = [random_parameter(1) for i in range(9)]

  def model_parameters(self):
    return f"""
    {self.w11},
    {self.w12},
    {self.w21},
    {self.w22},
    {self.b1},
    {self.b2},
    {self.z1},
    {self.z2},
    {self.bz}
        """

  def forward(self,x1,x2):
    # print("w11 in forward: ",self.w11)
    a1 = sigmoid(x1*self.w11 + x2*self.w12 + self.b1)
    a2 = sigmoid(x1*self.w21 + x2*self.w22 + self.b2)
    y_hat = sigmoid(a1*self.z1 + a2*self.z2 + self.bz)
    return y_hat


  def backward(self,cost):

    # cost
    dy = cost(self)
    # w11
    pre_w11 = self.w11
    self.w11 = self.w11 + self._eps
    dw11 = (cost(self)-dy)/self._eps
    self.w11 = pre_w11
    # w12
    pre_w12 = self.w12
    self.w12 = self.w12 + self._eps
    dw12 = (cost(self)-dy)/self._eps
    self.w12 = pre_w12
    # w21
    pre_w21 = self.w21
    self.w21 = self.w21 + self._eps
    dw21 = (cost(self)-dy)/self._eps
    self.w21 = pre_w21
    # w22
    pre_w22 = self.w22
    self.w22 = self.w22 + self._eps
    dw22 = (cost(self)-dy)/self._eps
    self.w22 = pre_w22
    # b1
    pre_b1 = self.b1
    self.b1 = self.b1 + self._eps
    db1 = (cost(self)-dy)/self._eps
    self.b1 = pre_b1
    # b2
    pre_b2 = self.b2
    self.b2 = self.b2 + self._eps
    db2 = (cost(self)-dy)/self._eps
    self.b2 = pre_b2
    # z1
    pre_z1 = self.z1
    self.z1 = self.z1 + self._eps
    dz1 = (cost(self)-dy)/self._eps
    self.z1 = pre_z1
    # z2
    pre_z2 = self.z2
    self.z2 = self.z2 + self._eps
    dz2 = (cost(self)-dy)/self._eps
    self.z2 = pre_z2
    # bz
    pre_bz = self.bz
    self.bz = self.bz + self._eps
    dbz = (cost(self)-dy)/self._eps
    self.bz = pre_bz


    # making the update here after finishing all
    # this is the function Wi+1 = Wi * (lr * dWi)
    self.w11 = self.w11 - (self._lr*dw11)
    self.w12 = self.w12 - (self._lr*dw12)
    self.w21 = self.w21 - (self._lr*dw21)
    self.w22 = self.w22 - (self._lr*dw22)
    self.b1 = self.b1 - (self._lr*db1)
    self.b2 = self.b2 - (self._lr*db2)
    self.z1 = self.z1 - (self._lr*dz1)
    self.z2 = self.z2 - (self._lr*dz2)
    self.bz = self.bz - (self._lr * dbz)

xor_train = [[0,0,0],[0,1,1],[1,1,0],[1,0,1]]
or_train = [[0,0,0],[0,1,1],[1,1,1],[1,0,1]]
and_train = [[0,0,0],[0,1,0],[1,1,0],[1,0,0]]

# you can choose the dataset to train on
data = xor_train

data_amount = len(data)

### ##### Functions ######### ############
def random_parameter(mada):
  return random.random()*mada


def sigmoid(x):
  return (1/(1+(e**-x)))

def forward(model:Model,x1,x2):
  a1 = sigmoid((x1*model.w11 + x2*model.w12) + model.b1)
  a2 = sigmoid((x1*model.w21 + x2*model.w22) + model.b2)
  y_hat = sigmoid(a1*model.z1 + a2*model.z2 + model.bz)

  return y_hat

def cost(model:Model):
  total_loss = 0
  for dr in data:
    x1 = dr[0]
    x2 = dr[1]
    y = dr[2]
    y_hat = model.forward(x1,x2)
    # print(y_hat)

    distance = (y_hat-y)**2
    total_loss += distance

  return round(total_loss/data_amount,5)


# defining the model and its random weights
random_weights = [random_parameter(1) for i in range(9)]
model = Model(random_weights[0],
                random_weights[1],
                random_weights[2],
                random_weights[3],
                random_weights[4],
                random_weights[5],
                random_weights[6],
                random_weights[7],
                random_weights[8])

### ##### main work ######### ############
def main():
  costs = []
  model._lr = 1e-1
  model._eps = 1e-2


  # print(model.model_parameters())
  # print(model.forward(0.25,10))

  epochs = 50_000

  for epoch in range(epochs):
    c = cost(model)
    costs.append(c)
    # print(c)
    model.backward(cost)
    # print(model.model_parameters())

  print(cost(model))
#   plt.plot(costs)
# also to show the loss function if needed 



main()


