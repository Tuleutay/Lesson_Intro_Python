# a - открытие для добавления данных
# r - открытие для чтения данных
# w  открытие для записи данных
# w+, r+

colors = [ 'red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors) # разделителей не будет
data.close()


exit()
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

