import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink = Drink("Beer", 3.00, 5, 100)
        self.customer = Customer("Pep", 10, 21)
        self.customer1 = Customer("Ethan", 20, 17)
        self.customer2 = Customer("Jon", 100, 21)
        self.food = Food("Burger", 9.00, 5, 16)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    # @unittest.skip("delete this line to run the test")
    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_can_increase_till(self):
        self.pub.increase_till(self.drink)
        self.pub.increase_till(self.food)
        self.assertEqual(112, self.pub.till)
        
    def test_pub_can_sell_drink(self):
        self.pub.sell_drink(self.customer, self.drink)
        
        self.assertEqual(103.00, self.pub.till)
        self.assertEqual(7.00, self.customer.wallet)
        self.assertEqual(99, self.drink.stock)

    # @unittest.skip("skip")
    def test_pub_can_sell_food(self):
        self.pub.sell_food(self.customer, self.food)

        self.assertEqual(109.00, self.pub.till)
        self.assertEqual(1, self.customer.wallet)
        self.assertEqual(15, self.food.stock)




        



