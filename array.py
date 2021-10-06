import random
import numpy as np

random.seed(23)#Зерно

m, n = 5, 10
a = [[random.randint(100, 999) for j in range(m)] for i in range(n)]#генерация массива 5х10
a=np.array(a)
print("Исходный массив:\n\n", a)

numb = int(input("Введите целое число: "))
print("Простые:", end = " ")
for i in range(numb - 1, 1, -1):
    is_simple = 0 # Счётчик
    if (numb % i == 0):
        for j in range(i - 1, 1, -1):
            if (i % j == 0):
                is_simple = is_simple + 1 # Увеличиваем, если находим делитель
        if (is_simple == 0): # Если делителей не было найдено, выводим
            print(i, end = " ")