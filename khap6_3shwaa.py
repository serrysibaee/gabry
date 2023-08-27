
# this library is to make random numbers from scratch
# يجب استخدام الوقت وغيره من المتغيرات حتى نستطيع عمل أرقام عشوائية في بايثون
import time

# using Linear Congruential Generator
# source: https://levelup.gitconnected.com/how-do-computers-generate-random-numbers-a72be65877f6 

# use time steps to take seeds 
# the loop will take about 10-steps 
# modulo is مقاس أو متبقي 


class Generator:

    def seeder(self):
        seeder = time.time_ns()
        seed = seeder % 10000
        return seed
    
    def __init__(self, seed=0, a=1664525, c=1013904223 ,m=2**32):
        # for useful porposes I will use the current time as a seed 
        self.seed = self.seeder()
        self.a = a
        self.c = c
        self.m = m
    
 
    
    def random_norm(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed / self.m
    
    def random_int(self, integer=10):
      return int(self.random_norm() * integer)