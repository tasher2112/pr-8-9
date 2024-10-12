import re

def split(email):
    match = re.match(r"(.+)@(.+)", email)
    if match:
        username = match.group(1)
        domain = match.group(2)
        return {
            'username': username, 
            'domain': domain
        }
    else:
        return {
            'username': None, 
            'domain': None
        }

email = input("Введите email адрес: ")
result = split(email)

# Выводим результат
if result['username'] and result['domain']:
    print(f"Имя пользователя: {result['username']}")
    print(f"Доменное имя: {result['domain']}")
else:
    print("Некорректный email адрес.")