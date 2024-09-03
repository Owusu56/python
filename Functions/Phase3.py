
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

Student_name = input("Input your name")


def Search(kay):
    for data in Database:
        if kay == data.__getitem__('name'):
            print("id ", data.__getitem__('id'))
            print("name ", data.__getitem__('name'))
            print("course ", data.__getitem__('course'))
            print("level ", data.__getitem__('level'))
            print("password ", data.__getitem__('password'))
            print("email ", data.__getitem__('email'))
            return True
            break


if Search(Student_name):
    print("Record Found")
else:
    print("Get the fuck out of here")
