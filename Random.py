import random 
def random_user():
    num_1 = int(input("Введите число от 1 до 10"))
    p = True
    while p:
        num_2 = random.randint(1,10)
        if num_1 == num_2:
            print(f"Компьютер угадал число{num_2}")
            break
        else:
            print(f"Компьютер не угадал{num_2}")

    
random_user()            
