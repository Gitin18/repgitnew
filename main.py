import math

def gcd_three_numbers(a, b, c):
    return math.gcd(math.gcd(a, b),c)

    # Calculate the GCD of the first two numbers, then calculate the GCD of that result with the third number
    return math.gcd(math.gcd(a, b), c)

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Check if the three numbers are coprime
gcd_value = gcd_three_numbers(num1, num2, num3)
if gcd_value == 1:
    print(f"{num1}, {num2}, and {num3} are coprime.")
else:
    print(f"{num1}, {num2}, and {num3} are not coprime. Their greatest common divisor is {gcd_value}.")




