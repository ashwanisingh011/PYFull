# Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    total_car = 0
    def __init__ (self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand
    
    def fullname(self):
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Modle S", "85kWh")
safari = Car("Tata", "Safari")
print(Car.total_car)