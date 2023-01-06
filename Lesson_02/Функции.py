# import Les01 as h
#
# print(h.f(1))

# def new_string(symbol, count=3):
#     return symbol * count
#
# print(new_string('!', 5)) # !!!!!
# print(new_string('!'))    # !!!
# print(new_string(4))      # 12

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
#
#
# print(concatenatio('a', 'b', 'i', 'k', 'e'))  # abike
# print(concatenatio('a', '1'))  # a1

# def concatenatioint(*params):
#     res: int = 0
#     for item in params:
#         res += item
#     return res
#
# print(concatenatioint(1, 2, 3, 45))   # 51
#
#
# ########## RECURSION
#
# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# list = []
# for e in range (1,10):
#     list.append((fib(e)))
# print(list)                 # [1, 1, 2, 3, 5, 8, 13, 21, 34]


##############  К О Р Т Е Ж И - это неизменяемые списки

# a = (3, 1, 41, 4)
# print(a)        # (3, 1, 41, 4)
# print(a[0])     # 3
# print(a[-2])    # 41
# for item in a:
#     print(item)
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
####   r:red g:green b:blue
####### СЛОВАРИ - это неупорядоченные коллекциии
# произвольных объектов с доступом по ключу

# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary)  # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# dictionary['left'] = 'vlevo'
# print(dictionary['left'])
# # print(dictionary['left'])  # ←
# # типы ключей могут отличаться
#
# del dictionary['left']        # yдаление элемента
# for k in dictionary.keys():
#     print(k)                ### up left down right

# for v in dictionary.values():
#     print(v)                    ### ← ↑ ← ↓ →
# for v in dictionary:  ### up left down right
#     print(v)

# for v in dictionary:                ### ← ↑ ← ↓ →
#     print(dictionary[v])

# for item in dictionary:
#   print('{}: {}'.format(item, dictionary[item]))
#         up: ↑,
#         left: ←,
#         down: ↓,
#         right: →

###########  МНОЖЕСТВА
#
# colors = {'black', 'green', 'blue123'}
# print(colors)  # {'blue123', 'green', 'black'}
# colors.add('red')
# print(colors)  # {'red', 'blue123', 'green', 'black'}
# colors.add('grey')
# print(colors)  # {'black', 'grey', 'blue123', 'green', 'red'}
# colors.remove('red')
# print(colors)  # {'blue123', 'grey', 'black', 'green'}
# # colors.discard('red')
# # print(colors)  ## {'blue123', 'grey', 'black', 'green'}
# # colors.clear()
# # print(colors)  # set()
#
# a = {1, 2, 3, 5, 8}
# b = {2, 4, 5, 6, 9, 12}
# c = a.copy()  # c = {1, 2, 3, 5, 8}
# u = a.union(b)  # u = {1, 2, 3, 4, 5, 6, 8, 9, 12}
# i = a.intersection(b)  # i = {2, 5}
# dl = a.difference(b)  # dl = { 1, 3, 8}
# dr = b.difference(a)  # dr = { 4, 6, 9, 12}
#
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))  # {1, 3, 4, 6, 8, 9, 12}
# print(q)
#
# s = frozenset(a)  # - не изменяемое множество
# print(a)

########### СПИСКИ

list1 = [1, 12, 3, 4, 5]
list2 = list1
#
list1[0] = 354
list2[1] = 777
# for e in list1:
#     print(e)
#
# print()
#
# for e in list2:
#     print(e)

# list1 = [1,2,3,4,5]

# print(len(list1))
# print(list1.pop())
# print(len(list1))
# print(list1)
# print(list1.pop())
# print(list1)
# # print(list1)  # [1, 2, 3, 4]
# # print(list1.pop(2))
# # print(list1)            # [1, 2, 4, 5]
# print(list1.insert(2,11))  # Добавление элемента после элемента 2
# print(list1)                # [1, 2, 11, 3, 4, 5]
# print(list1.append(97))           # Добавление элемента в конец
# print(list1)                # [1, 2, 11, 3, 4, 5, 97]
