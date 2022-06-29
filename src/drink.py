class Drink:

    def __init__(self, _name, _price, _alcohol_units, _stock):
        self.name = _name
        self.price = _price
        self.alcohol_units = _alcohol_units
        self.stock = _stock

    def reduce_stock(self):
        self.stock -= 1
    
    

    