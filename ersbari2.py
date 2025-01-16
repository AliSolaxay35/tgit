class Laptop:
    def __init__(self, ram, hard, cpu):
        self.ram = ram
        self.hard = hard
        self.cpu = cpu

    def value(self):
        return self.ram + self.hard + self.cpu

class Computer(Laptop):
    def value(self):
        return self.ram + self.hard + self.cpu + self.size
        

pc1 = Laptop(12, 2, 4)
print(pc1.value())

computer1 = Computer(16, 2, 4)
computer1.size = 15
print(computer1.value()) 