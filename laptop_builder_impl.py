from laptop import Laptop
from laptop_builder import LaptopBuilder

class LaptopBuilderImpl(LaptopBuilder):
    def __init__(self):
        self.model = None
        self.color = None
        self.memory = None
        self.size = None
        self.ram = None
        self.vram = None

    def set_model(self, model):
        self.model = model

    def set_color(self, color):
        self.color = color

    def set_memory(self, memory):
        self.memory = memory

    def set_size(self, size):
        self.size = size

    def set_ram(self, ram):
        self.ram = ram

    def set_vram(self, vram):
        self.vram = vram

    def build(self):
        return Laptop(self.model, self.color, self.memory, self.size, self.ram, self.vram)
