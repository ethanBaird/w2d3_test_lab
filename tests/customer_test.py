import unittest

from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Ethan", 20, 27)
        self.drink = Drink("Absynth", 8, 5)
        self.food = Food("Burger", 9, 5)

    def test_customer_has_name(self):
        self.assertEqual("Ethan", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(27, self.customer.age)

    def test_customer_can_reduce_cash(self):
        self.customer.reduce_cash(10)
        self.assertEqual(10, self.customer.wallet)

    def test_customer_can_increase_drunkenness(self):
        self.customer.increase_drunkenness(self.drink)
        self.assertEqual(5, self.customer.drunkenness)

    def test_customer_can_decrease_drunkenness(self):
        self.customer.increase_drunkenness(self.drink)
        self.customer.decrease_drunkenness(self.food)
        self.assertEqual(0, self.customer.drunkenness)