class Customer:

    def __init__(self, _name, _wallet, _age):
        self.name = _name
        self.wallet = _wallet
        self.age = _age
        self.drunkenness = 0

    def sufficient_funds(self, item):
        return self.wallet >= item.price

    def buy_drink(self, drink):
        if self.sufficient_funds(drink) == True:
            self.wallet -= drink.price
            self.drunkenness += drink.alcohol_units

    def buy_food(self, food):
        if self.sufficient_funds(food) == True:
            self.wallet -= food.price
            self.drunkenness -= food.rejuvenation_level
    
    
    