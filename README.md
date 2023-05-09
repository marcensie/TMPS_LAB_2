# TMPS_LAB_2 - Laptop manufacturing system
## by Jardan Alexandru

## Objective :
Implement some creational design patterns for object instantiation in a  project

### Builder: The LaptopBuilder class is an abstract base class defining the interface for building a laptop. It has abstract methods for setting the laptop's model, color, memory, size, RAM, VRAM, and a method for building the laptop itself. The LaptopBuilderImpl class is a concrete implementation of the LaptopBuilder interface. It provides methods for setting the different attributes of a laptop and implements the build() method to create a Laptop object with the specified attributes. The UltrabookFactory class acts as a concrete factory that utilizes the LaptopBuilderImpl to create Ultrabook laptops with random attributes. It demonstrates the usage of the builder pattern by setting the attributes of the laptop using the builder's methods (set_model(), set_color(), etc.) before finally calling build() to obtain the constructed Laptop object. Overall, the code follows the principles of the Builder pattern by separating the construction of a Laptop object from its representation and providing a flexible way to create different configurations of laptops.
```
class LaptopBuilder(ABC):
    @abstractmethod
    def set_model(self, model):
        pass

    @abstractmethod
    def set_color(self, color):
        pass
......
    @abstractmethod
    def build(self):
        pass

class LaptopBuilderImpl(LaptopBuilder):
    def __init__(self):
        self.model = None
        self.color = None

    def set_model(self, model):
        self.model = model

    def set_color(self, color):
        self.color = color
......
    def build(self):
        return Laptop(self.model, self.color, self.memory, self.size, self.ram, self.vram)

class UltrabookFactory(LaptopFactory):
......
    def create_laptop(self):
        builder = LaptopBuilderImpl()
        builder.set_model("Ultrabook")
        color = random.choice(self.available_colors)
        builder.set_color(color)
        return builder.build()
```
### Singleton: The _instance variable is used to store the singleton instance, and the get_instance() method ensures that only one instance of LaptopManufacturer is created. When get_instance() is called, it checks if _instance is None. If it is, a new instance of LaptopManufacturer is created and assigned to _instance. Subsequent calls to get_instance() will return the existing instance instead of creating a new one. This ensures that throughout the program, there is only one instance of LaptopManufacturer available, making it a Singleton.
```
class LaptopManufacturer:
    _instance = None

 def get_instance():
        if LaptopManufacturer._instance is None:
            LaptopManufacturer._instance = LaptopManufacturer()
        return LaptopManufacturer._instance

```
### Prototype: The Laptop class serves as the prototype. It has a clone() method that creates a new Laptop object with the same attributes as the original object. This allows for creating new instances of Laptop by cloning existing instances. The LaptopManufacturer class acts as the client and utilizes the prototype pattern. It maintains a list of Laptop objects and uses a factory to create new laptops. The manufacture_laptops() method demonstrates the prototype pattern by calling the factory's create_laptop() method to obtain a new laptop and then cloning it using the clone() method before adding it to the list of manufactured laptops. By using the prototype pattern, the LaptopManufacturer can create new laptop instances without explicitly specifying their concrete classes or relying on subtyping. Instead, it relies on the clone() method provided by the Laptop class to create new instances based on existing ones. 
```
class Laptop:
    def __init__(self, model, color, memory, size, ram, vram):
        self.model = model
        self.color = color
        self.memory = memory
        self.size = size
        self.ram = ram
        self.vram = vram 
......
    def clone(self):
        return Laptop(self.model, self.color, self.memory, self.size, self.ram, self.vram)
class LaptopManufacturer:
.....
def manufacture_laptops(self, factory, quantity):
        for _ in range(quantity):
            laptop = factory.create_laptop()
            self.laptops.append(laptop.clone())

```
### Abstract Factory: In the code, LaptopFactory is an abstract base class (ABC) that defines the create_laptop() method as an abstract method. This create_laptop() method is meant to be implemented by concrete laptop factories. The UltrabookFactory, BusinessFactory, and GamingFactory classes are concrete implementations of the LaptopFactory abstract class. Each factory class overrides the create_laptop() method and provides its own implementation to create specific types of laptops (Ultrabooks, Business laptops, and Gaming laptops). The LaptopManufacturer class acts as the client and utilizes the abstract factory pattern. It maintains a list of manufactured laptops and uses different concrete factory instances (UltrabookFactory, BusinessFactory, and GamingFactory) to create laptops of different types. Overall, the code demonstrates the use of the abstract factory pattern to create families of related objects (different types of laptops) without explicitly specifying their classes in the client code. The factories encapsulate the creation logic and allow for the creation of appropriate laptop objects based on the concrete factory implementation. 
```
class LaptopFactory(ABC):
    @abstractmethod
    def create_laptop(self):
        pass

class GamingFactory(LaptopFactory):
    def __init__(self):
        self.available_colors = ["White", "Black", "Red", "Blue", "Silver"]
        self.available_size = [14, 15.6, 16.2, 17.3]
....
    def create_laptop(self):
        builder = LaptopBuilderImpl()
        builder.set_model("Gaming")
        color = random.choice(self.available_colors)
        builder.set_color(color)
.....
        return builder.build()

if __name__ == "__main__":
    manufacturer = LaptopManufacturer.get_instance()

    ultrabook_factory = UltrabookFactory()
    manufacturer.manufacture_laptops(ultrabook_factory, 2)
    business_factory = BusinessFactory()
    manufacturer.manufacture_laptops(business_factory, 2)
    gaming_factory = GamingFactory()
    manufacturer.manufacture_laptops(gaming_factory, 2)

```


