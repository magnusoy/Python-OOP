# Opprette en klasse med en metode
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def born_in(self, current_year=2021):
        return current_year - self.age


# Lag et objekt og benytt metoden
p1 = Person("Magnus", 26)
print(p1.born_in())
