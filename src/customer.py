class Customer:

    def __init__(self, _name, _wallet, _age):
        self.name = _name
        self.wallet = _wallet
        self.age = _age
        self.drinks = []
        self.drunkenness = 0

    def reduce_cash(self, amount):
        self.wallet -= amount


    def get_drink(self, drink):
        self.drinks.append(drink)

    def num_of_drinks(self):
        return len(self.drinks)

    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_units
    
    
    