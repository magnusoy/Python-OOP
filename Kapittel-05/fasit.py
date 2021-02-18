"""
Oppgave 1

Lag en superklasse Person som har egenskapene
    - navn
    - alder
"""
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

"""
Oppgave 2

Lag en subklasse av Person som heter Employee og har egenskapene
    - lønn
"""

class Employee(Person):

    def __init__(self, emp_name, emp_age, emp_salary):
        super().__init__(emp_name, emp_age)
        self.emp_salary = emp_salary
    
    def display(self):
        super().display()
        print("Salary: ", self.emp_salary)


""" 
Oppgave 3

Utvid begge klassene til å ha sin egen "display" funksjon
som lister egenskapene.

Deretter legg til funksjonalitet i Employee "display" sånn
at den viser egenskapene til superklassen
"""

emp = Employee("Mari", 24, 600000)
emp.display()