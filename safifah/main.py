
from matrix_op import *

# simple examples for the library safifah 
# sf1 = Safifah(2,2)
# fill(sf1,10)
# idn_sf = [1,0,0,1]

# sf2 = Safifah(2,2)

# sf2.masfofah = idn_sf

# print_safifah(sf2)

# sf3 = Safifah(2,2)

# dot(sf3, sf1, sf2)

# print_safifah(sf3)

### Building XOR example
x = Safifah(1,2)
x.change_at(0,0,0) 
x.change_at(0,1,1)

w1 = Safifah(2,2)
b1 = Safifah(1,2)

a1 = Safifah(1,2)

w2 = Safifah(2,1)
b2 = Safifah(1,1) 
a2 = Safifah(1,1) # a*w2 + b2 
# randomize the weights

random_safifah_bound(w1,5,10)
random_safifah_bound(b1,5,10)
random_safifah_bound(w2,5,10)
random_safifah_bound(b2,5,10)

# print("----------")
# print_safifah(w1,"w1")
# print("----------")
# print_safifah(b1,"b1")
# print("----------")
# print_safifah(w2,"w2")
# print("----------")
# print_safifah(b2,"b2")

# forwading 

dot(a1,w1,x)
add(a1,b1)
sigmoid_saf(a1)

dot(a2,a1,w2)
add(a2,b2)
sigmoid_saf(a2)

# to get y 
y = a2.derefrence()

