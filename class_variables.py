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

    

# Driver Code    
obj1 = Car('BMW', 'X3', 25000)
print(obj1)
print(obj1.increase_price())

obj2 = Car('Mahindra', 'XUV700', 12000)
print(obj2)
print(obj2.increase_price())

#Print the price_inc used by obj1. It takes from the Class unless it overrides that class variable
print(obj1.price_inc)
print(obj1.__dict__)

#Now uses the obj1's owne price_inc member. now price_inc is an instance variable of obj1
obj1.price_inc = 1.07
print(Car.price_inc)
print(obj1.price_inc)
print(obj1.__dict__)

print(Car.no_of_cars)
# same as above
print(obj1.no_of_cars)
