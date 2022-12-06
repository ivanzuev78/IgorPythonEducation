# Базовые типы данных

# Целые числа - int
my_numb_1 = 12
my_numb_2 = 64
my_numb_3 = 3

# действия
# сложение, вычитание, умножение, деление

my_numb_4 = my_numb_1 + my_numb_2
my_numb_5 = my_numb_1 * my_numb_2
my_numb_6 = my_numb_1 / my_numb_2
my_numb_7 = my_numb_1 - my_numb_2
my_numb_8 = my_numb_1 ** my_numb_2  # Возведение в степень 5 ** 2 -> 25

# Десятичные дроби - float
my_numb_11 = 12.22
my_numb_12 = 64.98
my_numb_13 = 3.0

# Строки (текстовый тип) - str
"""
Неизменяемый тип
"""

my_str0 = 'Какой-то текст'
my_str1 = "Тоже текст"
my_str2 = "4"
perenos = '\n'  # Символ переноса строки
tab = '\t'  # символ табуляции

# действия
result_str = tab + my_str0 + perenos + my_str1

my_str3 = my_str0.replace(' ', '!!!')
print(my_str0)
print(my_str3)

# Булевый тип - bool

t = True
f = False

# Ничего - None

n = None

# Составные типы данных

# 1 Списки - list

# Создаём пустой список
my_list = []
my_list1 = list()

# Создаём непустой список
my_list2 = [1, 2, 3, 'asdd', 'aaa', 2.334, True, False, None]

# Индексация элементов происходит с 0
"""
Индексы     0  1  2    3       4      5     6     7       8
my_list2 = [1, 2, 3, 'asdd', 'aaa', 2.334, True, False, None]

"""

# Получить элемент списка
elem = my_list2[3]

one_plus_two = my_list2[1] + my_list2[2]

# Специальные методы списка
# 1 добавление в конец списка - append
print(my_list)
my_list.append(one_plus_two)
my_list.append(55)
print(my_list)

# 2 добавление на конкретное место в списке
my_list.insert(1, my_list2[3])
print(my_list)
my_list.insert(1, 12)
print(my_list)

# Кортеж - неизменяемый список - tuple

my_tuple = (1, 2, 2, 2, 2, 2, 2)
my_tuple1 = 1, 2, 3


one = my_tuple[0]

# Множества - set - набор уникальных значений
"""
Свойства:
Неупорядоченное
Данные в множестве должны быть неизменяемыми
"""

my_set = set()  # Пустое множество
my_set2 = {1, 2, 3, 4, 4, 4, 4, 5}
my_set3 = {4, 5, 6, 7}
my_set3.add(10)  # Добавление объекта в множество
my_set3.add(my_tuple1)
print(my_set2 & my_set3)
print(my_set2 - my_set3)
print(my_set3 - my_set2)
print(my_set3 | my_set2)
print(my_set3)


# Словари - dict (хеш таблица, мап таблица, маппинг)
"""
Ключом могут быть только неизменяемые типы данных: int, str, float, tuple, bool
Ключами не могут быть: list, set, dict
Ключи всегда уникальные
Значения могут быть любыми типами

Свойства:
Неупорядоченный
"""
my_dict = {}  # Пустой словарь
my_dict1 = {'key': 'value', 1: 42, '1': 1}

# Как достать данные из словаря

elem_dict = my_dict1['key']
print(my_dict1['key'])
print(my_dict1[1])
print(my_dict1['1'])

man1 = {
    'Рост': 182,
    'Вес': 80,
}
man2 = {
    'Рост': 178,
    'Вес': 98
}
man3 = {
    'Рост': 187,
    'Вес': 67
}

print('Вес человека', man1['Вес'])

# Добавление или перезапись значений словаря

print(man1)
man1['Длина рук'] = 81
print(man1)
man1['Вес'] = 55
print(man1)


# Небольшое дз: в каждый словарь добавить ключ "Индекс массы тела" - соответствующее ему значение
# Контрольный пример
m = 80
h = 200
imt = 20.0
imt_your = ...
print('imt_your', imt_your)