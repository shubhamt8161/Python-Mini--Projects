num1 =float(input("Enter your first number:"))
num2 =float(input("Enter your second number:"))

operator = input("Enter operation (+, -, *, /): ")

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    print(num1 / num2)

else:
    print("Invalid operation")


