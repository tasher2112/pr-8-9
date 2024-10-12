def check(number):
    for i in number:
        if i == ".":
            continue
        elif i.isdigit() == False:
            print("Неверный ввод!!!")
            break
x = input("Введите x:")
check(x)
y = input("Введите y:")
check(y)
print("Все числа между ", x, " и ", y)
if int(float(x)) < int(float(y)):
    for i in range(int(float(x))+1, int(float(y))+1):
        print(i, end=" ")
else:
    for i in range(int(float(y))+1, int(float(x))+1):
        print(i, end=" ")