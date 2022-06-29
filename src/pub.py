class Pub:
    
    #constructor
    def __init__(self, _name, _till):
        self.name = _name
        self.till = _till

    def increase_till(self, item):
        self.till += item.price

    def can_buy(self, customer):
        return customer.age >= 18 and customer.drunkenness < 12
           
    def sell_drink(self, customer, drink):
        if drink.in_stock() == True and self.can_buy(customer) == True:
                customer.buy_drink(drink)
                self.increase_till(drink)
                drink.reduce_stock()
        else:
            pass

    def sell_food(self, customer, food):
        self.increase_till(food)
        customer.buy_food(food)
        food.reduce_stock()




   

