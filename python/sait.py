
age = int(input("Введите ваш возвраст:"))
five_rub = int(input("Введите ваше количество монет по 5 рублей:"))
ten_rub = int(input("Введите ваше количество монет по 10 рублей:"))
name = input("Введите ваше имя:")


pivo = (age > 21 and age % 2 == 0 and name != "Олег" and name != "олег") or name == "Инокентий" 

if pivo:
    total_money = five_rub * ten_rub * 10
    hotdog_price = 20
    num_hotdogs = total_money // hotdog_price
    print(f"Вам можно купить хотдоги!Вы можете купить {num_hotdogs} хотдогов.")
else:
    print("К сожалению вам нельзя купить хотдоги.")