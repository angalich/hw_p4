from itertools import count
from itertools import cycle

for el in count(9):
    print(el)

list = ['name', 123, None]
for el in cycle(list):
    print(el)