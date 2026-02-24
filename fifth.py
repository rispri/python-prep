#program to find odd even

def odd_even_finder(number):
    if (number%2)==0:
        print( "Number is even")
    else:
        print( "Number is Odd")
    
number=int(input("Enter the number you wish to check:"))
odd_even_finder(number)