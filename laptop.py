class Laptop:
    def __init__(self, model, color, memory, size, ram, vram):
        self.model = model
        self.color = color
        self.memory = memory
        self.size = size
        self.ram = ram
        self.vram = vram

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def get_memory(self):
        return self.memory

    def get_size(self):
        return self.size
    
    def get_ram(self):
        return self.ram
    
    def get_vram(self):
        return self.vram

    def clone(self):
        return Laptop(self.model, self.color, self.memory, self.size, self.ram, self.vram)
