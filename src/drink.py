class Drink:

    def __init__(self, _name, _price, _alcohol_units, _stock):
        self.name = _name
        self.price = _price
        self.alcohol_units = _alcohol_units
        self.stock = _stock
    
    def in_stock(self):
        return self.stock > 0
    
    def check_stock(self):
        if self.stock > 0:
            return self.stock
        else:
            return "This product is out of stock"

    def restock(self, amount):
        self.stock += amount

    def reduce_stock(self):
        self.stock -= 1
    
    

    