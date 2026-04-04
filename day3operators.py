#arithmetic operators
#comparison operator

#In addition to the above comparison operator Python uses:
# is: Returns true if both variables are the same object(x is y)
# is not: Returns true if both variables are not the same object(x is not y)
# in: Returns True if the queried list contains a certain item(x in y)
# not in: Returns True if the queried list doesn't have a certain item(x not in y)

#logical operators
#and: Returns True if both statements are true(x and y)
#or: Returns True if one of the statements is true(x or y)
#not: Reverse the result, returns False if the result is true(not x)


#exercise

age=26
height=5.10
com=5+4j
#1
base=int(input("Enter the base of the triangle:"))
height=int(input("Enter the height of the triangle:"))
area=0.5*base*height 
print(f"The area of the triangle is {area}")   
#2
sidea=int(input("Enter the length of side a:"))
sideb=int(input("Enter the length of side b:"))
sidec=int(input("Enter the length of side c:"))
perimeter=sidea+sideb+sidec
print(f"The perimeter of the triangle is {perimeter}")

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for i in range(1,6):
    print(f"{i} {1} {i} {i**2} {i**3}")
