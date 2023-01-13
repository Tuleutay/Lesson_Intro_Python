# def select(f, col):
#     return [f(x) for x in col]
#
#
# def where(f, col):
#     return [x for x in col if f(x)]


#
#
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x ** 2), res)
# print(res)

# --------------------------- Модифицируем код при помощи мэп map select filter

# data = '1 2 3 5 8 15 23 38'.split()
#
# res = map(int, data)
# res = list(filter(lambda x: not x % 2, res))
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)
# -------------------------------------------------- filtr function
# data = [x for x in range(10)]
#
# res = list(filter(lambda x: not x % 2, data))
# print(res)

# data = list(map(int, input().split()))     # ввод списка
# print(data)

# data = map(int, input().split())
#
# for e in data:
#     print(e)

# data = list(map(int, '15 23 38'.split()))
#
# for e in data:
#     print(e * 2)
#
# print('----')
#
# for e in data:
#     print(e)

# ---------------------------- ZIP function
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 6, 7, 8]
# salary = [111, 22, 333]
#
# data = list(zip(users, ids, salary))
# print(data)

# ------------------ enumerate() function
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 6, 7, 8]
salary = [111, 22, 333]

data = list(enumerate(users))
print(data)
 ито
