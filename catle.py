class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood = Kettle('kenwood', 8.99)
print(kenwood.make)
print(kenwood.price)

