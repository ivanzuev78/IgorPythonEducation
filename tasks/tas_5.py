from random import randint

num = 0
finish = int(input())

while num != finish:
    r = randint(0, 5)
    if num > finish:
        num -= r
    else:
        num += r
        continue
    print(num, r)

# l = []
# for _ in range(10):
#     l.append(randint(0, 100))