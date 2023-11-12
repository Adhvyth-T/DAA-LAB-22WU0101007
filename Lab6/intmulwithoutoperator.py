def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    elif a < 0 and b < 0:
        return multiply(-a, -b)
    elif a < 0:
        return -multiply(-a, b)
    elif b < 0:
        return -multiply(a, -b)
    elif a == 1:
        return b
    elif a > 0:
        return b + multiply(a - 1, b)

# Example usage:
num1 = 7
num2 = 8

result = multiply(num1, num2)
print(f"The product of {num1} and {num2} is:", result)
