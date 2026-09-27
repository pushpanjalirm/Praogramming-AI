"""1 Operators in Python
1.1 Arithmetic, Comparison, and Logical Operators
Example:
# Arithmetic Operators
a = 10
b = 5
add = a + b # Addition
sub = a - b # Subtraction
mul = a * b # Multiplication
div = a / b # Division
mod = a % b # Modulus
exp = a ** b # Exponentiation
# Comparison Operators
greater = a > b # True
equal = a == b # False
not_equal = a != b # True
# Logical Operators
and_op = (a > 5) and ( b < 10) # True
or_op = (a < 5) or ( b > 2) # True
not_op = not (a < 5) # True"""

# Program: perform arithmetic operations on two input numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number:"))

addition = num1 + num2 + num3
subtraction = num1 - num2
multiplication = num1 * num2 * num3
modulus = num1 % num2

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Modulus: {modulus}")
