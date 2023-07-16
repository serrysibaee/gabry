from math import dist
# very simple one neuron
import random
data = [[0,0],[1,2],[2,4],[3,6],[4,8]]
data_amount = len(data)
random.seed(10)

def random_parameter(mada):
  return random.random() * mada


def cost(w:float, b:float):
  total_loss = 0
  for dr in data:
    x = dr[0]
    y = dr[1]
    y_hat = w * x + b

    distance = (y_hat-y)**2
    total_loss += distance
    #print(f"x:  {x},y_hat:{y_hat},\t y:{y} \n")

  #print(f'avrage loss is:  {total_loss/data_amount}')

  return round(total_loss/data_amount,5)

def main():
  lr = 1e-4
  eps = 0.0001

  w = round(random_parameter(3),5)
  b = round(random_parameter(1),5)

  print(f"w: {w}\n")

  for epoch in range(3000):
    if epoch % 100 == 0:
      print(f"cost: {cost(w,b)}, w:{w}, , b:{b}")

    dw = (cost(w+eps,b)-cost(w,b))/eps
    db = (cost(w,b+eps)-cost(w,b))/eps
    #print(f"dw: {dw}")
    # w -= dw
    # updating w from the drev
    w = w - (lr*dw)
    b = b - (lr*db)


main()