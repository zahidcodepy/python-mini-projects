a = int(input(" Enter first number: "))   # input → string → converted to int
b = int(input(" Enter second number: "))

Operation = input("Enter the operation (+,-,*,/): ")  # operator as string

# if-elif-else → decision making (only one block runs)
if Operation == "+":
    print(a + b)   # expression → performs addition

elif Operation == "-":
    print(a - b)   # subtraction

elif Operation == "*":
    print(a * b)   # multiplication

else:
    print(a / b)   # division (assumes '/')
