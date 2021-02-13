"""
Oppgave 1
Lag en klasse som representerer en person: Person
som innholder egenskapene:
    - Navn
    - Alder
    - Høyde
    - Vekt
"""


"""
Oppgave 2
Bruk Person klassen og utvid funksjonalitet med å legge til
en representasjon metode og bruk den.
"""


"""
Oppgave 4
Bruk Person klassen og utvid funksjonalitet med å legge til
en format metode og bruk den.
"""

# All in one solution
class Person:

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def __repr__(self):
        return f"Person:\nNavn: {self.name}\nAlder: {self.age}\nHøyde: {self.height}\nVekt: {self.weight}"
    
    def __str__(self):
        return f"{self.name} er en person som er {self.age} år gammel og er {self.weight} kg tung med sine {self.height} cm."


person = Person("Magnus", 25, 180, 100)
print(repr(person))
print(person)