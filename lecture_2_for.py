# for

"""
for (название переменной) in (составной объект):
    твой код
"""

my_list = [11, 12, 13]

my_sum = 0
for numb in my_list:
    # my_sum = my_sum + numb
    my_sum += numb

# Полезные структуры

# Сразу пронумеровать
for index, value in enumerate(my_list):
    print(index, value)

print('=================')
# Пройтись только по индексам
for index in range(len(my_list)):
    print(index)

print('================= set')
my_set3 = {4, 5, 6, 7}
for elem in my_set3:
    print(elem)

my_dict = {
    'key': 'value',
    'key1': 'value1',
    'key2': 'value2',
}

print('for key in my_dict:')
for key in my_dict:
    print(key, my_dict[key])

# Эквивалентно предыдущему
# print('for key in my_dict.keys():')
# for key in my_dict.keys():
#     print(key, my_dict[key])

print('for value in my_dict.values():')
for value in my_dict.values():
    print(value)

print('for key, value in my_dict.items():')
for key, value in my_dict.items():
    print(key, value)

print('for tup in my_dict.items():')
for tup in my_dict.items():
    print(tup)

# ===============================================
print('# ===============================================')
text = 'as;ldkfnlkasudnfasdf'
for i, s in enumerate(text, 20):  # вторым элементом можно передать начало нумерации
    print(i, s)
    # print(sdfg, s)

# распаковка
my_tup = (1, 2, 3)
a, b, c = my_tup
print(a, b, c)