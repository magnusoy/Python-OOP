"""
Oppgave 1

Lag underordnet klasse Buss som vil
arve alle variablene og metodene i kjøretøyklassen .
"""

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", school_bus.name, "Speed:", school_bus.max_speed, "Mileage:", school_bus.mileage)


"""
Oppgave 2

Lag underordnet klasse Buss som vil
arve alle variablene og metodene i kjøretøyklassen .
"""

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

school_bus = Bus("School Volvo", 180, 12)
print(school_bus.seating_capacity())


"""
Oppgave 3

Bestem hvilken klasse et gitt bussobjekt tilhører (sjekk type objekt) 
"""

print(type(school_bus))


"""
Oppgave 4

Bestem om School_bus også er en forekomst av kjøretøyklassen 
"""

print(isinstance(school_bus, Vehicle))