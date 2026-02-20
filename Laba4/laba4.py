import random
from random import choices


def task1():

    while True:
        n = input("Введіть N (>0): ").strip()
        if not n.isdigit() or int(n) <= 0:
            print("Помилка! Введіть додатнє число.")
        else:
            n = int(n)
            break

    arr = []
    print(f"Введіть {n} цілих чисел:")
    while len(arr) < n:
        s = input().strip()
        parts = s.split()
        for p in parts:
            try:
                arr.append(int(p))
            except:
                print(f"{p} не число, не врах")
            if len(arr) == n:
                break

    maximum = max(arr)
    arr.reverse()

    print("Максимальний елемент:", maximum)
    print("Список у зворотному порядку:", arr)


def task2():
    while True:
        n = input("Введіть N (>0): ").strip()
        if not n.isdigit() or int(n) <= 0:
            print("Помилка!")
        else:
            n = int(n)
            break

    arr = []
    print(f"Введіть {n} цілих чисел:")
    while len(arr) < n:
        s = input().strip()
        for p in s.split():
            try: arr.append(int(p))
            except: print(f"{p} не число")
            if len(arr) == n: break

    positives = []
    others = []

    for x in arr:
        if x > 0:
            positives.append(x)
        else:
            others.append(x)

    print("Позитивні:", positives)
    print("Інші:", others)


def task3():
    arr = []
    print("Введіть 20 цілих чисел:")

    while len(arr) < 20:
        s = input().strip()
        for p in s.split():
            try: arr.append(int(p))
            except: print(f"{p} не число")
            if len(arr) == 20: break

    total = 0
    for i in range(len(arr)):
        if i % 2 == 1:
            total += arr[i]

    print("Список:", arr)
    print("Сума елементів із непарними індексами:", total)


def task4():
    arr = [random.randint(-100, 100) for i in range(30)]
    maximum = max(arr)
    idx = arr.index(maximum)

    odd_numbers = []
    for x in arr:
        if x % 2 != 0:
            odd_numbers.append(x)

    print("Список:", arr)
    print("Максимум:", maximum, "Індекс:", idx)

    if odd_numbers:
        odd_numbers.sort(reverse=True)
        print("Непарні числа:", odd_numbers)
    else:
        print("Немає непарних чисел")


def task5():
    arr = [random.randint(-100, 100) for i in range(30)]
    print("Список:", arr)

    found = False
    for i in range(len(arr) - 1):
        if arr[i] < 0 and arr[i + 1] < 0:
            print(f"Пара ({arr[i]}, {arr[i+1]}) на позиції {i}")
            found = True

    if not found:
        print("Пар від'ємних чисел нема")


def task6():
    arr = []
    print("Введіть 10 чисел:")
    while len(arr) < 10:
        s = input().strip()
        for p in s.split():
            try: arr.append(int(p))
            except: print(f"{p} не число")
            if len(arr) == 10: break

    maximum = max(arr)

    smaller_squares = []
    for x in arr:
        if x < maximum:
            smaller_squares.append(x*x)

    smaller_squares.sort(reverse=True)

    print("Список:", arr)
    print("Максимум:", maximum)
    print("Квадрати менших:", smaller_squares)


def task7():
    arr = []
    for i in range(30):
        if random.choice([True, False]):
            arr.append(random.randint(-100, 100))
        else:
            arr.append(round(random.uniform(-100, 100), 3))

    min_by_abs = arr[0]
    for x in arr:
        if abs(x) < abs(min_by_abs):
            min_by_abs = x
    sorted_arr = sorted(arr)

    print("Список:", arr)
    print("Мінімальний по модулю:", min_by_abs)
    print("Сортований:", sorted_arr)


def task8():
    arr = []
    for _ in range(30):
        if random.choice([True, False]):
            arr.append(random.randint(-100, 100))
        else:
            arr.append(round(random.uniform(-100, 100), 3))

    groups = []
    for i in range(10):
        groups.append(arr[i*3:(i+1)*3])

    groups_with_sum = []
    for g in groups:
        s = sum(abs(x) for x in g)
        groups_with_sum.append((g, s))

    groups_sorted = sorted(groups_with_sum, key=lambda x: x[1])

    print("Список:", arr)
    for g, s in groups_sorted:
        print(f"{g} (сума |x| = {s})")


def main():
    while True:
        print("\nВиберіть завдання:")
        print("  1 - Максимум і вивід у зворотному порядку")
        print("  2 - Розділення на позитивні та інші")
        print("  3 - Сума елементів з непарними індексами")
        print("  4 - Максимум, індекс і непарні числа")
        print("  5 - Пошук пар від'ємних елементів")
        print("  6 - Квадрати менших за максимум")
        print("  7 - Мінімум по модулю та сортування")
        print("  8 - Групи по 3 та сортування за сумою модулів")
        print("  0 - Вихід")

        choice = input("\nВаш вибір: ").strip()

        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
        elif choice == '4':
            task4()
        elif choice == '5':
            task5()
        elif choice == '6':
            task6()
        elif choice == '7':
            task7()
        elif choice == '8':
            task8()
        elif choice == '0':
            print("Вихід")
            break
        else:
            print("Ви ввели яусь фігню")


if __name__ == "__main__":
    main()