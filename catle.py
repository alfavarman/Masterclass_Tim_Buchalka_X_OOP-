class Kettle(object):

    power_source = 'electricity'

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

kenwood = Kettle('kenwood', 8.99)
print(kenwood.make)
print(kenwood.price)


kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle('hamilton', 7.33)
print(hamilton.make, hamilton.price)

# bc its objects can specify they atributes in replacement fields
print(f'Models:{kenwood.make} {kenwood.price}, {hamilton.make} {hamilton.price}')
print('Models:{} {}, {} {}'.format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print('Models:{0.make} {0.price}, {1.make} {1.price}'.format(kenwood, hamilton))


'''
class is a template for creating objects,
all ob created using same class will have the same caracteristics
object: an instance of a class
method: a function defined in the class
attribute: a variable bond to an instance of a class
'''

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

print('*' * 40)
kenwood.power = 1.5
print(kenwood.power)
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.power_source)
print('*' * 40)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
