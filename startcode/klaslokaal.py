from student import Student

class KlasLokaal:
    def __init__(self):
        self.studenten = []

    def voeg_student_toe(self, student):
        self.studenten.append(student)

    def toon_studenten(self):
        for studenten in self.studenten:
            studenten.stelVoor()




student1 = Student("Milan", 12)
student2 = Student("Arthur", 13)
klaslokaal = KlasLokaal()
klaslokaal.voeg_student_toe(student1)
klaslokaal.voeg_student_toe(student2)
klaslokaal.toon_studenten()
