class Car:
    car_type: str = 'Hatchback'
    price_inc: int = 5000

    def __init__(self, brand: str, model: str, price: int):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f'{self.brand} - {self.model}\'s object'


    def increase_price(self):
        self.price += 1000
        return f'Total Price: {self.price}'

    
obj1 = Car('BMW', 'X3', 25000)
print(obj1)
# One way of calling method
print(obj1.increase_price())

# Another way
print(Car.increase_price(obj1))
