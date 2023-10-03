import random

N = random.randint(4, 30)
def pickupstone(n):
    global N
    N = N - n
    return N <= 0
print(N)
while N > 0:
    try:
        print("Ваш ход\n")
        count = int(input("Введите количество камней от 1 до 3\n"))
        if count < 0 or count > 3:
            raise 'ошибка'
        if pickupstone(count):
            print("Вы проиграли")
            break
        print(f'{N}\n')
        print("Ход соперника\n")
        count = random.randint(1, 4)
        if pickupstone(count):
            print("Вы победили")
            break
        print(f'{N}\n')
    except:
        print("Введено неверное количество камней")
