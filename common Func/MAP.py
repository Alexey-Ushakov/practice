#  Взяли рандомный список ПРИ ПОМОЩИ MAP превратили в строку и ПРИ ПОМОЩИ JOIN собрали строку обратно

my_list = [random.randint(0, 9) for i in range(0, 2500)]
my_list = ''.join(map(str, my_list))
print(my_list)

# Здесь использовали map для изменения кортежей  в списки после использования zip список стал кортежем
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]
matrix_1 = list(map(list, (zip(*matrix))))
print(matrix_1)
matrix_1 = list(zip(*matrix))
print(matrix_1)