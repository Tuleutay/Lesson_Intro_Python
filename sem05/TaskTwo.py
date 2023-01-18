# Объявите анонимную ЛЯМБДУ функцию для определения в переданную ей строку фрагмента "plr".
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False если отсутствует.

stroka = input()

# def find(str):
#     if str.count('plr') > 0:
#         return True
#     else:
#         return False
#
# find(stroka)

s = lambda findInStr: "plr" in stroka
print(s(stroka))
