import random

a = [round(random.uniform(1, 50), 1) for _ in range(random.randint(5,15))]
sh = a[len(a)-1]
print(a)
for i in range(len(a) - 1, 0, -1):
    a[i] = a[i-1]
a[0] = sh
print(a)