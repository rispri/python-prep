# Write a program to find the given number is positive or negative.

def positve_negative_check(number):
    if number>=0:
        print(f"The given {number} is positive")
    else:
        print(f"The given {number} is negative")
number = int(input("Enter the number you wish to check:"))
positve_negative_check(number)