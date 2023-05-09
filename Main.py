from laptop_manufacturer import LaptopManufacturer
from ultrabook_factory import UltrabookFactory
from business_factory import BusinessFactory
from gaming_factory import GamingFactory

if __name__ == "__main__":
    manufacturer = LaptopManufacturer.get_instance()

    ultrabook_factory = UltrabookFactory()
    manufacturer.manufacture_laptops(ultrabook_factory, 2)
    business_factory = BusinessFactory()
    manufacturer.manufacture_laptops(business_factory, 2)
    gaming_factory = GamingFactory()
    manufacturer.manufacture_laptops(gaming_factory, 2)

    laptops = manufacturer.get_laptops()

    for laptop in laptops:
        print("Model:", laptop.get_model(),
              "Color:", laptop.get_color(),
              "Memory:", laptop.get_memory(),
              "Size:", laptop.get_size(),
              "RAM:", laptop.get_ram(),
              "VRAM:", laptop.get_vram())
