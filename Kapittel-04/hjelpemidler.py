# Opprette en klasse med representasjons metoder
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Bilen er fra {self.brand}og modellen er: {self.model} "
    
    def __repr__(self):
        return f"Car:\nName: {self.name}\nAge: {self.age}\nHeight: {self.height}\nWeight: {self.weight}"


car = Car("Tesla", "Model S")
print(repr(car))
print(car)
