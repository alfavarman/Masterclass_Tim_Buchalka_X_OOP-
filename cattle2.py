class Kettle(object):

    power_source = 'Electricity'

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.switch = False

    def switch_on(self):
        self.on = True

kenwood = Kettle('Kenwood', 8.99)
hamilton = Kettle('Hamilton', 14.93)

print(kenwood.make)
print(kenwood.price)
kenwood.power = 1.5
print(kenwood.power)

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)