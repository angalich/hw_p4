list = [1, 1, 2, 11, 2, 3, 3, 5, 4, 7, 5, 4, 7, 9]
#https://dev-gang.ru/article/metod-listcount-v-python-8w0xk6kddk/
new_list = [el for el in list if list.count(el) < 2]
print(new_list)