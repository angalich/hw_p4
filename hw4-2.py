list = [20, 12, 2, 3, 1, 4, 7, 9, 12, 14, 20, 21]
new_list = [el for i, el in enumerate(list) if list[i - 1] < list[i]]
print(f'Исходный список {list}')
print(f'Новый список {new_list}')