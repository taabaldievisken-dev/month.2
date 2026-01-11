class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive_to(self, destination):
        print(f"Bus_100 {self.model} Driving to in Karakol")
        print(f"number {self.model} 01KG777AWM")


class Bus(Car):
    def __init__(self, model, color, number):
        super().__init__(model, color)
        self.number = number

bus_100= Bus("ZHONGTONG", "black", "bus_100")
print(bus_100.color)
bus_100.drive_to("Bishkek")

