class FlyingBird:
    left_wing = None
    right_wing = None
    left_foot = None
    right_foot = None

    def __init__(self, Pin1, Pin2, Pin3, Pin4):
        self.left_wing = Pin1
        self.right_wing = Pin2
        self.left_foot = Pin3
        self.right_foot = Pin4

    def setPin1(self, Pin1):
        self.left_wing = Pin1

    def getPin1(self):
        return self.left_wing

    def setPin2(self, Pin2):
        self.right_wing = Pin2

    def getPin2(self):
        return self.right_wing

    def setPin3(self, Pin3):
        self.left_foot = Pin3

    def getPin3(self):
        return self.left_foot

    def setPin4(self, Pin4):
        self.right_foot = Pin4

    def getPin4(self):
        return self.right_foot

    def Walk(self,Left_leg, Right_leg, High, Low, Delay):
        print()
        # print the way you want it to walk
    def Fly(self,Left_wing, Right_wing, High, Low, Delay):
        print(walk for 1000)
        # print the way you want it to fly







# object = FlyingBird("left wing up","right wing up","left foot forward","right foot back")
#
# print(object.getPin1())
# print(object.getPin2())
# print(object.getPin3())
# print(object.getPin4())