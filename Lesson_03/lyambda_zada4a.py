# В файле хранятся числа, нужно выбирать четные и составить список пар (число; квадрат числа).
# пример:         12345   (2,4) (4,16)
# path = 'file_name.txt'
# with open("file_name.txt") as s:
#     list = s.readlines()
#
#
# def f(x):
#     return int(x ** 2)
#
#
# newlist = [[(int(i), f(i)) for int(i) in list if int(i) % 2 == 0]]
# print(newlist)


path = 'file_name.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos + 1:]

out = []
for i in numbers:
    if i % 2 == 0:
        if not i % 2:
            out.append((i, i ** 2))

print(out)
