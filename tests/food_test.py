import unittest

from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Burger", 9, 5, 16)

    def test_food_has_name(self):
        self.assertEqual("Burger", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(9, self.food.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual(5, self.food.rejuvenation_level)

    def test_food_in_stock(self):
        self.assertEqual(True, self.food.in_stock())

    def test_food_out_of_stock(self):
        self.none_left = Food("Macaroni", 10, 4, 0)
        self.assertEqual(False, self.none_left.in_stock())

    def test_food_can_check_stock(self):
        stock_level = self.food.check_stock()
        self.assertEqual(16, stock_level)

    def test_food_can_reduce_stock(self):
        self.food.reduce_stock()
        self.assertEqual(15, self.food.stock)

    



