# Special methods - Magic/Dunder Operator overloading
class Car:
    car_type: str = 'Hatchback'
    price_inc: int = 5000

    def __init__(self, brand: str, model: str, price: int):
        self.brand = brand
        self.model = model
        self.price = price

    # Magic method - 1.
    # Is an unambiguous representation of object
    # Used by developers to know what is the object
    # used for debugging purposes
    # If there is no __str__, and you use str(obj) then this gets printed.
    # This should look like how we could create a Car object(see below)
    def __repr__(self):
        return f'Car({self.brand}, {self.model}, {self.price})'

    # Magic Method - 2
    # Used to denote a string representation of object
    # Used for the convenience of end users
    def __str__(self):
        return f'{self.brand} - {self.model}\'s object'

    def increase_price(self):
        self.price += 1000
        return f'Total Price: {self.price}'

    # Operator Overloading - +
    def __add__(self, other):
        return self.price + other.price


    def __len__(self):
        return len(self.brand + self.model)

    
obj1 = Car('BMW', 'X3', 25000)
print(repr(obj1))
print(str(obj1))
# One way of calling method
print(obj1.increase_price())

obj2 = Car('Audi', 'A3', 26000)
print(repr(obj2))

print(obj1 + obj2)
print(len(obj1))
print(len(obj2))
