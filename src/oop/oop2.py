
# class GroundVehicle

class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    def drive(self):
        return f"vroooom"

# Subclass Motorcycle from GroundVehicle.

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__(2)
    
    def drive(self):
        return f"BRAAAP!!"

# list of vehicles

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

for x in vehicles:
    print(x.drive())
