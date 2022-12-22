#print('Hello World, it is me')
#value = None
#print(type(value))
#a = 123
#b = 1.23
#print(type(a))
#print(type(b))
#value = 123421
#print(type(value))
#s = 'hello world'
#print(s)
#print(a, b, s)
#print(a, ' - ' ,b, ' - ',s)
#print(f'{a} - {b} - {s}')
#print('{1} - {2} - {0}'.format(a, b, s))

#f = True
#print(f)

#list = ['1', '2', '3']
#col = ['hello', 1, 2, 4.5, True]
#print(list)
#print(col)

#print('введите число а')
#a = int(input())
#print('введите число b')
#b = int(input())
#print(a, ' + ' , b, ' = ', a+b)

# a = 12
# b = 5
# #c=a//b =2 сколько раз поделили целая часть
# #c=a%b =2 остаток от деления
# c=a**b #возведение в степень
# print(c)

# d=1.3123545487
# e=9
# g=round(d*e,7) математическое округление
# print(g)


#__________________________________________________________________________________________________
# Логические опреции

# >, >=, <, <=, ==, !=
# not, and, or - не путать с &,|,^
# Кое-что еще: is, is not, in, not in, gen


#a= 1<4 and 5>2             
#print(a)
  
#a= 'qwe'
#b= 'qwe'
#print(a==b)

#a=[1,2,3]
#b=[1,2,5]
#print(a==b)

#print(func<T>(x))

#f = [1,2,3,4]
#print(f)
#print( not 2 in f)

#is_odd = not f[0] % 2
#print(is_odd)
#___________________________________________________________________

# Управляющие конструкции
# if, if-else

# a = int(input('a = ')) 
# b = int(input('b = ')) 
# if a>b:
#     print(a)
# else:
#     print(b)

# username = input(' Введите имя: ')
# if username == 'Маша':
#     print('Ура!, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Медина':
#     print('Мир тебе сестра, Медина')
# else:
#     print('Привет, ', username)

#___________________________________________________________________
# Управляющие конструкции
# ЦИКЛ while 

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10  + (original % 10)
#     original //=10
#     print(original)
# else:
#     print('пожалуй')
#     print('хватит')
# print(inverted)


# ЦИКЛ for

#for i in 1,2,3,4,5,6:
#    print(i**2)
 
#list = [1,2,3,10,5]
#for i in list:
#    print(i)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(1, 10, 2):
#     print(i)
# 
# for i in 'qwerty':
#     print(i)

#text = 'Съешь еще эти жирные сладкие булки'
## 
#print(len(text))                        # 39
#print('еще' in text)                    # true
#print(text.isdigit())                   # false
#print(text.islower())                   #   true
#print(text.replace('еще', 'ЕЩЁ'))       #   #

#for c in text:
#    print(c)#

#print (text[0])                         # c
#print(text[len(text)-1])                # k
#print(text[-5])                         # б
#print(text[:])                          # print(text)
#print(text[len(text)-2:])               # ки
#print(text[6:-18])                      # еще эти жи
#print(text[0:len(text):6])              # сеиыду
#print(text[::6])                        # сеиыду


#_____________________________________________________
#Списки введение

#numbers = [1, 2, 3, 4, 5]
#print(numbers)                          # [1, 2, 3, 4, 5]
#ran=range(1,6)
#print(type(ran))
#numbers = list(ran)
#print(type(numbers))
#
#numbers[0] = 10
#print(f'{len(numbers)} len')            # 5 len
#print(numbers)                          # [10, 2, 3, 4, 5]
#for i in numbers:
#    i*=2
#    print(i)                            #[20, 4, 6, 8, 10]
#print(numbers)                          # [10, 2, 3, 4, 5]

# colors.append('gray')       # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # true
# colors.remove('red') # del colors[0] # удалить элемент

# ФУНКЦИИ______________________________________________________
def f(x):
    if x ==1:
        return 'Целое'
    elif x==2.3:
        return '23'
    else:
        return

arg=1.3
print(f(arg))
print(type(f(arg)))






