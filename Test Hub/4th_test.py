class Voters:

    def individual(self, age):
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")


object = Voters()
print(object.individual(19))


class Test:

    def Triangle(self, base, height):
        print(1 / 2 * base * height)

    def Square(self, length):
        print(2 * length)

    def Rectangle(self, length, height):
        print(length * height)

    def Cube(self, length):
        print(3 * length)

object = Test()
print(object.Triangle(10, 13))
print(object.Square(14))
print(object.Rectangle(14, 23))
print(object.Cube(31))



