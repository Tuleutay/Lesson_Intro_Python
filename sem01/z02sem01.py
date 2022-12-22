# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них. Примеры:
# 1, 4, 8, 7, 5 -> 8

a = [0] * 5
for i in range(len(a)):
    i = str(i)
    print(f'Введите ',i+1, ' элемент массива ')
    i = int(i)
    a[i] = int(input())
print(a)   
min = a[0]
max = a[0]

for i in range(len(a)):
    if (a[i ]< min):
        min = a[i]   
    if (a[i] > max):
        max = a[i]        
min = str(min)
max = str(max)

print("Минимальное значение = " + min)
print("Максимальное значение = " + max)