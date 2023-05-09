import random
from laptop_builder_impl import LaptopBuilderImpl
from laptop_factory import LaptopFactory

class GamingFactory(LaptopFactory):
    def __init__(self):
        self.available_colors = ["White", "Black", "Red", "Blue", "Silver"]
        self.available_size = [14, 15.6, 16.2, 17.3]
        self.available_memory = [512, 1024, 2048]
        self.available_ram = [16, 24, 32]
        self.available_vram = [4, 6, 8]

    def create_laptop(self):
        builder = LaptopBuilderImpl()
        builder.set_model("Gaming")
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
