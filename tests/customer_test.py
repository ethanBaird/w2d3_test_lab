import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Ethan", 20, 27)

    def test_customer_has_name(self):
        self.assertEqual("Ethan", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(27, self.customer.age)

    