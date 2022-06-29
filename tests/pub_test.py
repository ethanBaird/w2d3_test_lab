import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink = Drink("Beer", 3.00, 5)
        self.customer = Customer("Pep", 10, 21)
        self.customer1 = Customer("Ethan", 20, 17)
        self.food = Food("Burger", 9, 5)

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

    def test_pub_can_check_if_drunk__customer_sober(self):
        is_drunk = self.pub.check_if_drunk(self.customer)
        self.assertEqual(False, is_drunk)
        
    def test_pub_can_check_if_drunk__customer_drunk(self):
        self.customer.increase_drunkenness(self.drink)
        self.customer.increase_drunkenness(self.drink)
        self.customer.increase_drunkenness(self.drink)
       
        is_drunk = self.pub.check_if_drunk(self.customer)
        self.assertEqual(True, is_drunk)

    def test_pub_can_sell_drink(self):
        self.pub.add_drink(self.drink)
        
        self.pub.sell_drink(self.customer, self.drink)
        
        self.assertEqual(103.00, self.pub.till)
        self.assertEqual(7.00, self.customer.wallet)
        self.assertEqual(0,self.pub.check_stock())
        self.assertEqual(1, self.customer.num_of_drinks())

    def test_pub_can_check_age_before_sale_customer_over_18(self):
        self.pub.add_drink(self.drink)

        self.pub.sell_drink(self.customer, self.drink)

        self.assertEqual(True, self.pub.check_age(self.customer))
        self.assertEqual(103.00, self.pub.till)
        self.assertEqual(7.00, self.customer.wallet)
        self.assertEqual(0,self.pub.check_stock())
        self.assertEqual(1, self.customer.num_of_drinks())

    # @unittest.skip("delete")
    def test_pub_can_check_age_before_sale_customer_under_18(self):
        self.pub.add_drink(self.drink)

        self.pub.sell_drink(self.customer1, self.drink)

        self.assertEqual(False, self.pub.check_age(self.customer1))
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(10.00, self.customer.wallet)
        self.assertEqual(1,self.pub.check_stock())
        self.assertEqual(0, self.customer.num_of_drinks())

    # @unittest.skip("skipping for now")
    def test_pub_can_check_drunkenness_before_sale__customer_sober(self):
        self.pub.add_drink(self.drink)

        self.pub.sell_drink(self.customer, self.drink)

        self.assertEqual(False, self.pub.check_if_drunk(self.customer))
        self.assertEqual(True, self.pub.check_age(self.customer))
        self.assertEqual(103.00, self.pub.till)
        self.assertEqual(7.00, self.customer.wallet)
        self.assertEqual(0,self.pub.check_stock())
        self.assertEqual(1, self.customer.num_of_drinks())

    def test_pub_can_check_drunkenness_before_sale__customer_drunk(self):
        self.customer.increase_drunkenness(self.drink)
        self.customer.increase_drunkenness(self.drink)
        self.customer.increase_drunkenness(self.drink)
        
        self.pub.add_drink(self.drink)

        self.pub.sell_drink(self.customer, self.drink)

        self.assertEqual(True, self.pub.check_if_drunk(self.customer))
        self.assertEqual(True, self.pub.check_age(self.customer))
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(10.00, self.customer.wallet)
        self.assertEqual(1,self.pub.check_stock())
        self.assertEqual(0, self.customer.num_of_drinks())

    def test_pub_can_sell_food(self):
        self.pub.add_food(self.food)

        self.pub.sell_food(self.customer, self.food)

        self.assertEqual(109.00, self.pub.till)
        self.assertEqual(1, self.customer.wallet)
        self.assertEqual(0, self.pub.check_food_stock())
        self.assertEqual(1, self.customer.num_of_food())




        



