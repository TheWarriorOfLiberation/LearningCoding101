# A very simple python calculator
print("Welcome to Daniel's calculator! \n'It can add, subtract, multiply and divide any number!")
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter a operator, the options are +,-,*,/,%,**: ")
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "%":
        print(num1 % num2)
    elif operator == "**":
        print(num1 ** num2)
    else:
        print("Invalid operator")



calculator()
# Version 1.0 for the calculator
