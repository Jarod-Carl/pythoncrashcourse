import time
import random

class LCG:
        def __init__(self, seed):
            self.seed = seed
            self.modulous = 2**31 - 1
            self.multiplyer = 48271
            self.increment = 0

        def random(self):
              self.seed = self.seed * self.multiplyer
              self.seed = self.seed + self.increment
              self.seed = self.seed % self.modulous
              return self.seed / self.modulous
lcg = LCG(time.time())

for i in range(10):
    print(lcg.random())

print(random.randint(0, 9))