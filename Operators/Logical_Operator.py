# and or not


age = int(input("Input Your Age"))
can_vote = age >= 18
can_vote2 = age > 18 or age == 18

if can_vote:
    print("You can vote")
else:
    print("You cant vote")


# A program to check the largest number amongst three

A = int(input("Input Your Number"))
B = int(input("Input Your Second Number"))
C = int(input("Input Your Third Number"))

if A > B and A > C:
    print("A is the greatest")
elif B > A and B > C:
    print("B is the greatest")
elif C > A and C > B:
    print("C is the greatest")
else:
    print("Two numbers can't be equal")



