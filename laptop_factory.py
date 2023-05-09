from abc import ABC, abstractmethod
from laptop import Laptop

class LaptopFactory(ABC):
    @abstractmethod
    def create_laptop(self):
        pass
