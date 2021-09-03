# Inheritance and Subclasses

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
        self.price *= self.price_inc
        # Other way
        #self.price *= self.price_inc
        


# Subclass - 1    
class FuelCars(Car):
    """FuelCars is a sub-class of Car."""
    # Changing the price_inc for FuelCars
    price_inc:int = 1.02

    # Adding some extra instance variables to FuelCars
    def __init__(self, brand: str, model: str, price: int, fuel: str):
        # Calls the parent class' __init__() method
        # Usually sufficient when Single inheritance
        super().__init__(brand, model, price)
        # Another way - Used when there is Multiple inheritance
        #Car.__init__(brand, model, price)
        self.fuel = fuel


# Subclass - 2
class ElectricCars(Car):
    price_inc = 1.06

    def __init__(self, brand: str, model: str, price: int, isSelfDriving: bool):
        super().__init__(brand, model, price)
        self.isSelfDriving = isSelfDriving
    


# Driver Code    
obj1 = FuelCars('BMW', 'X3', 25000, 'Petrol')
print(obj1)

obj2 = ElectricCars('Tesla', 'S20', 12000, True)
print(obj2)

# To know Method Resolution Order and other details inherited from parent class
#help(FuelCars)
obj1.increase_price()
print(obj1.price)
obj2.increase_price()
print(obj2.price)
print(obj1.fuel)
