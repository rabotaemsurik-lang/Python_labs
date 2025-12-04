from task2 import Human, SmallHouse, House
import pytest

def test_house_price_calc():
    h = House(50, 10000)
    assert h.final_price(10) == 9000

def test_human_buy_house_success():
    human = Human("Антон", 20, 10000)
    home = SmallHouse(5000)
    assert human.buy_house(home) is True

def test_human_buy_house_fail():
    human = Human("Антон", 20, 100)
    home = SmallHouse(5000)
    assert human.buy_house(home) is False

def test_human_earn_money():
    h = Human("Test", 18, 100)
    h.earn_money(50)
    # через приватність беремо через _Human__money
    assert h._Human__money == 150
