Database = [
    {
        "id": "UPI00000001",
        "name": "Pauson",
        "course": "Software Engineering",
        "level": 2,
        "email": "pausonchills@gmail.com",
        "password": "123456789"
    },
    {
        "id": "UPI00000002",
        "name": "Giscard",
        "course": "Software Engineering",
        "level": 2,
        "email": "gisard@gmail.com",
        "password": "12345678"
    },
    {
        "id": "UPI00000003",
        "name": "Jones",
        "course": "Software Engineering",
        "level": 2,
        "email": "classicaljones@gmail.com",
        "password": "1234567"
    },
    {
        "id": "UPI00000004",
        "name": "Boakye",
        "course": "Software Engineering",
        "level": 2,
        "email": "boakye@gmail.com",
        "password": "123456"
    }

]


class SoftwareEngineer:
    __id = None
    __name = None
    __course = None
    __level = None
    __email = None
    __password = None

    # CONSTRUCTOR or INITIALIZER
    def __init__(self, Id, Name, Course, Level, Email, Password):
        self.__id = Id
        self.__name = Name
        self.__course = Course
        self.__level = Level
        self.__email = Email
        self.__password = Password

    # SETTERS and GETTERS

    def setId(self, Id):
        self.__id = Id

    def getId(self):
        return self.__id

    def setName(self, Name):
        self.__name = Name

    def getName(self):
        return self.__name


userinput = input("User ID:")
for data in Database:
    if data.__getitem__("id") == userinput:
        object = SoftwareEngineer(data.__getitem__('id'), data.__getitem__('name'), data.__getitem__('course'),
                                  data.__getitem__('level'), data.__getitem__('email'), data.__getitem__('password'))
        print(object.getId())
        print(object.getName())
