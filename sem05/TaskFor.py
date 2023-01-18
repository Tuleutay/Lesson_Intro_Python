# 4.Саша и Галя коллекционируют монетки. Каждый из них решил записать номиналы монеток из своей коллекции.
# Получилось два списка. Эти списки поступают на вход программы в виде двух строк из целых чисел,
# записанных через пробел. Необходимо выделить значения, присутствующие в обоих списках и оставить среди
# них только четные. Результат вывести на экран в виде строки полученных чисел в порядке их возрастания через пробел.
# При реализации программы используйте функцию filter и кое-что еще (для упрощения программы), подумайте что.

sasha = list(map(int, input().split()))
galya = list(map(int, input().split()))
new_list = list(filter(lambda x: (x % 2 == 0), (list(set(sasha) and set(galya)))))
print(sorted(new_list))