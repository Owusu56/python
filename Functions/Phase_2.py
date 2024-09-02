
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
        "id": "UPI00000001",
        "name": "Giscard",
        "course": "Software Engineering",
        "level": 2,
        "email": "gisard@gmail.com",
        "password": "12345678"
    },
    {
        "id": "UPI00000001",
        "name": "Jones",
        "course": "Software Engineering",
        "level": 2,
        "email": "classicaljones@gmail.com",
        "password": "1234567"
    },
    {
        "id": "UPI00000001",
        "name": "Boakye",
        "course": "Software Engineering",
        "level": 2,
        "email": "boakye@gmail.com",
        "password": "123456"
    }

]

username = input("Input your name")
password = input("Input your password")


def login(username, password):
    for data in Database:

        if username == data.__getitem__('name') and password == data.__getitem__('password'):
            return True
    else:
        return False


if login(username, password):
    print("Welcome ", username)
else:
    print("Failed to login")
