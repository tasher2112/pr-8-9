while(True):
    x = str(input("Введите 0 для выхода из цикла или целую цифру для суммирования: "))
    if x.isdigit() == False:
        print("Вы ввели не число!")
        break
    if int(x) == 0:
        print("Вы вышли из цикла!")
        break
    else:
        y = str(input("Введите вторую цифру для суммирования: "))
        if y.isdigit() == False:
            print("Вы ввели не число!")
            break
        print("Сумма: ", int(x) + int(y))