
class Personal_Information:
    first_name = None
    surname = None
    middle_name = None
    age = None

    def __init__(self, FirstName, Surname, MiddleName, Age):
        self.first_name = FirstName
        self.surname = Surname
        self.middle_name = MiddleName
        self.Age = Age

    def __init__(self, MiddleName, Age):
        self.middle_name = MiddleName
        self.Age = Age



object = Personal_Information("Junior", 20)
print(object.age)