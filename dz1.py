import numpy as np

#Создать массив из 25 нулей
zeros_arr = np.zeros(25)
#zeros_arr = [0] * 25
print(zeros_arr)

#Создать массив из 10 единиц
ones_arr = np.ones(10)
print(ones_arr)

#Создать массив из 12 пятерок
fives_arr = np.full(12, 5)
#[5 for i in range(10)]
print(fives_arr)

#Создать массив из целых чисел от 12 до 51
arr1 = np.arange(12, 52)
#[i for i in range(12, 52)]
print(arr1)

#Создать массив из целых четных чисел от 12 до 51
arr2 = np.arange(12, 52, 2)
#[i for i in range(12,52) if i % 2 == 0]
print(arr2)

#Создать матрицу 3х3 с числами от 1 до 9
arr3 = np.arange(1, 10).reshape(3, 3)
#[[i for i in range(1, 4)], [i for i in range (4, 7)], [i for i in range(7, 10)]]
print(arr3)

#Создать единичную матрицу 5х5
arr4 = np.eye(5, 5)
#units_p = [[1 for i in range(5)] for i in range(5)]
print(arr4)

#Создайте матрицу 
# [[0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09 0.1 ]
#  [0.11 0.12 0.13 0.14 0.15 0.16 0.17 0.18 0.19 0.2 ]
#  [0.21 0.22 0.23 0.24 0.25 0.26 0.27 0.28 0.29 0.3 ]
#  [0.31 0.32 0.33 0.34 0.35 0.36 0.37 0.38 0.39 0.4 ]
#  [0.41 0.42 0.43 0.44 0.45 0.46 0.47 0.48 0.49 0.5 ]
#  [0.51 0.52 0.53 0.54 0.55 0.56 0.57 0.58 0.59 0.6 ]
#  [0.61 0.62 0.63 0.64 0.65 0.66 0.67 0.68 0.69 0.7 ]
#  [0.71 0.72 0.73 0.74 0.75 0.76 0.77 0.78 0.79 0.8 ]
#  [0.81 0.82 0.83 0.84 0.85 0.86 0.87 0.88 0.89 0.9 ]
#  [0.91 0.92 0.93 0.94 0.95 0.96 0.97 0.98 0.99 1.  ]]
arr5 = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
#matrix = [[0.01 * j + 0.1 * i for j in range(1, 11)] for i in range(10)]
print(arr5)

# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]
arr6 = np.arange(1, 26).reshape(5, 5)
print(arr6)

# Извлечь подматрицу из 9 задания
#  [[12 13 14 15]
#  [17 18 19 20]
#  [22 23 24 25]]
a = arr6[2:, 1:]
print(a)

#Написать код, который извлечет число 15 из 9 задания
element = arr6[2, 4]
print(element)

# Извлечь из 9 задания матрицу +
#  [[7]
#  [12]
#  [17]]
sub_arr = arr6[1:4, [1]]
print(sub_arr)

# Извлечь из 9 задания строку 
#  [[21 22 23 24 25]]
row = arr6[4:5, :]
print(row)

# Извлечь две строки из 9 задания +
#  [[16 17 18 19 20]
#  [21 22 23 24 25]]
rows = arr6[3:5, :]
print(rows)


#Получить сумму всех значений из матрицы в задании 9
matrix_sum = np.sum(arr6)
#total_sum = sum(sum(arr6, []))
#total_sum = sum(sum(row) for row in arr6)
print(matrix_sum)


#Получить сумму значений в колонках из матрицы в задании 9 +
column_sums = arr6.sum(axis=0)
# column_sum = [0] * len(arr6[0])
# for row in arr6:
#     for i in range(len(row)):
#         column_sum[i] += row[i]

print(column_sums)



