# 3. Задайте список из n чисел последовательности 
# (1+1/n)n и выведите на экран их сумму
#  Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} 
# Сумма 9.06

n= int(input('Введите число n: '))
dict={}
sum=0
for i in range(1,n+1):
    # dict[i]=(1+1/i)*i
    # s=s+dict[i]
    dict[i]=round((1+1/i)**i,2)
    sum+=dict[i]
print(dict)
# print("Сумма =", s)
print(round(sum,2))








# print( f'Введите чило :')
# n=int (input())
# d={a:((1+1/a)/a)for a in range(1,n+1)}
# print(d)