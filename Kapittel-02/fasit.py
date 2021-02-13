"""
Oppgave 1

Lag en klasse som representerer en: Hest
Den trenger ikke å ha noen egenskaper
"""

class Horse:
    
    def __init__(self):
        pass

"""
Oppgave 2

Opprett en kjøretøyklasse med egenskaper
for maks. Hastighet og kjørelengde 
"""

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)

"""
Oppgave 3

Lag en klasse som representerer en: Datamaskin
Den skal inneholde egenskapene: cpu, ram, gpu, storage
"""

class Computer:

    def __init__(self, cpu, gpu, ram, storage):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.storage = storage


"""
Oppgave 4

Bruk klassen du laget i forrige oppgave
og lag 2 objekter av den.
"""

com_1 = Computer("Intel I7", "NVIDIA RTX 3080", "3200 MHZ", 120)
com_2 = Computer("Intel I7", "NVIDIA RTX 3080", "3200 MHZ", 230)


"""
Oppgave 5

Med de to objektene så er laget så ønsker
jeg å vite hvilken av de som har mest lagring.
"""

print("Computer 1 has the largest storage") if com_1.storage > com_2.storage else print("Computer 2 has the largest storage")