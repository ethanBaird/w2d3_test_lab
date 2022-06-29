class Pub:
    
    #constructor
    def __init__(self, _name, _till):
        self.name = _name
        self.till = _till
        self.drinks = []

    def check_stock(self):
        return len(self.drinks)

    def add_drink(self, drink):
        self.drinks.append(drink)

    def remove_drink(self, drink):
        self.drinks.remove(drink)

    def increase_till(self, amount):
        self.till += amount

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        else: 
            return False

    def sell_drink(self, customer, drink):
        if self.check_age(customer) == True:
            self.increase_till(drink.price)
            self.remove_drink(drink)
            customer.reduce_cash(drink.price)
            customer.get_drink(drink)
        else:
            pass


   

