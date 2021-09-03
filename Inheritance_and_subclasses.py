# Class methods and Static methods
class Car:
    # class variables
    car_type: str = 'Hatchback'
    price_inc: int = 1.05
    no_of_cars: int = 0

    def __init__(self, brand: str, model: str, price: int):
        # Instance variables
        self.brand = brand
        self.model = model
        self.price = price
        # This should be Class name and not the instance
        Car.no_of_cars += 1

    def __str__(self):
        return f'{self.brand} - {self.model}\'s object'


    def increase_price(self):
        # Using a class variable - one way
        self.price *= Car.price_inc
        # Other way
        #self.price *= self.price_inc
        return f'Total Price: Rs. {self.price}'

    @classmethod
    def set_price_inc(cls, amount):
        """Sets the price_inc of the class."""
        cls.price_inc = amount


    @classmethod
    def create_instance_from_comma_separated_string(cls, cs):
        """Creates an object from a comma separated string."""
        brand, model, price = cs.split(',')
        return cls(brand, model, int(price))

    """Static methods do not take any arguments like self or cls. They are just
       like normal function that has some logical connection to our class.
       If a method doesn't use any of instance/class varaibles/methods then that
       method is a good candidate for Staticmethod
       """

    @staticmethod
    def is_workday(day):
        if day.weekday() in (5,6):
            return False
        return True

# Driver Code    
obj1 = Car('BMW', 'X3', 25000)
print(obj1)

obj2 = Car('Mahindra', 'XUV700', 12000)
print(obj2)

print(f'Before:')
print(Car.price_inc)
print(obj1.price_inc)
print(obj2.price_inc)

# Calling the class method
Car.set_price_inc(1.26)
# Even this will change the price_inc
#obj1.set_price_inc(1.26)

print(f'After:')
print(Car.price_inc)
print(obj1.price_inc)
print(obj2.price_inc)

# Create an object from comma separated stirng
obj3 = Car.create_instance_from_comma_separated_string('Audi, A8, 22000')
print(obj3)


# Using a staticmethod
import datetime
tod = datetime.date(2021, 4, 8)
print(Car.is_workday(tod))
