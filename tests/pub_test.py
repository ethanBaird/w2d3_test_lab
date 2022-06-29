import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub1 = Pub("Bannermans", 200.00)
        self.drink = Drink("Beer", 3.00, 2)
        self.customer = Customer("Pep", 10, 21)
        self.customer1 = Customer("Ethan", 20, 17)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    # @unittest.skip("delete this line to run the test")
    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    # @unittest.skip("delete this line to run the test")
    def test_pub_has_drinks(self):
        self.assertEqual(0, self.pub.check_stock())

    # @unittest.skip("delete this line to run the test")
    def test_pub_can_add_drinks(self):
        self.pub.add_drink(self.drink)
        self.assertEqual (1, self.pub.check_stock())

    # @unittest.skip("delete this line to run the test")
    def test_pub_can_remove_drinks(self):
        self.pub.add_drink(self.drink)
        self.pub.remove_drink(self.drink)
        self.assertEqual(0, self.pub.check_stock())

    def test_pub_can_increase_till(self):
        self.pub.increase_till(500)
        self.assertEqual(600.00, self.pub.till)

    def test_pub_can_check_customer_age(self):
        customer_over_18 = self.pub.check_age(self.customer)
        self.assertEqual(True, customer_over_18)
        customer_under_18 = self.pub.check_age(self.customer1)
        self.assertEqual(False, customer_under_18)



