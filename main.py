from task1 import Alphabet, EngAlphabet
from task2 import Human, SmallHouse
from task3 import AppleTree, Gardener
from task4 import KmrWork


def run_task1():
    print("\n=== TASK 1: Alphabet ===")
    try:
        eng = EngAlphabet()
        eng.print_alphabet()
        print("Кількість букв:", eng.letters_num())
        print("Чи H англійська?", eng.is_en_letter("H"))

        ua = Alphabet()
        print("Чи 'Л' українська?", ua.is_ua_lang("Л"))
        print("Example:", EngAlphabet.example())
    except Exception as e:
        print("Помилка:", e)


def run_task2():
    print("\n=== TASK 2: Human ===")
    Human.default_info()

    h = Human(name="Антон", age=20, money=2000)
    h.info()

    house = SmallHouse(price=5000)

    h.buy_house(house)   # Недостатньо грошей
    h.earn_money(4000)   # Заробив
    h.buy_house(house)   # Тепер купив
    h.info()


def run_task3():
    print("\n=== TASK 3: AppleTree ===")

    tree = AppleTree(5)
    gardener = Gardener("Петро", tree)

    Gardener.apple_base(tree)
    gardener.work()
    gardener.work()
    gardener.work()

    gardener.harvest()
    Gardener.apple_base(tree)


def run_task4():
    print("\n=== TASK 4: CSV STATS ===")

    kmr1 = KmrWork("kmr1.csv", 1)
    kmr2 = KmrWork("kmr2.csv", 2)

    kmr2.avg_plot(kmr2.avg_stat(kmr2.data))
    kmr2.marks_plot(kmr2.marks_stat(kmr2.data))

    kmr1.compare_csv(kmr2)
    kmr1.compare_avg_plots(kmr2)


def menu():
    print("\n=============================")
    print("ОБЕРИ ЗАВДАННЯ:")
    print("1 — Task 1 (Alphabet)")
    print("2 — Task 2 (Human)")
    print("3 — Task 3 (AppleTree)")
    print("4 — Task 4 (KMR CSV)")
    print("0 — Вийти")
    print("=============================")

    cmd = input("Введи номер: ")

    match cmd:
        case "1": run_task1()
        case "2": run_task2()
        case "3": run_task3()
        case "4": run_task4()
        case "0": exit()
        case _: print("Невірний вибір!")


if __name__ == "__main__":
    while True:
        menu()
