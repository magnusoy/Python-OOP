# Superclass
class Animal:

    def __init__(self, color='brown', sound='Unknown'):
        self.color = color
        self.sound = sound
    
    def makes_sound(self):
        print(self.sound)

# Subclass
class Dog(Animal):

    def __init__(self, color, sound):
        super().__init__(color, sound)
    
    def makes_sound(self):
        return self.sound

# Subclass
class Cat(Animal):

    def __init__(self, color, sound):
        super().__init__(color, sound)
    
    def makes_sound(self):
        return self.sound


dog = Dog('white', 'BARK!')
cat = Cat('white', 'MEOW!')

print(f"The Dog says: {dog.makes_sound()} and the Cat says: {cat.makes_sound()}")