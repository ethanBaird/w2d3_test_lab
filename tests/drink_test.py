import unittest

# from src.pub import Pub
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Tennents", 3.50, 4.0, 100)
    
    def test_drink_has_name(self):
        self.assertEqual("Tennents", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(3.50, self.drink.price)

    def test_drink_has_alcohol(self):
        self.assertEqual(4.0, self.drink.alcohol_units)

    def test_drink_in_stock(self):
        self.assertEqual(True, self.drink.in_stock())

    def test_drink_stock_level(self):
        self.assertEqual(100, self.drink.check_stock())

    def test_can_restock(self):
        self.drink.restock(50)
        self.assertEqual(150, self.drink.stock)
    
    def test_drink_can_reduce_stock(self):
        self.drink.reduce_stock()
        self.assertEqual(99, self.drink.stock)
    
            