"""
Создать список из нечётных целых чисел от 1 до N
Несколько решений:
1) С использованием range
2) C помощью цикла for
"""

n = 15
x = []
for i in range(1, n, 2):
    x.append(i)
print(x)
