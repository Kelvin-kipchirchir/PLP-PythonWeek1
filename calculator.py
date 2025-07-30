# -----------simple Calculator Program--------------

# request user inputs
num1 = float(input("Enter the first number: "))
operator = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# doing the calculations
if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("cannot divide by zero")
else:
    print("Invalid operand only use +, -, *, or /")
