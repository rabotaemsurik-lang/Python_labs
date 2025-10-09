import random
import math


def task1():
    print("Завдання 1-----------------------------------------------------------------------------------")
    list_random_number = random.sample(range(0, 101), 10)
    print(list_random_number)
    print("Числа <=50:")
    for i in list_random_number:
        if i <= 50:
            print(i)


def task2():
    print("Завдання 2-----------------------------------------------------------------------------------")
    while True:
        try:
            price = int(input("Введіть ціну: "))
            break
        except ValueError:
            print("Введіть число!")

    if price <= 0:
        print("Ціна не може бути <= 0")
    elif price < 500:
        print("Знижки немає:", price)
    elif price < 1000:
        print("Знижка є:", (price * 97) / 100)
    else:
        print("Знижка є:", (price * 95) / 100)


def task3():
    print("Завдання 3-----------------------------------------------------------------------------------")
    while True:
        try:
            a = int(input("Введіть сторону a = "))
            c = int(input("Введіть сторону c = "))
            break
        except ValueError:
            print("Введіть число!")

    b = a
    print("У нас рівнобедрений трикутник, тому a = b, c - основа")
    if a + b > c:
        p = (a + b + c) / 2
        s1 = p * (p - a) * (p - b) * (p - c)
        s = math.sqrt(s1)
        if s % 2 == 0:
            print("Площа парна, s/2 =", s / 2)
        else:
            print("Не можу ділити на 2. Площа =", s)
    else:
        print("Трикутник не існує")


def task4():
    print("Завдання 4-----------------------------------------------------------------------------------")
    while True:
        try:
            A = int(input("Введіть A: "))
            B = int(input("Введіть B: "))
            break
        except ValueError:
            print("Введіть число!")

    if A < B:
        suma = sum(range(A, B + 1))
        print("Сума чисел від A до B:", suma)
    else:
        print("A має бути менше за B")


def task5():
    print("Завдання 5-----------------------------------------------------------------------------------")
    while True:
        try:
            A = int(input("Введіть A: "))
            B = int(input("Введіть B: "))
            break
        except ValueError:
            print("Введіть число!")

    if A < B:
        suma = sum(i ** 2 for i in range(A, B + 1))
        print("Сума квадратів чисел від A до B:", suma)
    else:
        print("A має бути менше за B")


def task6():
    print("Завдання 6-----------------------------------------------------------------------------------")
    while True:
        try:
            a = int(input("Введіть a: "))
            b = int(input("Введіть b: "))
            break
        except ValueError:
            print("Введіть число!")

    if a <= b:
        suma = 0
        while a <= b:
            suma += a
            a += 1
        print("Сума всіх чисел від a до b:", suma)
    else:
        print("a має бути <= b")


def task7():
    print("Завдання 7-----------------------------------------------------------------------------------")
    while True:
        try:
            a = int(input("Введіть a: "))
            break
        except ValueError:
            print("Введіть число!")

    if 0 <= a <= 50:
        suma = sum(i ** 2 for i in range(a, 51))
        print(f"Сума квадратів чисел від {a} до 50:", suma)
    else:
        print("Число a не входить у 0 <= a <= 50")


def task8():
    print("Завдання 8-----------------------------------------------------------------------------------")
    while True:
        try:
            N = int(input("Введіть N: "))
            break
        except ValueError:
            print("Введіть число!")

    if N <= 1:
        print("N має бути > 1")
    else:
        K = 1
        while 5 ** K <= N:
            K += 1
        print("Найменше ціле число K, при якому 5^K > N =", K)


def task9():
    print("Завдання 9-----------------------------------------------------------------------------------")
    while True:
        try:
            n = int(input("Введіть число n: "))
            break
        except ValueError:
            print("Введіть число!")

    for i in range(1, 20000):
        square = i ** 2
        if square > n:
            print("Перше число > n - це", i, "^2 =", square)
            break


def task10():
    print("Завдання 10----------------------------------------------------------------------------------")
    while True:
        try:
            n = int(input("Введіть число n: "))
            break
        except ValueError:
            print("Введіть число!")

    first = 1
    for_step = 1
    while for_step <= n:
        first += 1
        for_step = first ** 2 + 1
    print("Перше число > n:", for_step)


def task11():
    print("Завдання 11----------------------------------------------------------------------------------")
    while True:
        try:
            D = int(input("Введіть день: "))
            M = int(input("Введіть місяць: "))
            break
        except ValueError:
            print("Введіть число!")

    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= M <= 12 and 1 <= D <= days_in_month[M]:
        if (M == 1 and D >= 20) or (M == 2 and D <= 18):
            sign_zod = "Водолій"
        elif (M == 2 and D >= 19) or (M == 3 and D <= 20):
            sign_zod = "Риби"
        elif (M == 3 and D >= 21) or (M == 4 and D <= 19):
            sign_zod = "Овен"
        elif (M == 4 and D >= 20) or (M == 5 and D <= 20):
            sign_zod = "Телець"
        elif (M == 5 and D >= 21) or (M == 6 and D <= 21):
            sign_zod = "Близнюки"
        elif (M == 6 and D >= 22) or (M == 7 and D <= 22):
            sign_zod = "Рак"
        elif (M == 7 and D >= 23) or (M == 8 and D <= 22):
            sign_zod = "Лев"
        elif (M == 8 and D >= 23) or (M == 9 and D <= 22):
            sign_zod = "Діва"
        elif (M == 9 and D >= 23) or (M == 10 and D <= 22):
            sign_zod = "Терези"
        elif (M == 10 and D >= 23) or (M == 11 and D <= 22):
            sign_zod = "Скорпіон"
        elif (M == 11 and D >= 23) or (M == 12 and D <= 21):
            sign_zod = "Стрілець"
        else:
            sign_zod = "Козеріг"
        print("Знак Зодіаку:", sign_zod)
    else:
        print("Немає такої дати")


def task12():
    print("Завдання 12----------------------------------------------------------------------------------")
    while True:
        try:
            number_of_od_mas = int(input("Введіть номер одиниці маси (1-кілограм, 2-мілiграм, 3-грам, 4-тонна, 5-центнер): "))
            masa = float(input("Маса тіла в одиницях: "))
            break
        except ValueError:
            print("Введіть число!")

    if number_of_od_mas == 1:
        mass_kg = masa
    elif number_of_od_mas == 2:
        mass_kg = masa / 1_000_000
    elif number_of_od_mas == 3:
        mass_kg = masa / 1000
    elif number_of_od_mas == 4:
        mass_kg = masa * 1000
    elif number_of_od_mas == 5:
        mass_kg = masa * 100
    else:
        print("Не то ввели")
        return

    print("Маса тіла у кілограмах:", mass_kg)


def main():
    while True:
        print("Меню завдань:")
        for i in range(1, 13):
            print(f"Завдання {i}")
        print("вихід - 0")
        while True:
            try:
                choice = int(input("номер завдання: "))
                break
            except ValueError:
                print("Введіть число!")

        match choice:
            case 0:
                print("Вихід з програми...")
                break
            case 1:
                task1()
            case 2:
                task2()
            case 3:
                task3()
            case 4:
                task4()
            case 5:
                task5()
            case 6:
                task6()
            case 7:
                task7()
            case 8:
                task8()
            case 9:
                task9()
            case 10:
                task10()
            case 11:
                task11()
            case 12:
                task12()
            case _:
                print("Немає такого завдання!")


if __name__ == "__main__":
    main()
