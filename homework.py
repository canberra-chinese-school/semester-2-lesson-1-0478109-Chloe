# Edit this file to make a calculator program that:
# asks the user for the first number
# then asks the user for an operation choice (plus, minus, multiply, or divide)
# asks the user for the second number
# calculates and prints the result


number1 = int(input("Enter number1: "))
operation_choice = input("Enter your choice of operation (plus, minus, multiply, divide):")
number2 = int(input("Enter number2: "))

def plus():
    result = number1 + number2
    return result

def minus():
    result = number1 - number2
    return result

def multiply():
    result = number1 * number2
    return result

def divide():
    result = number1 / number2
    return result


if operation_choice == "plus":
    print(plus())
elif operation_choice == "minus":
    print(minus())
elif operation_choice == "multiply":
    print(multiply())
elif operation_choice == "divide":
    print(divide())
else:
    print("Please enter a valid operation choice")



