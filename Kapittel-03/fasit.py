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

    def foot_to_meter(self, foot):
        return foot / 3.281

    def pound_to_kilogram(self, pound):
        return pound / 2.205

    def fahrenheit_to_celcius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

metric_converter = MetricConverter()

"""
Oppgave 2

Benytt deg av konverten som du laget i forrige oppgave.
Gitt listen som følger med oppgaven så skal du gjennomføre
en kovertering fra Pound til Kilogram på alle og lagre
resultatet i en ny liste.
"""

pounds = [180, 201, 289, 167, 142, 190, 154, 314]

kilograms = [int(metric_converter.pound_to_kilogram(pound)) for pound in pounds]
print(pounds)
print(kilograms)