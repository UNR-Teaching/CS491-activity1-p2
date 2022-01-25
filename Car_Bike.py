from curses import ACS_GEQUAL

class Vehicle:
    def __init__(Vehicle, color, age):
        Vehicle.color = color
        Vehicle.age = age
        def start(Vehicle):
            print("Starting Up...")
        def drive(Vehicle):
            print("Zoom!...")
        def brake(Vehicle):
            print("Pumping The Brakes!...")
        def gas(Vehicle):
            print("Stepping on the Gas!...")
        pass

class Car(Vehicle):
    def __init__(Car, make, name, owner):
        Car.name = name
        Car.make = make
        set.owner = "Wayne"
        set.name = "Pinto"
        set.make = "Ford"
        pass

class Bike(Vehicle):
    def __init__(Bike, make, name):
        Bike.name = name
        Bike.make = make
        set.owner = "Garth"
        set.make = "BMX"

    def pedal(Vehicle):
        print("Pushing P....")
        pass


