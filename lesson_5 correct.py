# exercise 1. Создать файл и добавить данные

with open("new_file.txt", "w") as fil1:
    while True:
        newtext = input('Введите текст: ')
        if newtext !="":
            fil1.write(newtext+'\n')
        else:
            break
        

# exercise 2. Подсчет количества строк


my_file = open('strcount.txt','r')
n=0
while True:
    content = my_file.readlines()
    for item in content:
        n=n+1
        print(f'длина {n}-й строки составляет: {len(item.split())} слов')
    if not content:
        break
print(f'общее количество строк: {n}')

# exercise 3. Зарплаты сотрудников

 
salary_list = []
with open("salary.txt", "r") as sal1:
    for line in sal1:
        name, salary = line.split()
        if int(salary) < 20000:
            print(f'меньше 20000 получает {name}')
        salary_list.append(int(salary))
        avg_salary = sum(salary_list)/len(salary_list)
print(f'средняя ЗП составляет {avg_salary}') 
    
    
# exercise 4. Замена числительных

            
num_rus = ['Один', 'Два', 'Три', 'Четыре']
new_line = []           
lines = [line.strip() for line in open('numbs.txt')]
for el in lines:
    x=el.split()
    x.pop(0)
    x.insert(0, num_rus[lines.index(el)])
    full_data = ' '.join(x)
    out_f = open("file4.txt", "a")
    out_f.write(full_data +'\n')
    out_f.close()
print('Новый файл file4.txt готов')            

# exercise 5. Сумма чисел 


my_file = open('new_file2.txt','w')
my_file.write(input('Введите слагаемые цифры через пробел: '))
my_file.close()
my_file = open('new_file2.txt','r')
content = my_file.readline()
content_list = (content.split())
result = [int(el) for el in content_list]
print(sum(result))


# exercise 6. Рапсисание

schedule_dict = {}
with open("schedule.txt", "r") as sch1:
    for line in sch1:
        subject, coma, lection, practice, lab = line.split()
        lec= lection.replace('(л)','').replace('-','0')
        pra =practice.replace('(пр)','').replace('-','0')
        lab =lab.replace('(лаб)','').replace('-','0')
        total =  int(lec) + int(pra) + int(lab)
        schedule_dict[f"{subject}"] = f"{total}"
print(schedule_dict)
        

# exercise 7. Компании


import json
avg_profit = []
result = []
avg_dict = {}
profit_dict = {}
with open("companies.txt", "r") as comp1:
    for line in comp1:
        name, llc, revenue, expenses = line.split()
        profit = int(revenue) - int(expenses)
        if profit >= 0:
            avg_profit.append(profit)
        profit_dict[f"{name}"] = f"{profit}"
    result.append(dict_profit)
    avg_dict["avg_profit"] = sum(avg_profit)/len(avg_profit)
    result.append(avg_dict)
    print(result)

with open("companies.json", "w") as compjs:
    json.dump(result, compjs)


