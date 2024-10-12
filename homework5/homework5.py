import random
s = []
a = [round(random.uniform(1, 50), 1) for _ in range(19)]
print("Исходный массив:", a)
for i in range(0, len(a)-1):
    if a[i] < a[i+1]:
        s.append(a[i+1])
print("Цифры, которые больше предыдущего элемента: ", s)