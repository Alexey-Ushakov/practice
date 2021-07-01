# Списки
ls_1 = [1, 2, 3, 4]  # Списки могут быть из числе
ls_2 = ["a", "b", "c", "d"]  # Из строк
ls_3 = ["a", 2, 2.3]  # Из строк и чисел как целых int так и вещественных float
new_ls = ls_1 + ls_2
print(new_ls)
ls_1 *= 3
print(ls_1)
ls_1.append(2)  # добавляет хначение к концу списка
print(ls_1)
print(len(new_ls))  # длинна списка
ls = [1, 2, 3, 4, 5]
b = ls.pop(0)  # Удаляет элемент с индексом указанным в скобках и возхвращает его. Если скобки пустые удаляет
# последний элемент и возвращает его как видно происвоив переменной значение удаленного элемента
print(ls, b)
# Операции над списками
ls = [1, 2, 3, 4, 5]
print(ls)
a = []  # Создаем новый пустой список в него мы положим новые изменненые элементы исходного списка
for i in ls:  # пробегаем по всем элементам исходного списка
    i = i * 2  # производим над ними какуюто опирацию
    a.append(i)  # добовляем каждый изменный элемент в новым список
    print(a)  # получаем новый список добавление по элементно
print(ls)  # Как мы видим сам список не изменился
# При помощи цикла вайл мы вытаскиваем элементы и изменяем их уже в самом списке
i = 0  # Начинаем с нулдевого элемента
while i < len(ls):  # По длинне всего списка
    ls[i] *= 2  # Умножаем каждый элемент на 2
    i += 1
print(ls)

ls = [1, 2, 3, 4, 4]
for elem in (0, len(ls)):
    print(elem)

# Поиск элемента в списке
ls = [1, 2, 3, 4, 4]
x = 4  # Задаем икс который мы хотим найти в списке ls
if x in ls: # Если икс есть в списке то
    print(ls.index(x))  # в данном случаее мы хотим вывести индекс этого икса ВНИМАНИЕ выведет индекс первого
    # совпадающего значения
else:
    print(x in ls)  # Если его нет выведет False
# Поиск элемента в списке всех X
ls = [1, 2, 3, 4, 4]
x = 4
i = 0
while i < len(ls):
    if ls[i] == x:
        print(i)
    i += 1
#  Очень важная вещь с циклами мы можем брать информацию из списков и делать с ними действия не изменяя сам список!!!!
#  если нам нужно изменить элементы списка то мы затрагиваем ИНДЕКСЫ!
ls = [1, 2, 3, 4, 4]
for elem in range(0, len(ls)):
    ls[elem] += ls[elem]
print(ls)

ls = [1, 2, 3, 4, 4]
for elem in ls:
    print(elem)
print(ls)

