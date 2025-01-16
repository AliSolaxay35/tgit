class laptab:
    count = 0
    def __init__(self, ram, hard, cpu):
        self.ram = ram
        self.hard = hard
        self.cpu = cpu

    def value(self):
        return self.ram + self.hard + self.cpu


pc1 = laptab(12, 2, 4)
pc2 = laptab(8, 4, 4)
print(pc1.value())
print(pc2.value())
