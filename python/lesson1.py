num1 = int(input("vvedite 1 chislo"))
num2 = int(input("vvedite 2 chislo"))


char = str(input("vvedite znak + - * / %: "))

if(char == "+"):
    print(num1 + num2)
elif(char == "-"):
    print(num1 - num2)
elif(char == "*"):
    print(num1 * num2)
elif(char == "/"):
    print(num1 / num2)
elif(char == "%"):
    print(num1 % num2)
else:
    print("ti perepytal")