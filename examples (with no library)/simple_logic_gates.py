# or gates with two Ws
# very simple one neuron
import matplotlib.pyplot as plt
from math import dist
from math import e
import random
random.seed(10)

### ##### main initalize ######### ############
or_train = [[0,0,0],[0,1,1],[1,1,1],[1,0,1]]
and_train = [[0,0,0],[0,1,0],[1,1,1],[1,0,0]]
nand_train = [[0,0,1],[0,1,1],[1,1,0],[1,0,1]]
# you can choose your data set
data = or_train


costs = []

data_amount = len(data)

### ##### Functions ######### ############
def random_parameter(mada):
  return random.random()*mada


def sigmoid(x):
  return (1/(1+(e**-x)))

def cost(w1:float, w2:float, b:float):
  total_loss = 0
  for dr in data:
    x1 = dr[0]
    x2 = dr[1]
    y = dr[2]
    y_hat = sigmoid((w1 * x1 + w2 * x2) + b)

    distance = (y_hat-y)**2
    total_loss += distance

  #print(f'avrage loss is:  {total_loss/data_amount}')

  return round(total_loss/data_amount,5)


### ##### main work ######### ############
def main():

  lr = 1e-1
  eps = 1e-1
  w1 = random_parameter(1)
  w2 = random_parameter(1)
  b =  random_parameter(1)

  print(f"w1: {w1} w2: {w2} b:{b}\n")

  for epoch in range(100000):
    if epoch % 10000 == 0:
      print(f"cost: {cost(w1,w2,b)}, w1:{w1}, , w2:{w2}, b:{b}")

    c = cost(w1,w2,b)
    costs.append(c)
    dw1 = (cost(w1+eps,w2,b)-c)/eps
    dw2 = (cost(w1,w2+eps,b)-c)/eps
    db = (cost(w1,w2,b+eps)-c)/eps


    # update Ws and b
    w1 = w1 - (lr*dw1)
    w2 = w2 - (lr*dw2)
    b = b - (lr*db)



  print(f"cost: {cost(w1,w2,b)}, w1:{w1}, , w2:{w2}, b:{b}")
  print("name of the gate is:") # from the list choosed 
  print([(sigmoid(x1*w1+x2*w2+b)) for (x1,x2,y) in data])




main()

## Additional function to show the curve of the loss function
# plt.plot(costs)
# plt.show()
# it is similar 1/x (from tsoding)