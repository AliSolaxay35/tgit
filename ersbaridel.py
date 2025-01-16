class Laptop:
    count = 0

    def __init__(self, ram, hard, cpu):
        Laptop.count += 1
        self.ram = ram
        self.hard = hard
        self.cpu = cpu

    def value(self):
        return self.ram + self.hard + self.cpu

    def __del__(self):
        Laptop.count -= 1


class Computer(Laptop):
    def value(self):
        return self.ram + self.hard + self.cpu


pc1 = Laptop(12, 2, 4)
print(pc1.value())
print("Laptop count:", Laptop.count) 
del pc1
print("Laptop count after deletion:", Laptop.count)  

computer1 = Computer(16, 2, 4)
computer1.size = 15
print(computer1.value())