# Write a program to find a maximum of two numbers.

def maximum(num1, num2):
    if num1>num2:
        print(f"{num1} is maximum")
    elif num2>num1:
        print(f"{num2} is maximum")
    else:
        print("Both numbers are equal")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
maximum(num1, num2) 