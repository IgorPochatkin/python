#exercise 1. Деление двух чисел
def func1(a,b):
        try:
            a/b
        except Exception as e:
            print('Ошибка! Деление на 0', e)
        else:    
            return a/b        
print(func1(int(input('Введите число a: ')), int(input('Введите число b: '))))

#exercise 2. Информация о человеке

def my_func(name, surname, year, city, email, phone):
    datainfo = name + " " + surname + ",  год рождения: "+ str(year) + ", город: " + city + "; почта: " + email + " ; телефон: " + str(phone)
    return datainfo
while True:
        try:
            new_name = input("Введите имя: ")
            new_surname = input("Введите фамилию: ")
            new_year = int(input("Год рождения: "))
            new_email = input("Email: ")
            new_city = input("Город: ")
            new_phone = int(input("Телефон: "))
            break
        except ValueError as E:
            print("Ошибка ввода!", E) 
print(my_func(name=new_name, surname=new_surname, year=new_year, city=new_city,email=new_email, phone=new_phone))

#exercise 3. Сумма 2х наибольших чисел
def func2(a,b,c):
    return a+b+c-min(a,b,c)
print(func2(1,2,3))


#exercise 4. Возведение  в степень
def my_func(x, y):
    mult = 1
    for el in range(abs(y)):
        mult *= x
    if y >= 0:
        return mult
    else:
        return 1 / mult
print(my_func(float(input('Введите число x: ')), int(input('Введите число y: '))))


def my_func(x, y):
    if y>=0:
        return x**y
    else:
        return 1/(x**y)
print(my_func(float(input('Введите число x: ')), int(input('Введите число y: '))))

#exercise 5. Сумма чисел

result =[]
while True:
    try:  
        intdata = input('Введите числа через пробел, введиту E для выхода: ')
        dat1 = intdata.split(" ")
        if 'E' in dat1:
            dat1.pop(len(dat1)-1)
            for el in range(len(dat1)):
                dat1[el] = int(dat1[el])
            sum1 = sum(dat1)
            result.append(sum1)
            break
        else:
            for el in range(len(dat1)):
                dat1[el] = int(dat1[el])
            sum1 = sum(dat1)
            result.append(sum1)
            print('Промежуточная сумма чисел: ',sum(result))  
    except Exception as error1:
        print("Ошибка данных", error1)
        break
print('Итоговая сумма: ',sum(result))
    
#exercise 6. Заглавные буквы.
def int_func(x):
    return x.title()
print(int_func('happy new year'))




