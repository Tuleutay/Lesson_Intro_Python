# Преобразовать набор списков

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 24, 7]
salary = [111, 222, 333]

a, b, c = list(zip(users, ids, salary))
print(a, b, c, sep='\n')
a, b, c = map(list, zip(a, b, c))
print(a, b, c, sep='\n')
