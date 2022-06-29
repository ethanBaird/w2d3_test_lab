import unittest

from src.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub1 = Pub("Bannermans", 200.00)
        self.drink = Drink("Beer", 3.00, 2)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_no_drinks(self):
        self.assertEqual(0, len(self.pub.drinks))

    def test_pub_can_add_drinks(self):
        add_drink(self.drink)
        self.assertEqual (1, len(self.pub.drinks))

    def test_pub_can_remove_drinks(self):
        add_drink(self.drink)
        remove_drink(self.drink)
        self.assertEqual(0, self.pub.drinks)

