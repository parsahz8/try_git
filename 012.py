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

def list_Prime(n1,n2):   
    list_prime = []
    for i in range (n1,n2):
        if is_prime(i):
            list_prime.append(i)
    return list_prime

