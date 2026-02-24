#program to find odd even

def odd_even_finder(number):
    if (number%2)==0:
        return "Number is even"
    else:
        return "Number is odd"
    
number=input("Enter the number you wish to check:")
odd_even_finder(number)