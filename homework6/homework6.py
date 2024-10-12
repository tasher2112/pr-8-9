import random

a = [round(random.uniform(1, 50), 1) for _ in range(10)]
print("Исходный массив:", a)
x = min(a)
y = max(a)
print("Минимальное и максимальное числа: ", x, " и ", y)
min_ind = a.index(x)
max_ind = a.index(y)
a[min_ind], a[max_ind] = a[max_ind], a[min_ind]
print("Изменённый массив: ", a)