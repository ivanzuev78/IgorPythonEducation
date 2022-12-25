"""
Дан список строк.
Получить из них текст, который соединен через:
1) Пробел
2) Точку

Несколько решений:
1) С использованием .join
2) С использованием цикла for
"""

list_1 = ['Мама', 'мыла', 'рыбу', 'неизвестно', 'зачем']

text = ''
text_2 = ''
for word in list_1:
    text += word + ' '
    text_2 += word + '.'

print(text)
print(text_2)

text_3 = ' '.join(list_1)
print(text_3)

text_3 = '.'.join(list_1)
print(text_3)
