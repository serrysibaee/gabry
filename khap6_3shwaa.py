
# this library is to make random numbers from scratch
# يجب استخدام الوقت وغيره من المتغيرات حتى نستطيع عمل أرقام عشوائية في بايثون
import time
import os 
# we will not use random libraries

now_time = time.time()

print(now_time.as_integer_ratio())

def extract_randint(data):
    # genrate random numbers (0,1]
    str_data = str(data)
    numbers = [i for i in str_data if i != "0"]
    return int(numbers[-1])/9.0


# MAX_INT = 10_000_000
# for i in range(10):
#     rand_int = extract_randint(time.time_ns())
#     print(rand_int)
#     # print(time.clock())


# using Linear Congruential Generator
# source: https://levelup.gitconnected.com/how-do-computers-generate-random-numbers-a72be65877f6 

# use time steps to take seeds 
# the loop will take about 10-steps 
# modulo is مقاس أو متبقي 


def generator(seed:int):
    # Xn+1 = (aXn + c)%m
    # Xn is seed 
    # 0 <= a < m 
    # 0 <= c < m
    # m from choice
    # choose time to get m,c,a   
    Xn = seed
    a = 100
    m = 10_000_000
    c = 40

    number = 0

    for _ in range(1000):
        number = (a*Xn + c)%m
        print(number)
        Xn = number

    return number

print(generator(10000))
