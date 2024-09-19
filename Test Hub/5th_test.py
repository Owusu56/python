# Write a library code for junior engineers to use to,
# 1.Create a class student
# 2.Private property to take information
# 3.Create a database with list and dictionary using student information
# 4.Populate database with data
# 5.Loop all data out using for loop and Init method.

Database = [
    {
        "id": "UPI00000001",
        "code": "2015",
        "name": "Pauson",
        "course": "Software Engineering",
        "password": "123456789",
        "performance": "Good"
    },
    {
        "id": "UPI00000002",
        "code": "2016",
        "name": "Giscard",
        "course": "Networking and Cybersecurity",
        "password": "12345678",
        "performance": "Good"
    },
    {
        "id": "UPI00000003",
        "code": "2017",
        "name": "Classical Jones",
        "course": "Office Administration",
        "password": "1234567",
        "performance": "Good"
    },
    {
        "id": "UPI00000004",
        "code": "2018",
        "name": "Boakye",
        "course": "Design Technology",
        "password": "123456",
        "performance": "Good"
    }, ]


class Student:
    __id = None
    __code = None
    __name = None
    __course = None
    __password = None
    __performance = None

    def __init__(self, Id, Code, Name, Course, Password, Performance):
        self.__id = Id
        self.__code = Code
        self.__name = Name
        self.__course = Course
        self.__password = Password
        self.__performance = Performance

    def setId(self, Id):
        self.__id = Id

    def getId(self):
        return self.__id

    def setCode(self, Code):
        self.__code = Code

    def getCode(self):
        return self.__code

    def setName(self, Name):
        self.__name = Name

    def getName(self):
        return self.__name

    def setCourse(self, Course):
        self.__course = Course

    def getCourse(self):
        return self.__course

    def setPassword(self, Password):
        self.__password = Password

    def getPassword(self):
        return self.__password

    def setPerformance(self, Performance):
        self.__performance = Performance

    def getPerformance(self):
        return self.__performance


# userinput = input("User Code:")
for data in Database:

    # if data.__getitem__("code") == userinput:
        focus = Student(data.__getitem__('id'), data.__getitem__('code'), data.__getitem__('name'),
                        data.__getitem__('course'), data.__getitem__('password'), data.__getitem__('performance'))
        print(focus.getId())
        print(focus.getCode())
        print(focus.getName())
        print(focus.getCourse())
        print(focus.getPassword())
        print(focus.getPerformance())
