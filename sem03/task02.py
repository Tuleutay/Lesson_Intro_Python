# 2)Орел и решка
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла,
# а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.
# Примечание. Если выпавших Решек нет, то необходимо вывести число
# Тестовые данные
# Sample Input 1:
# ОРРОРОРООРРРО
# Sample Output 1:
# 3
# Sample Input 2:
# ООООООРРРОРОРРРРРРР
# Sample Output 2:
# 7
# Sample Input 3:
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
# Sample Output 3:
# 31

stroka = "OPOPPPPOPOPOPPPOPPOPPPOPOPPPPPPOPO"
# a = stroka.split('O')
# print(a)
# max = 1
# for i in range(len(a)):
#     b = len(str(a[i]))
#     if b > max:
#         max = b
# print(max)

# 2 rewenie

# find1 = "P"
# while stroka.count(find1) > 0:
#     count = len(find1)
#     find1 += 'P'
# print(cout)
# 3 rewenie
#
s = input()
t = 0
while "P" * (t + 1) in s:
    t += 1
print(t)
