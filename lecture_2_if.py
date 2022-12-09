
"""

if (условие 1):
    Код, который выполняется, если условие 1 истина

elif (условие 2):
    Код, который выполняется, если условие 1 ложь, а условие 2 истина

elif (условие 3):
    Код, который выполняется, если условия 1 и 2 ложь, а условие 3 истина

else:
    Код, который выполняется, если все предыдущие условия ложны


"""

# bool

# Логическое И - and
"""
    a       b
    True    True    ->  True
    True    False   ->  False
    False   True    ->  False
    False   False   ->  False

"""
a = False
b = True
c = False
result = a and b


# Логическое ИЛИ - or
"""
    a       b
    True    True    ->  True
    True    False   ->  True
    False   True    ->  True
    False   False   ->  False
"""


# Логическое отрицание - not
"""
not True -> False
not False -> True


    a       b       not (a and b)
    True    True    ->  False
    True    False   ->  True
    False   True    ->  True
    False   False   ->  True



    a       b       not (a or b)
    True    True    ->  False
    True    False   ->  False
    False   True    ->  False
    False   False   ->  True

"""


if 5 < a < 8:
    print('5 < a < 8')
elif a > 10 or a < 5:
    print('a > 10 or a < 5')

"""
больше >
Меньше <
Равно ==
больше или Равно >=
Меньше или Равно <=
Не равно !=
"""


"""
Приведение различных типов к bool (True или False)
1. Объект составной (list, set, tuple, dict, str)
    Если объект пустой, то он False
    Иначе он True
    
2. int, float 
    0 - False
    Все остальные числа - True

3. None -> False
"""

my_list = None
print(bool(my_list))
if my_list:
    print('True', my_list)
else:
    print('False', my_list)

"""
Как работает and и or под капотом

my_list or default_list

как работает and
my_list and default_list

"""
default_list = []

print(my_list or default_list)

