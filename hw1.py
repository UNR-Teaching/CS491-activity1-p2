from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def __init__(self, color = "none", name = "none"):
        print("Creating car object ...")
        self._color = color
        self._name = name
        self._engine = Engine()
        Wheels(4)

    def getColor(self):
        return self._color
    
    def setColor(self, x):
        self._color = x
    
    def delColor(self):
        del self._color

    def getName(self):
        return self._name
    
    def setName(self, x):
        self._name = x

    def delName(self):
        del self._name
    
    color = property(getColor, setColor, delColor, )
    name = property(getName, setName, delName, )

    def move(self):
        self._engine.startEngine()
        print("Driving" ,self._name, "...")

class Bike(Vehicle):
    def __init__(self, color = "none", name = "none"):
        print("Creating bike object ...")
        self._color = color
        self._name = name
        Wheels(2)

    def getColor(self):
        return self._color
    
    def setColor(self, x):
        self._color = x
    
    def delColor(self):
        del self._color

    def getName(self):
        return self._name
    
    def setName(self, x):
        self._name = x

    def delName(self):
        del self._name
    
    color = property(getColor, setColor, delColor, )
    name = property(getName, setName, delName, )

    def move(self):
        print("Pedaling" ,self._name, "...")

class Wheels:
    def __init__(self, x=0):
        print(x, "wheels created.")


class Engine:
    def __init__(self):
        print("Engine created.")
    
    def startEngine(self):
        print("Engine started.")
    
def main():
    print("Car class instantiation/tests")
    car0 = Car("blue","Miata")

    print("\nGetting car color and name")
    print(car0.color)
    print(car0.name)
   
    print("\nMoving Car object")
    car0.move()

    print("\nBike class instantiation/tests")
    bike0 = Bike("silver","BMX")

    print("\nGetting Bike color and name")
    print(bike0.color)
    print(bike0.name)
   
    print("\nMoving Bike object")
    bike0.move()




if __name__ == "__main__":
    main()    
    
