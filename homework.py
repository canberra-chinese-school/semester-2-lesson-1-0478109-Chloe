# In the exercise in class, we made a simple calculator program that can only do additions.
# In this homework, we'll work on a calculator that can plus, minus, multiply and divide 2 numbers.
# Edit this file to make a calculator program that:
# asks the user for the first number
# then asks the user for an operation choice (plus, minus, multiply, or divide)
# asks the user for the second number
# calculates and prints the result

# After writing the script, make sure you test it on "https://www.online-python.com/" or "https://www.onlinegdb.com/online_python_compiler"
# or Github codespaces, or your own python interpreter/IDE.

number1 = ... # TODO
operation_choice = input("Enter your choice of operation (plus, minus, multiply, divide):")
number2 = ... # TODO

def plus():
    result = ... # TODO
    return ... # TODO

def minus():
    result = ... # TODO
    return ... # TODO

def multiply():
    result = ... # TODO
    return ... # TODO

def divide():
    result = ... # TODO
    return ... # TODO


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



