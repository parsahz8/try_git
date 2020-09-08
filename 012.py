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
s