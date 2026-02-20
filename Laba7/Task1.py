from datetime import date
import csv


class Person:
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname

        if isinstance(birth_date, str):
            y, m, d = map(int, birth_date.split('-'))
            self.birth_date = date(y, m, d)
        else:
            self.birth_date = birth_date

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return str(age)

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"

    def __str__(self):
        return (
            f"Surname: {self.surname}\n"
            f"First name: {self.first_name}\n"
            f"Nickname: {self.nickname}\n"
            f"Birth date: {self.birth_date}\n"
            f"Fullname: {self.get_fullname()}\n"
            f"Age: {self.get_age()}"
        )


def modifier(filename):
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    persons = []

    for r in rows:
        p = Person(
            surname=r["surname"],
            first_name=r["first_name"],
            nickname=r.get("nickname") or None,
            birth_date=r["birth_date"]
        )
        persons.append(p)

    new_fields = ["surname", "first_name", "fullname", "nickname", "birth_date", "age"]

    with open(filename, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=new_fields)
        writer.writeheader()

        for p in persons:
            writer.writerow({
                "surname": p.surname,
                "first_name": p.first_name,
                "fullname": p.get_fullname(),
                "nickname": p.nickname or "",
                "birth_date": p.birth_date.isoformat(),
                "age": p.get_age()
            })
while True:
    print("1 — для завдання 1")
    print("2 — для завдання 2")
    print("0 — Вийти")
    task = input("Ваш вибір: ")

    if task == "1":
        print("\n--- TASK 1 ---\n")
        p = Person("Грицай", "Денис", "2007-06-21", nickname="Cheremuha")
        print(p)
    elif task == "2":
        print("\n--- TASK 2 ---\n")
        filename = input("Введіть ім'я CSV-файлу: ")
        try:
            modifier(filename)
            print("Файл успішно модифіковано!")
        except FileNotFoundError:
            print("Помилка! Файл не знайдено. Спробуйте ще раз.")

    elif task == "0":
        print("Програма завершена.")
        break

    else:
        print("Невірний вибір! Введіть 1, 2 або 0.")
