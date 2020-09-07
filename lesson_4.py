# exercise 1. Расчет зп

from sys import argv

wname = argv[1]
surname = argv[2]
whours = int(argv[3])
payperhour = int(argv[4])
bonus = int(argv[5])
salary = whours * payperhour + bonus

print(f"Сотруднику {wname}{surname} начислена зарплата {salary}")

# exercise 2. Числа больше предыдущих

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7,  1, 78, 123, 55]
print([my_list[el] for el in range(1,len(my_list)) if my_list[el]>my_list[el-1]])


# exercise 3. Числа крастные 20 и 21

print([el for el in range(20,241) if el % 20 ==0 or el % 21==0])



# exercise 4. Список неповторяющихся значений
my_list=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([el for el in my_list if my_list.count(el) == 1])


# exercise 5. Сумма четных чисел 

from functools import reduce
def my_func(prev_el,el):
    return prev_el + el
print(reduce(my_func,[el for el in range(100,1001) if el % 2 == 0]))


# exercise 6. Count и Cycle 

from itertools import count
my_list = []
for el in count(-3):
    if  el > 9:
        break
    else:
        my_list.append(el)
print(my_list)


from itertools import cycle
my_list = [3, 6, 9, 12, 15]
new_list = []
c=1
for el in cycle(my_list):
    if  c > len(my_list):
        break
    else:
        new_list.append(el)
        c+=1
print(new_list)


# exercise 7. Факториал

n=int(input('Введите число для расчета факториала: '))
def fact (n):
    m=1
    for el in range(1,n+1):
        m*=el
        yield m
for el in fact(n):
    print(el)   