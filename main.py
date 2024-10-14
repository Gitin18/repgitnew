import math

def are_coprime(a, b):
    return math.gcd(a, b) == 1

# Request two integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Check if the numbers are coprime56
gcd_value = math.gcd(num1, num2)
if are_coprime(num1, num2):
    print(f"{num1} and {num2} are coprime.")
else:
    print(f"{num1} and {num2} are not coprime. Their greatest common divisor is {gcd_value}.")


