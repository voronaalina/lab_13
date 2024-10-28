class SWEET:
    def __init__(self, name, price, producer):
        self.name = name
        self.price = price
        self.producer = producer
    def set_name(self, new_name):
        self.name = new_name
    def set_price(self, new_price):
        self.price = new_price
    def display(self):
        print("назва:",self.name, " ціна:",self.price, " виробник:",self.producer)
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price