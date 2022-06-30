class Food:
    def __init__(self, _name, _price, _rejuvenation_level, _stock):
        self.name = _name
        self.price = _price
        self.rejuvenation_level = _rejuvenation_level
        self.stock = _stock

    def in_stock(self):
        return self.stock > 0

    def check_stock(self):
        return self.stock

    def reduce_stock(self):
        self.stock -= 1


    
