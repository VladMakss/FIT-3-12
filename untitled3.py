# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-qWuR2vMKzM2u1PjudJErQ3Fz7L6hwiO
"""

### ЗАВДАННЯ 1.1: створити та проінспектувати масив 3х4 з ім'ям arr1_1, який містить числа з плавоючою точкою 
arr1_1 = ...
print(arr1_1)

import numpy as np

arr1_1 = np.random.rand(3, 4)
print(arr1_1)

### ЗАВДАННЯ 1.2: створити одномірний масив з 5 строкових елементів
arr1_2 = ...
print(arr1_2)

arr1_2 = ['яблуко', 'банан', 'апельсин', 'киві', 'груша']
print(arr1_2)

### ЗАВДАННЯ 1.3: створити одиничний масив 3х4 чисел з плаваючою точкою
arr1_3 = ...
print(arr1_3)

import numpy as np

arr1_3 = np.ones((3, 4), dtype=float)
print(arr1_3)

### ЗАВДАННЯ 2.1: створити 3-мірний масив (3х1х3) логічного 'False'
arr2_1 = ...
...
print(arr2_1)

import numpy as np

arr2_1 = np.zeros((3, 1, 3), dtype=bool)
print(arr2_1)

### ЗАВДАННЯ 2.2: перетворити масив arr2_1 в 2-мірний масив (3х3) типу int
arr2_2 = ...
...
print(arr2_2)

import numpy as np

arr2_1 = np.zeros((3, 1, 3), dtype=bool)  # створюємо масив
arr2_2 = arr2_1.astype(int)  # перетворюємо масив в тип int

print(arr2_2)

### ЗАВДАННЯ 2.3: створити  2-мірний масив парних чисел в інтервалі 10-21
arr2_3 = ...
...
print(arr2_3)

arr2_3 = []
for i in range(10, 22):
    if i % 2 == 0:
        row = [i, i+1]
        arr2_3.append(row)
print(arr2_3)

### ЗАВДАННЯ 3.1: створити масив 4х5 нормально розподілений випадкових чисел 3 інтервалу [10 - 100]
arr3_1 = ...

import numpy as np

# задаємо параметри для нормального розподілу
mean = 55
std = 20

# генеруємо масив випадкових чисел з нормального розподілу з заданими параметрами
arr3_1 = np.random.normal(loc=mean, scale=std, size=(4, 5))

# масштабуємо масив так, щоб значення були в інтервалі [10 - 100]
arr3_1 = np.interp(arr3_1, (arr3_1.min(), arr3_1.max()), (10, 100))

print(arr3_1)

### ЗАВДАННЯ 3.2:  вивести 3-елемент в 2-му рядку
el3_2 = ...
print(el3_2)

el3_2 = arr3_1[1][2]
print(el3_2)

### ЗАВДАННЯ 3.3:  вивести 2-й рядок масива `arr3_1`
vect3_3 = ...
print(vect3_3)

vect3_3 = arr3_1[1, :]
print(vect3_3)

### ЗАВДАННЯ 3.4:  вивести 3 колонку масива `arr3_1`
vect3_4 = ...
print(vect3_4)

vect3_4 = arr3_1[:, 2]
print(vect3_4)

### ЗАВДАННЯ 3.5: вивести матрицю  з 2 та 3 рядка та 2 та 3 колонки масива `arr3_1`
mat3_5 = ...
print(mat3_5)

mat3_5 = arr3_1[1:3, 1:3]
print(mat3_5)

# ЗАВДАННЯ 4.1: створити квадратну матрицю з 36 рівномірно розподілених цілих 
# елементів з інтервалу 100 - 200
mat4_1 = ...
print(mat4_1)

import numpy as np

mat4_1 = np.random.randint(low=100, high=201, size=(6,6))
print(mat4_1)

# ЗАВДАННЯ 4.2: вивести головну діагональ матниці `mat4_1`
diag4_2 = ...
print(diag4_2)

import numpy as np

diag4_2 = np.diagonal(mat4_1)
print(diag4_2)

# ЗАВДАННЯ 4.3: транспонувати матрицю 'mat4_1'
trans4_3 = ...
print(trans4_3)

trans4_3 = mat4_1.T
print(trans4_3)

# ЗАВДАННЯ 4.4: вирахувати зворотню до 'mat4_1' матрицю 
inv4_4 = ...

import numpy as np

det = np.linalg.det(mat4_1)
if det != 0:
    inv4_4 = np.linalg.inv(mat4_1)
    print(inv4_4)
else:
    print("Матриця є виродженою")

# ЗАВДАННЯ 5.1: просумувати по рядкам масив випадкових чисел розмірностю 3х4
mat5_1 = ...
sum_mat5_1 = ...
print(sum_mat5_1)

import random

# створюємо масив розмірності 3х4 з випадковими числами
mat5_1 = [[random.randint(0, 9) for j in range(4)] for i in range(3)]

# виводимо масив на екран
for row in mat5_1:
    print(row)

# обчислюємо суму кожного рядка
sum_mat5_1 = [sum(row) for row in mat5_1]

# виводимо суму кожного рядка на екран
print(sum_mat5_1)

# ЗАВДАННЯ 5.2: знайти мінімальний елемент матриці `sum_mat5_1`
min_mat5_1 = ...
print(min_mat5_1)

import random

# створюємо масив розмірності 3х4 з випадковими числами
mat5_1 = [[random.randint(0, 9) for j in range(4)] for i in range(3)]

# обчислюємо суму кожного рядка
sum_mat5_1 = [sum(row) for row in mat5_1]

# знаходимо мінімальний елемент
min_mat5_1 = min(sum_mat5_1)

# виводимо мінімальний елемент на екран
print(min_mat5_1)

# ЗАВДАННЯ 5.3: створити масив додавши до елементів `mat5_1`  число 100
mat5_3 = ...
print(mat5_3)

import random

# створюємо масив розмірності 3х4 з випадковими числами
mat5_1 = [[random.randint(0, 9) for j in range(4)] for i in range(3)]

# створюємо новий масив, додавши до кожного елементу mat5_1 число 100
mat5_3 = [[elem+100 for elem in row] for row in mat5_1]

# виводимо новий масив на екран
for row in mat5_3:
    print(row)

# ЗАВДАННЯ 5.4: помножити матрицю `mat5_1` на головну діагональ матриці `mat5_3`
mat5_4 = ...
print(mat5_4)

import random

# створюємо масив розмірності 3х4 з випадковими числами
mat5_1 = [[random.randint(0, 9) for j in range(4)] for i in range(3)]

# створюємо новий масив, додавши до кожного елементу mat5_1 число 100
mat5_3 = [[elem+100 if i==j else elem for j, elem in enumerate(row)] for i, row in enumerate(mat5_1)]

# виводимо матрицю mat5_3 на екран
for row in mat5_3:
    print(row)

# отримуємо головну діагональ матриці mat5_3
diag_mat5_3 = [mat5_3[i][i] for i in range(min(len(mat5_3), len(mat5_3[0])))]

# множимо матрицю mat5_1 на діагональну матрицю з елементами з diag_mat5_3
mat5_4 = [[mat5_1[i][j] * diag_mat5_3[j] for j in range(len(mat5_1[0]))] for i in range(len(mat5_1))]

# виводимо отриману матрицю mat5_4 на екран
for row in mat5_4:
    print(row)

# ЗАВДАННЯ 5.5: додати справа до матриці `mat5_3` матрицю `mat5_4` 
# вивести ранг отриманої матриці
mat5_5 = ...
...

import random
import numpy as np

# створюємо масив розмірності 3х4 з випадковими числами
mat5_1 = [[random.randint(0, 9) for j in range(4)] for i in range(3)]

# створюємо новий масив, додавши до кожного елементу mat5_1 число 100
mat5_3 = [[elem+100 if i==j else elem for j, elem in enumerate(row)] for i, row in enumerate(mat5_1)]

# отримуємо головну діагональ матриці mat5_3
diag_mat5_3 = [mat5_3[i][i] for i in range(min(len(mat5_3), len(mat5_3[0])))]

# множимо матрицю mat5_1 на діагональну матрицю з елементами з diag_mat5_3
mat5_4 = [[mat5_1[i][j] * diag_mat5_3[j] for j in range(len(mat5_1[0]))] for i in range(len(mat5_1))]

# додаємо матрицю mat5_4 справа від матриці mat5_3
mat5_5 = np.hstack((mat5_3, mat5_4))

# виводимо матрицю mat5_5 на екран
for row in mat5_5:
    print(row)

# виводимо ранг матриці mat5_5
print("Ранг матриці mat5_5:", np.linalg.matrix_rank(mat5_5))