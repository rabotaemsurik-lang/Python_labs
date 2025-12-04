class House:


    def __init__(self, area=0, price=0):
        # Перевірки валідності параметрів
        if not isinstance(area, (int, float)) or area <= 0:
            raise ValueError("area має бути додатним числом")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("price має бути додатним числом")

        self._area = area
        self._price = price

    def final_price(self, discount: float):

        if not isinstance(discount, (int, float)):
            raise TypeError("discount має бути числом")
        if discount < 0 or discount > 100:
            raise ValueError("discount має бути в межах 0–100")

        return self._price * (1 - discount / 100)


class SmallHouse(House):


    def __init__(self, price=0):
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("price має бути додатним числом")

        super().__init__(area=40, price=price)


class Human:


    default_name = "NoName"
    default_age = 18

    def __init__(self, name=None, age=None, money=0, house=None):
        # Ім'я
        if name is None:
            name = Human.default_name
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("name має бути непорожнім рядком")

        # Вік
        if age is None:
            age = Human.default_age
        if not isinstance(age, (int, float)) or age <= 0:
            raise ValueError("age має бути додатним числом")

        # Гроші
        if not isinstance(money, (int, float)) or money < 0:
            raise ValueError("money має бути числом ≥ 0")

        # Будинок
        if house is not None and not isinstance(house, House):
            raise TypeError("house має бути об'єктом класу House або None")

        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    @staticmethod
    def default_info():

        print(f"Default name: {Human.default_name}, Default age: {Human.default_age}")

    def info(self):

        print("\n=== Human info ===")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Money: {self.__money}")
        print(f"House: {self.__house if self.__house else 'No house'}")
        print("=================")

    def __make_deal(self, house: House, price: float):


        if not isinstance(house, House):
            raise TypeError("house має бути об'єктом класу House")

        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("price має бути числом > 0")

        self.__money -= price
        self.__house = house

    def earn_money(self, amount: float):

        if not isinstance(amount, (int, float)):
            raise TypeError("amount має бути числом")
        if amount <= 0:
            raise ValueError("amount має бути більше нуля")

        self.__money += amount
        print(f"\n{self.name} заробив {amount}$. Тепер у нього {self.__money}$.")

    def buy_house(self, house: House, discount: float = 10):

        if not isinstance(house, House):
            raise TypeError("house має бути об'єктом класу House")

        price = house.final_price(discount)

        if self.__money < price:
            print(f"\nНедостатньо грошей! Потрібно {price}$, є тільки {self.__money}$.")
            return False

        self.__make_deal(house, price)
        print(f"\nУспішно куплено будинок за {price}$.")
        return True
