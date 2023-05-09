from abc import ABC, abstractmethod

class LaptopBuilder(ABC):
    @abstractmethod
    def set_model(self, model):
        pass

    @abstractmethod
    def set_color(self, color):
        pass

    @abstractmethod
    def set_memory(self, memory):
        pass

    @abstractmethod
    def set_size(self, size):
        pass

    @abstractmethod
    def set_ram(self, ram):
        pass

    @abstractmethod
    def set_vram(self, vram):
        pass

    @abstractmethod
    def build(self):
        pass
