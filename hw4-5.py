from functools import reduce


#https://pythonz.net/references/named/functools.reduce/
def reducer_func(el_prev, el):
    return el_prev * el


elem_list = [el for el in range(99, 1001)]
new_list = [el for el in range(99, 1001) if el % 2 == 0]

print(new_list)
print(reduce(reducer_func, elem_list))
