def calculator():
    user = input("Введите + или -")
    num_1 = int(input("Введите первое число"))
    num_2 = int(input("Введите второе число"))
    
    if user == "+":
        print(f"Сумма равна {num_1+num_2}")
    elif user == "-":
        print(f"Сумма равна {num_1-num_2}")
    else:print("Вы ввели неправильный опратор") 

calculator()
