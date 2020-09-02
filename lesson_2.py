#exercise #1 Разные типы

newlist = ['spring',2, False, 3.141593]
for eltype in newlist:
    print(eltype,type(eltype))

    #exercise #2 Поменять местам

my_list = [int(a) for a in input('Значения через пробел, по oкончании ввода нажмите Enter').split()]
for el in range(0,len(my_list)-1,2):
    my_list[el],my_list[el+1] = my_list[el+1],my_list[el]
print(my_list)