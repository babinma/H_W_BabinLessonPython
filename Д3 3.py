print("1 ПУНКТ ДЗ К УРОКУ 2")
list1 = [2, 'text', 456, 45.3, None]
count_el_list1 = len(list1)
print(list1)
print(f'Всего в списке {count_el_list1} элементов')
list2 = []
x = -1
for el in list1:
    x=x+1
    tip = type(list1[x])# ghjdthrfrf
    n=x+1
    d = (f'Тип {n} элемента: {tip}')
    list2.insert(x, d)
x = -1
for el in list2:
    x=x+1
    print(list2[x])


print("2 ПУНКТ ДЗ К УРОКУ 2")
list =[]

d = input("Введите значение для списка, если все нужные значения введены уже ранее, введите "no": ")
while d != "no":
    list.append(d)
    d = input("Введите значение для списка, если все нужные значения введены уже ранее, введите no: ")
print(list)

n = len(list) - 1
v = 0
while v < n:
    r = list[v]
    s = v+1
    list[v] = list[s]
    list[s] = r
    v = v + 2
print(list)

print("3 ПУНКТ ДЗ К УРОКУ 2")

my_dict3 = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Autumn'}
list3 = [my_dict3.get(1), my_dict3.get(2), my_dict3.get(2), my_dict3.get(2),my_dict3.get(2),my_dict3.get(3),my_dict3.get(3),my_dict3.get(3),my_dict3.get(4), my_dict3.get(4), my_dict3.get(4),my_dict3.get(1)]
d = int(input('Enter the number of the month in which you were born: '))
s = list3[d-1]
print(f'It was a {s}!')

print("4 ПУНКТ ДЗ К УРОКУ 2")

string4 = input("Введите строчку текста: ")
list4 = string4.split( )
n = len(list4)
s = 0
while s < n:
    a = str(list4[s])
    s = s+1
    print(f'{s}.{a[0:10]}')

print("5 ПУНКТ ДЗ К УРОКУ 2")
print ('Created a rating from elements: 23231231233,344,4,5,5,7,888,99,321,321,345')
list5 = [23231231233,344,4,5,5,7,888,99,321,321,345]
list5.sort(reverse=True)

d = int(input('Enter a new rating element: '))

n = len(list5)
s = 0
while s < n:
    a = (list5[s])
    if a == d:
        v = list5.index(a)+list5.count(a)
        list5.insert(v, d)
        break
    else:
        if  s == n - 1:
            list5.append(d)
            list5.sort(reverse=True)
    s = s + 1

print(f'Rating numbers with a new value: {list5}')


