# Дан список, вывести отдельно буквы и цифры.

a = ("s", "b", "2", "c", "-5")

# numbers = list(i for i in a if int(i).isnumeric()))
# print(numbers)
# c = [item for item in a if item not in numbers]
# print(c)

# 2 rewenie
# num_list = []
# char_list = []
#
# for i in a:  # обработка исключений
#     try:
#         int(i)
#         num_list.append(i)
#     except:
#         char_list.append(i)
#
# print(num_list)
# print(char_list)

# 3 rewenie

b = filter(str.isalpha, a)
c = filter(str.isdigit, a)
print(*b)  # s b c
print(*c)  # 2  (-5) ne rabotaet
