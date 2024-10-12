import random

def check(number):
    for i in number:
        if i.isdigit() == False:
            print("Неверный ввод!!!")
            return False
    return True

def main(a):
    user_inputs = []
    for i in range(5):
        while True:
            print(f"Введите", i+1, " число из", i+1, " строки: ")
            x = input()
            if check(x):
                x = int(x)
                if x in a[i]:
                    user_inputs.append(x)
                    break
                else:
                    print("Числа нет в этой строке!")
            else:
                continue
    return user_inputs

def rand_choose(a):
    choose = []
    for i in range(5):
        choose.append(random.choice(a[i]))
    return choose

def comparison(user_inputs, choose):
    matches = 0
    for i, user_input in enumerate(user_inputs):
        if user_input == choose[i]:
            matches += 1
    print("Совпадений:", matches)

a = [[random.randint(0, 30) for j in range(5)] for i in range(5)]
print("Лотерейный билет: ")
for i in a:
    print(i)

user_inputs = main(a)
rand_nums = rand_choose(a)
print("Случайный выбор:", rand_nums)
print("Ваш выбор:", user_inputs)
comparison(user_inputs, rand_nums)