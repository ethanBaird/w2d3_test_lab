class Pub:
    
    #constructor
    def __init__(self, _name, _till):
        self.name = _name
        self.till = _till
        self.drinks = []
        self.food = []

    def check_stock(self):
        return len(self.drinks)

    def check_food_stock(self):
        return len(self.food)

    def add_drink(self, drink):
        self.drinks.append(drink)

    def add_food(self, food):
        self.food.append(food)

    def remove_drink(self, drink):
        self.drinks.remove(drink)

    def remove_food(self, food):
        self.food.remove(food)

    def increase_till(self, amount):
        self.till += amount

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        else: 
            return False

    def check_if_drunk(self, customer):
        if customer.drunkenness >= 12:
            return True
        else:
            return False

    def sell_drink(self, customer, drink):
        if self.check_age(customer) == True and self.check_if_drunk(customer) == False:
            self.increase_till(drink.price)
            self.remove_drink(drink)
            customer.reduce_cash(drink.price)
            customer.get_drink(drink)
        else:
            pass

    def sell_food(self, customer, food):
        self.increase_till(food.price)
        self.remove_food(food)
        customer.reduce_cash(food.price)
        customer.get_food(food)




   

