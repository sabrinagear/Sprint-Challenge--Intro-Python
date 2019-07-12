# class hierarchy exercise

# base
class Vehicle: 
    def __init__(self):
        pass

class FlightVehicle(Vehicle):
    def __init__(self):
        super()
        pass

class Starship(FlightVehicle):
    def __init__(self):
        super()
        pass

class Airplane(FlightVehicle):
    def __init__(self):
        super()
        pass

class GroundVehicle(Vehicle):
    def __init__(self):
        super()
        pass

class Motorcycle(GroundVehicle):
    def __init__(self):
        super()
        pass

class Car(GroundVehicle):
    def __init__(self):
        super()
        pass
