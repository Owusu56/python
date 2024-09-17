class SoftwareEngineer:
    first_name = None
    surname = None
    other = None
    student_id = None
    age = None

    # CONSTRUCTOR or INITIALIZER
    def __init__(self, First_Name, Surname, Other, Student_Id, Age):
        self.first_name = First_Name
        self.surname = Surname
        self.other = Other
        self.student_id = Student_Id
        self.age = Age

    # SETTERS and GETTERS

    def setFirst_Name(self, First_Name):
        self.first_name = First_Name

    def getFirstName(self):
        return self.first_name


object = SoftwareEngineer("Pauson", "Chills", "Kay", "SE00024", "23")

object.setFirst_Name("Bra Panin")

print(object.getFirstName())
