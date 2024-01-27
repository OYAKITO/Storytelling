"""
CALCULATOR PROGRAM

this Python program simulates a calculator application that will take in any two numbers, and a basic mathematical operation (addition, subtraction, multiplication, division, or exponentiation), perform that operation, print a lexical statement of the operation, and return a mathematical statement that describes the mathematical results. Upon completion, your program will print out a history of all calculations performed including any error messages that may have occurred such as division by zero.
"""

def perform_operation(a, b, operation, operation_symbol):
    """Perform the specified operation and return the result."""
    result = round(operation(a, b), 4)
    print(f"The {operation_symbol} of {a} and {b} is {result}.")
    return f"{a} {operation_symbol} {b} = {result}"

def add(a, b):
    """Add two numbers and return the sum."""
    return a + b

def subtract(a, b):
    """Subtract two numbers and return the difference."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the product."""
    return a * b

def divide(a, b):
    """Divide two numbers and return the quotient."""
    if b != 0:
        return a / b
    else:
        print("You cannot divide by zero.")
        return "DIV ERROR"

def exponent(a, b):
    """Take a number to a power and return the result."""
    return a ** b

# The main code
print("CALCULATOR")
print("Enter two numbers and the desired operation will be performed.")

history = []
running = True

while running:
    # Get user input
    num1 = float(input("\nEnter a number: "))
    num2 = float(input("Enter a number: "))
    operator = input("Enter an operation (addition, subtraction, multiplication, division, or exponentiation): ").lower()

    # Call the appropriate function based on the value of operator
    if operator in {'addition', 'a'}:
        result = perform_operation(num1, num2, add, 'sum')
    elif operator in {'subtraction', 's'}:
        result = perform_operation(num1, num2, subtract, 'difference')
    elif operator in {'multiplication', 'm'}:
        result = perform_operation(num1, num2, multiply, 'product')
    elif operator in {'division', 'd'}:
        result = perform_operation(num1, num2, divide, 'quotient')
    elif operator in {'exponentiation', 'e'}:
        result = perform_operation(num1, num2, exponent, 'answer')
    else:
        print("That is not a valid operation. Try again.")
        result = "OPP ERROR"

    # Append the mathematical result to the history
    history.append(result)

    # Allow user to quit
    choice = input("Would you like to run the program again (y/n): ").lower()
    if choice != 'y':
        print("\nCalculation Summary:")
        for calc in history:
            print(calc)
        print("\nThank you for using the Calculator. Goodbye!")
        running = False
