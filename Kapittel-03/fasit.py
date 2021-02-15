"""
Oppgave 1

Du skal lage en klasse som representer en: MetricConverter
Den skal konvertere fra Imperial til metriske målinger
Følgende konverteringen skal finnes i klassen:
    - Fot til Meter | Formell: (Fot / 3.281)
    - Pound til Kilogram | Formell: (Pound / 2.205)
    - Fahrenheit til Celcius | Formell: (Fahrenheit - 32) * 5/9

"""

class MetricConverter:

    @staticmethod
    def feet_to_meter(feet):
        return feet / 3.281
    
    @staticmethod
    def pound_to_kilogram(pound):
        return pound / 2.205
    
    @staticmethod
    def fahrenheit_to_celcius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

"""
Oppgave 2

Benytt deg av konverten som du laget i forrige oppgave.
Gitt listen som følger med oppgaven så skal du gjennomføre
en kovertering fra Pound til Kilogram på alle og lagre
resultatet i en ny liste.
"""

pounds = [180, 201, 289, 167, 142, 190, 154, 314]

kilograms = [int(MetricConverter.pound_to_kilogram(pound)) for pound in pounds]
print(pounds)
print(kilograms)
