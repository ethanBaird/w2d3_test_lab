import unittest

from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Ethan", 20, 27)
        self.drink = Drink("Absynth", 8, 5, 14)
        self.food = Food("Burger", 9, 5, 16)

    def test_customer_has_name(self):
        self.assertEqual("Ethan", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(27, self.customer.age)

    def test_customer_has_sufficient_funds(self):
        can_buy = self.customer.sufficient_funds(self.drink)
        self.assertEqual(True, can_buy)

    def test_customer_has_insufficent_finds(self):
        self.expensive_drink = Drink("Single Malt", 25, 10, 36)
        can_buy = self.customer.sufficient_funds(self.expensive_drink)
        self.assertEqual(False, can_buy)

    def test_customer_can_buy_drink(self):
        self.customer.buy_drink(self.drink)

        self.assertEqual(12, self.customer.wallet)
        self.assertEqual(5, self.customer.drunkenness)

    def test_customer_can_buy_food(self):
        self.customer.buy_drink(self.drink)
        self.customer.buy_food(self.food)

        self.assertEqual(3, self.customer.wallet)
        self.assertEqual(0, self.customer.drunkenness)