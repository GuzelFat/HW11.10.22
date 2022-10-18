# 4. Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Найдите произведение элементов 
# на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.

from itertools import product
import random
N=int(input('Задайте количество элементов в списке: '))
file=open("file.txt",'w')
file.write(str(random.randint(0,N-1)))
file.write('\n')
file.write(str(random.randint(0,N-1)))
file.write('\n')
file.write(str(random.randint(0,N-1)))
file.write('\n')
file.close()
s=[]
for i in range(1,N+1):
    s.append(random.randint(-N,N))
print (f'Список из {N} элементов,заполненных числами из промежутка[{-N},{N}]:{s} ')
print()

file=open('file.txt','r')
product=1
print('Содержание файла')
for i in file:
    print (i,end= "")
    product*=s[int (i)]
file.close()
print()
print(f'Произведение заданных элементов = {product}')



