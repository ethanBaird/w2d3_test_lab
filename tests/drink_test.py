import unittest

# from src.pub import Pub
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Tennents", 3.50, 4.0)
    
    def test_drink_has_name(self):
        self.assertEqual("Tennents", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(3.50, self.drink.price)

    def test_drink_has_alcohol(self):
        self.assertEqual(4.0, self.drink.alcohol_units)

    
            