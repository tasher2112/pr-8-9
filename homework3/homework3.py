x = input("Выберите какой квадрат нарисовать(1 - полый, 2 - заполненный): ")
if x.isdigit() == False:
    print("Неверный ввод!")
else:
    x = int(x)
    if x == 1:
        for i in range(10):
            for j in range(10):
                if i == 0 or i == 9 or j == 0  or j == 9:
                    print("*  ",end = "")
                else:
                    print("   ",end = "")
            print()
    if x == 2:
        for i in range(10):
            for j in range(10):
                print("*  ",end="")
            print()
