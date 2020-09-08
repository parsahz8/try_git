import numpy as np
import pandas as pd
import multiprocessing
from multiprocessing import Process
import os
import math
import time


def is_prime(n):
    t = True
    for i in range(int(math.floor(math.sqrt(n))) - 1):
        if n % (i + 2) == 0:
            t = False
            break
    return t


print (is_prime(88))
list_prime_1to100 = []
for i in range (1,101):
    if is_prime(i):
        list_prime_1to100.append(i)
     
