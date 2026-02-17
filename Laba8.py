import random
from datetime import date



class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Додано {amount}, новий баланс: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Знято {amount}, новий баланс: {self.__balance}")
        else:
            print("Недостатньо коштів!")

    def get_balance(self):
        return self.__balance



class Coin:
    def __init__(self):
        self.__sideup = "heads"

    def toss(self):
        self.__sideup = random.choice(["heads", "tails"])
        return self.__sideup



class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed



class Dog:
    mammal = True

    def init(self, name, age, nature="Good", breed="Unknown"):
        self.name = name
        self.age = age
        self.nature = nature
        self.breed = breed

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Nature: {self.nature}, Breed: {self.breed}"

    def show_info(self):
        print(self.get_info())

    def bark(self):
        print(f"{self.name} says: Woof!")


class Labrador(Dog):
    def fetch(self):
        print(f"{self.name} is fetching the ball!")


class Bulldog(Dog):
    def snore(self):
        print(f"{self.name} is snoring loudly!")

class Pets:
    def __init__(self):
        self.pet_list = []

    def add_pet(self, pet):
        self.pet_list.append(pet)

    def show_pets(self):
        for pet in self.pet_list:
            pet.show_info()



class Buffer:
    def __init__(self):
        self.data = []

    def add(self, *a):
        self.data.extend(a)
        while len(self.data) >= 5:
            s = sum(self.data[:5])
            print(f"Сума п'ятірки: {s}")
            self.data = self.data[5:]

    def get_current_part(self):
        return self.data



class NameLengthError(ValueError):
    pass

def check_name(name):
    if len(name) < 10:
        raise NameLengthError("Довжина імені менше 10 символів!")



class DecimalToRoman:
    def __init__(self):
        self.val = [
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
        ]
        self.sym = [
            "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
        ]

    def convert(self, num):
        res = ""
        for i, v in enumerate(self.val):
            while num >= v:
                num -= v
                res += self.sym[i]
        return res

class RomanToDecimal:
    def __init__(self):
        self.rom_val = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    def convert(self, s):
        res = 0
        prev = 0
        for c in reversed(s):
            curr = self.rom_val[c]
            if curr < prev:
                res -= curr
            else:
                res += curr
            prev = curr
        return res



class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Shop: {self.shop_name}, Type: {self.store_type}")

    def open_shop(self):
        print(f"Онлайн-магазин {self.shop_name} відкритий!")

    def set_number_of_units(self, n):
        self.number_of_units = n

    def increment_number_of_units(self, n):
        self.number_of_units += n

class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products=None):
        super().__init__(shop_name, store_type)
        self.discount_products = discount_products or []

    def get_discount_products(self):
        print(f"Товари зі знижкою: {self.discount_products}")



class User:
    def __init__(self, first_name, last_name, email="", nickname="", subscribe=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.nickname = nickname
        self.subscribe = subscribe
        self.login_attempts = 0

    def describe_user(self):
        print(f"Full name: {self.first_name} {self.last_name}")

    def greeting_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts =0

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for p in self.privileges:
            print("-", p)

class Admin(User):
    def __init__(self, first_name, last_name, email="", nickname="", subscribe=False):
        super().__init__(first_name, last_name, email, nickname, subscribe)
        self.privileges = Privileges([
            "Allowed to add message",
            "Allowed to delete users",
            "Allowed to ban users"
        ])



while True:
    print("\n==========================")
    print("     ВИБЕРІТЬ ЗАВДАННЯ")
    print("==========================")
    print("1 — Bank")
    print("2 — Coin toss")
    print("3 — Car")
    print("4 — Dog & Pets")
    print("5 — Buffer")
    print("6 — Name length check")
    print("7 — Roman conversion")
    print("8 — Shop & Discount")
    print("9 — User & Admin")
    print("0 — Вийти з програми")
    print("==========================")

    choice = input("Ваш вибір: ")

    if choice == "1":
        bank = Bank(1000)
        bank.deposit(500)
        bank.withdraw(200)
        print(f"Поточний баланс: {bank.get_balance()}")

    elif choice == "2":
        coin = Coin()
        n = 5
        for i in range(n):
            print(f"Підкидання {i+1}: {coin.toss()}")

    elif choice == "3":
        car = Car("Toyota", "Corolla", 2020)
        for _ in range(5):
            car.accelerate()
            print(f"Speed: {car.get_speed()}")
        for _ in range(5):
            car.brake()
            print(f"Speed: {car.get_speed()}")

    elif choice == "4":
        dog1 = Labrador("Арчі", 3)
        dog2 = Bulldog("Буль", 5)
        dog3 = Dog("Рекс", 2)
        pets = Pets()
        pets.add_pet(dog1)
        pets.add_pet(dog2)
        pets.add_pet(dog3)
        pets.show_pets()
        dog1.fetch()
        dog2.snore()
        dog3.bark()

    elif choice == "5":
        buf = Buffer()
        buf.add(1,2,3)
        buf.add(4,5,6)
        buf.add(7,8)
        print("Поточні елементи:", buf.get_current_part())

    elif choice == "6":
        try:
            check_name("Short")
        except NameLengthError as e:
            print(e)

    elif choice == "7":
        dec_to_roman = DecimalToRoman()
        roman_to_dec = RomanToDecimal()
        num = 1994
        roman = dec_to_roman.convert(num)
        print(f"{num} = {roman}")
        print(f"{roman} = {roman_to_dec.convert(roman)}")

    elif choice == "8":
        shop = Shop("MyShop", "Online")
        shop.describe_shop()
        shop.open_shop()
        shop.set_number_of_units(10)
        print(f"Number of units: {shop.number_of_units}")
        shop.increment_number_of_units(5)
        print(f"Number of units: {shop.number_of_units}")
        discount_shop = Discount("DiscountShop", "Retail", ["Milk", "Bread"])
        discount_shop.get_discount_products()

    elif choice == "9":
        user = User("Ivan", "Ivanov", "ivan@mail.com", "ivan123", True)
        user.describe_user()
        user.greeting_user()
        user.increment_login_attempts()
        user.increment_login_attempts()
        print(f"Login attempts: {user.login_attempts}")
        user.reset_login_attempts()
        print(f"Login attempts after reset: {user.login_attempts}")
        admin = Admin("Admin", "User")
        admin.privileges.show_privileges()

    elif choice == "0":
        print("Програма завершена.")
        break

    else:
        print("Невірний вибір! Введіть 0-9.")
