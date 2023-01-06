# a - открытие для добавления данных
# r - открытие для чтения данных
# w  открытие для записи данных
# w+, r+

# with open('file.txt', 'a') as data:
#     data.write('line 1991\n')
#     data.write('line 333\n')

# colors = ['red', 'green', '22blue']  # Работа с файлом
# data = open('file.txt', 'a')
# # data.writelines(colors)  # разделителей не будет
# data.write('LINE 121\n')
# data.write('LINE 598\n')
# data.close()

# path = 'file.txt'  # СЧИТЫВАНИЕ С ФАЙЛА
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
#
# exit()

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return '23'
    else:
        return
