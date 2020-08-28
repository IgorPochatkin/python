#exercise 2. Перевод секунд в ЧЧ:ММ:СС
time=int(input('Введите время в секундах:'))
h=time//3600
m=time%3600//60
s=time%3600%60
rh=h//10
rm=m//10
rs=s//10
oh=h%10
om=m%10
os=s%10
texttime = "Время в формате ЧЧ:ММ:СС: {}{}:{}{}:{}{}".format(rh,oh,rm,om,rs,os)
print(texttime)



#exercise 3.Сумма последовательности n+nn+nnn...
a=int(input('Введите число:' ))
c=1
new=a
m=a
while c<a:
    c=c+1
    new=int(str(new)+str(a))
    m=m+new
print(m)



#exercise 4. Поиск наибольшей цифры из произвольного числа
n=input('Введите число: ')
c=9
x=str(c)
while x not in n:
    c=c-1
    x=str(c)
print ('Наибольшая цифра в числе: ',x)



#exercise 5. Показатели предприятия
e=int(input('Введите выручку: ')) #выручка
c=int(input('Введите затраты: '))  #затраты
r=(e-c)/e*100 #рентабельность
if e > c:
    print ('Фирма работает с прибылью: ',e-c)
    print ('Рентабельность: {:.2f} %'.format(r))
    s=int(input('Введите количество сотрудников: ')) #количество сотрудников
    print('Прибыль на одного сотрудника: {:.2f}'.format((e-c)/s))
else:
    print ('Фирма работает с убытком: ',e-c)
  
    
  
#exercise 6. Про спортсмена   
a=int(input('Введите начальный результат:'))
b=int(input('Введите дистанцию:'))
c=1
print('{}-й день: {:.2f} км'.format(c,a))
while a<b:
    c+=1
    a*=1.1
    print('{}-й день: {:.2f} км'.format(c,a))
print ('Ответ: на {}-й день спортсмен достиг результата - не менее {} км'.format(c,b))    
    
    
    