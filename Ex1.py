# 1.Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
#  Пример:
# 6782 -> 23
# 0,56 -> 11

# print("Введите число")
# x=float(input())
# sum=0
# i=0
# while(x!=0):
#     i=(x%10)*10
#     sum=sum+i
#     x=x//10

a=input('Введите число: ')
a=a.replace('-',"")
a=a.replace('.','')
a=a.replace(',','')
b=list(a)
sum=0
for i in b:
    sum+=int(i) 
print(sum)
