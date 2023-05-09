from laptop import Laptop

class LaptopManufacturer:
    _instance = None

    def __init__(self):
        self.laptops = []

    @staticmethod
    def get_instance():
        if LaptopManufacturer._instance is None:
            LaptopManufacturer._instance = LaptopManufacturer()
        return LaptopManufacturer._instance

    def manufacture_laptops(self, factory, quantity):
        for _ in range(quantity):
            laptop = factory.create_laptop()
            self.laptops.append(laptop.clone())

    def get_laptops(self):
        return self.laptops
