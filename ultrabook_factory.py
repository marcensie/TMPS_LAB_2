import random
from laptop_builder_impl import LaptopBuilderImpl
from laptop_factory import LaptopFactory

class UltrabookFactory(LaptopFactory):
    def __init__(self):
        self.available_colors = ["White", "Black", "Red", "Blue", "Silver"]
        self.available_size = [13.3, 14, 15.6]
        self.available_memory = [256, 512, 1024]
        self.available_ram = [8, 16]
        self.available_vram = [1, 2]

    def create_laptop(self):
        builder = LaptopBuilderImpl()
        builder.set_model("Ultrabook")
        color = random.choice(self.available_colors)
        builder.set_color(color)
        memory = random.choice(self.available_memory)
        builder.set_memory(memory)
        size = random.choice(self.available_size)
        builder.set_size(size)
        ram = random.choice(self.available_ram)
        builder.set_ram(ram)
        vram = random.choice(self.available_vram)
        builder.set_vram(vram)
        return builder.build()
