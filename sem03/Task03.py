# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие
# последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы
# Формат входных данных
# В первой строке подаётся число
# n
# n – количество холодильников. В последующих
# n
# n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от
# 5
# 5 до
# 100
# 100 символов.
# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.
# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3
# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8
# def check(user_string):
#     find_str = 'anton'
#     j = 0
#     count = 0
#     for i in find_str:
#         while j < len(user_string):
#             if i == user_string[j]:
#                 count += 1
#                 break
#             else:
#                 j += 1
#     if count == 5:
#         print(f'{user_string} заражен')
#     else:
#         print(f'{user_string} не заражен')
#
#
# test_str1 = '2a5dn8t78o9n0'
# test_str2 = '2naf5dncbvs8t7v8o90n'
# test_str3 = 'kamila'
# test_str4 = 'nw5og5au68itpipun'
# check(test_str1)
# check(test_str2)
# check(test_str3)
# check(test_str4)


##### 2 rewenie


anton = 'anton'
n = 7
list = ['24a897nggdst998on', '2naf5dncbvs8t7v8o90n', 'elantofj4hfje3o3ndsa', 'asfnotxa23csyta', 'nw5og5au68itpipun',
        '87rfdsa7qfwyctna', 'annat67oant52odhdavan']
find = []

for i in range(n):
    count = 0
    for j in range(len(list[i])):
        if anton[count] == list[i][j]:
            count += 1
        if count == 5:
            find.append(i + 1)
            count = 0
            break

print(find)
