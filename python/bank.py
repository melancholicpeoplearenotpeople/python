age = int(input("введи ваш возраст"))

if (age % 3 == 0 or age > 40): 
    print ("ты прошел проверку")
else:
    print("ты не прошел проверку")

name = str(input ("введите ваше имя"))

if(name !="Олег" and name != "олег" and name != "oleg" and name !="Oleg" and len(name) >= 4):
    print("ты прошел проверку")
else:
    print("ты не прошел проверку")

num1 = int(input("введите первое число"))
num2 = int(input("введите второе число"))

sum = num1 + num2

if (sum % 7 == 0 or sum**2 > 500):
    print("ты прошел проверку")
else:
    print("ты не прошел проверку")