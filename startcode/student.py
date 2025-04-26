class Student:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd
    def stelVoor(self):
        print(f"Ik ben {self.naam} en {self.leeftijd} jaar oud")

Milan = Student("Milan", 12)
Arthur = Student("Arthur", 13)
#Milan.stelVoor()