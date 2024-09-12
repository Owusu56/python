#Write a program that turn off light when no one is present in a room using three people
#3 = Bright
#2 = Dim
#1 = Dimmer
#0 = Off

# Number = int(input("How many people detected?"))
#
# Three = 3
# Two = 2
# One = 1
# No_one = 0
#
# if Number == Three:
#     print("Bright light")
# elif Number == Two:
#     print("Dim light")
# elif Number == One:
#     print("Dimmer light")
# else:
#     print("Lights Off")


                           #ALTERNATIVE

while True:
    number = input("How many people detected?")
    if number == '3':
        print("Bright light")
    elif number == '2':
        print("Dim light.")
    elif number == '1':
        print("Dimmer light")
    elif number == '0':
        print("Lights Off")


