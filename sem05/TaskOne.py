# расчитать нод двух чисел(быстрый и медленный способ)
a = int(input('введите число '))
b = int(input('введите число '))


def f(x, y):
    for i in range(x, 0, -1):
        if (x % i == 0) and (y % i == 0):
            return i


if a < b:
    temp = a
    a = b
    b = temp

print(f(a, b))

print()

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(a)

print()
while a != b:
    if a > b:
        a = a / b
    else:
        b = b / a
print(a)

# 15|29
# 15|14
# 01|13
