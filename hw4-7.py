from itertools import count
from math import factorial


def fibo_gen():
    for i in count(1):
        yield factorial(i)


for el in fibo_gen():
    if el < 15:
        print(el)
        el += 1
    else:
        break
