class Marker:
    __color = None
    __name = None
    __type = None
    __brand = None
    __price = None
    __image = None

    def __init__(self, Color, Name, Type, Brand, Price, Image):
        self.__color = Color
        self.__name = Name
        self.__type = Type
        self.__brand = Brand
        self.__price = Price
        self.__image = Image

    def getColor(self):
        return self.__color

    def setColor(self, Color):
        self.__color = Color


object = Marker('Black, Red, Blue', 'Monami', 'Permanent', 'Monami Co. ltd', '3', 'marker.jpg')
# object.setColor()
print(object.getColor())
