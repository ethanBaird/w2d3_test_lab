import unittest

from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub1 = Pub("Bannermans", 200.00)
        self.drink = Drink("Beer", 3.00, 2)

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

