# Opprette en klasse
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Lag objekter fra klassen
p1 = Person("Magnus", 25)
p2 = Person("Hans", 26)
p3 = Person("Kari", 27)


# Sammenligne egenskapene til objekter
if p1.age > p2.age:
    print(f"{p1.name} er gamlere enn {p2.name}")
else:
    print(f"{p2.name} er gamlere enn {p1.name}")