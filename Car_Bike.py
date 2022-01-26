from curses import ACS_GEQUAL
from sys import builtin_module_names
from turtle import bk

class Vehicle:
    def __init__(Vehicle, color, age):
        Vehicle.color = color
        Vehicle.age = age
        set.color = "green"
        set.age = "5"
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
        Car.owner = owner
        set.owner = "Wayne"
        set.name = "Pinto"
        set.make = "Ford"
        pass

class Bike(Vehicle):
    def __init__(Bike, make, name, owner):
        Bike.name = name
        Bike.make = make
        Bike.owner = owner
        set.owner = "Garth"
        set.make = "BMX"
        set.name = "Bike"
    def pedal(Vehicle):
        print("Pushing P....")
        pass


