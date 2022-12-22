# a - открытие для добавления данных
# r - открытие для чтения данных
# w  открытие для записи данных
# w+, r+

# with open('file.txt', 'w') as data:
#     data.write('line 111\n')
#     data.write('line 1222\n')


# colors = [ 'red', 'green', 'blue123']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.write('LINE 121\n')
# data.write('LINE 131\n')
# data.close()



# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
#
# exit()
def f(x):
    if x ==1:
        return 'Целое'
    elif x==2.3:
        return '23'
    else:
        return