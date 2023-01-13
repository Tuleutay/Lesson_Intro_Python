# def f(x):
# #     return x ** 2
# #
# #
# # g = f
# # print(type(f))  # <class 'function'>
# # print(type(g))  # <class 'function'>
# # print(f(2))
# # print(g(4))

######################################

# def calc(x):
#     return x + 10
#
#
# # print(calc(10))
# def calc1(y):
#     return y * 10
#
#
# # print(calc1(10))
# def math(op, x):
#     print(op(x))
#
#
# math(calc1, 10)
# math(calc, 10)

####################################################
# def sum(x, y):
#     return x + y


# sum = lambda x, y: x + y
#
#
# def mylt(x, y):
#     return x * y
#
#
# def calc(op, a, b):
#     print(op(a, b))
#
#
# calc(lambda x, y: x + y, 4, 5)

#######################     LIST COMPREHENSION СПИСКИ
# [exp for item in iterable] СОЗДАНИЕ СПИСКА
# [exp for item in iterable (if conditional)] ВЫБОРКА ИЗ СПИСКА
# [ex[ <if conditional> for item in iterable (if conditional)]

# list = []
# for i in range(101):
#     #if (i % 2 == 0):
#         list.append(i);

# print(list)

# list = [(i, i) for i in range(1, 21) if i % 2 == 0]
#
# print(list)

def f(x):
    return x ** 3


list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]

print(list)
