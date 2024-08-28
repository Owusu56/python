
# (+, -, *, /, %, **)

# A program that add, subtract, divide and multiply

First_Number = float(input("Input First Number"))
op = input("Input Operator + - * /")
Second_Number = float(input("Input Second Number"))

if op == '+':
    print("The Sum Of ", First_Number, "+", Second_Number, "==", First_Number + Second_Number)
elif op == '-':
    print("The Subtraction Of ", First_Number, "-", Second_Number, "==", First_Number + Second_Number)
elif op == '*':
    print("The Product Of ", First_Number, "*", Second_Number, "==", First_Number + Second_Number)
elif op == '/':
    print("The Division Of ", First_Number, "/", Second_Number, "==", First_Number + Second_Number)


print(First_Number + Second_Number)
print(First_Number - Second_Number)
print(First_Number * Second_Number)
print(First_Number / Second_Number)

# A program to check if a number if Even or Odd Number

user = float(input("Enter a number"))
even = user % 2

print(even)
