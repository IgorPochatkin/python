#exercise #1 Разные типы

newlist = ['spring',2, False, 3.141593]
for eltype in newlist:
    print(eltype,type(eltype))
    
#exercise #2 Поменять местам

my_list = [int(a) for a in input('Значения через пробел, по oкончании ввода нажмите Enter').split()]
for el in range(0,len(my_list)-1,2):
    my_list[el],my_list[el+1] = my_list[el+1],my_list[el]
print(my_list)
    
    
#exercise #3 Времена года

monthnumb = int(input('Input number between 1 and 12: '))
calendar = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 
            5: "spring", 6: "summer", 7: "summer", 8: "summer", 
            9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}
print('season:', calendar.get(monthnumb))


monthnumb = int(input('Input number between 1 and 12: '))
calendar = ["winter","winter","spring","spring", 
            "spring", "summer", "summer", "summer", 
            "autumn", "autumn", "autumn", "winter"]
print('season:',calendar[monthnumb-1])

#exercise #4 Деление текста

my_text=input('Input text with space: ')
my_text=list(my_text.split())
for ind, el in enumerate(my_text, 1):
    print(ind, el[:10])
  
    
#exercise #5 Рейтинг
   
my_num= int(input('Insert number: '))
my_list = list([7, 5, 4, 3, 3, 1])
for  el in my_list:
    if my_num == el:
        continue
    elif my_num > el:
        my_list.insert(my_list.index(el),my_num)
        break
    elif my_num <= min(my_list):
        my_list.append(my_num)
        break
print(my_list)    
    
#exercise #6 Словарь 

while True:
        qty = int(input("Какое кол-во позиций вы хотите добавить:"))
        if qty > 0:
            break
catalog = {"наименование": [], "цена": [], "кол-во": [], "ед.измерения": []}
for el in range(qty):
    for catkey in catalog.keys():
        if catkey == "цена" or catkey == "кол-во":
            catvalue = int(input(f"Введите {catkey}\n"))
        else:
            catvalue = input(f"Введите {catkey}\n")        
        catalog[catkey].append(catvalue)
print(catalog)
newcatalog = []
for el in range(qty):
    catalog2 = dict({"наименование": input(f"наименование\n"), 
                     "цена": int(input(f"цена\n")), 
                     "кол-во": int(input(f"кол-во\n")), 
                     "ед.измерения": input(f"ед.измерения\n")})
    newcatalog.append((el+1, catalog2))
print(newcatalog) 
    

def ext_func(var_1):
    def int_func(var_2, var_3):
        return var_1 + var_2 +var_3
    return int_func

f_obj = ext_func(200) # f_obj - функция
print(f_obj(300))  







     