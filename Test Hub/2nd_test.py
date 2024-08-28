# Write a program to check if the last digit of a number is divisible by 23
# (any number %10 return last digit)

#
num = int(input("Input Your Number"))
if num % 23 == 0:
    print("Divisible by 23")
else:
    print(" Not divisible by 23")

    # ALTERNATIVE
number = float(input("Input Your Number"))

Divisible = (number % 23 == 0)
print(Divisible)
if Divisible:
    print("Divisible by 23")
else:
    print(" Not divisible by 23")

    # ALTERNATIVE
number = float(input("Input Your Number"))

Divisible = (number % 23)
print(Divisible)
if Divisible:
    print("Divisible by 23")
else:
    print(" Not divisible by 23")

print(4670 % 10)

# Write a program to check if a number is a multiple of 50


# Write a program to open a safe
# Before opening the safe require three or two personel to open. The President, Vice President ane the Speaker
# The president and any other can open the safe. The other two personel can also open the safe.


First_Personnel = str(input("President's Password"))
Second_Personnel = str(input("Vice President's Password"))
Third_Personnel = str(input("Mr Speaker's Password"))

President = '001'
Vice_President = '002'
Mr_Speaker = '003'

if First_Personnel == President and Second_Personnel == Vice_President:
    print("Safe Opened")
elif First_Personnel == President and Third_Personnel == Mr_Speaker:
    print("Safe Opened")
elif Second_Personnel == Vice_President and Third_Personnel == Mr_Speaker:
    print("Safe Opened")
else:
    print("Safe Can't Open")
