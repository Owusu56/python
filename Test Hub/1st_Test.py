# QUESTION: Create a program that takes four input checks which is the greatest value

Ant = int(input("Input Your First Value"))
Bat = int(input("Input Your Second Value"))
Cat = int(input("Input Your Third Value"))
Dog = int(input("Input Your Last Value"))

if Ant > Bat and Ant > Cat and Ant > Dog:
    print("1st has the greatest value")
elif Bat > Ant and Bat > Cat and Bat > Dog:
    print("2nd has the greatest value")
elif Cat > Ant and Cat > Bat and Cat > Dog:
    print("3rd has the greatest value")
elif Dog > Ant and Dog > Bat and Dog > Cat:
    print("4th has the greatest value")
else:
    print("Two or more animals can't have the same values")
