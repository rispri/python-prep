# Write a program to find if the given number is prime or not.
#number which can be divided by 1 and itself are prime.

def prime_number(number):
    if number>=1:
        for i in range(2,number):
            if (number%i)==0:
                print(f"The given {number} is not a prime number")
                break
        else:
            print(f"The given {number} is a prime number")
number=int(input("Kindly input your number you wish to check:"))
prime_number(number)