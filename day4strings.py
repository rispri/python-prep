# # #Text is a string data type. Any data type written as text is a string. Any data under single, double or triple quote are strings. There are different string methods and built-in functions
# # #  to deal with string data types. To check the length of a string use the len() method.

# # # In Python and other programming languages \ followed by a character is an escape sequence. Let us see the most common escape characters:

# # # \n: new line
# # # \t: Tab means(8 spaces)
# # # \\: Back slash
# # # \': Single quote (')
# # # \": Double quote (")

# # #string formatting: Instead of concatenating strings and variables we can use string formatting to make it easier to read and write. There are different ways to format strings in Python, such as using f-strings, the format() method, or the % operator.''''

# # Accessing Characters in Strings by Index
# # In programming counting starts from zero. Therefore the first letter of a string is at zero index and the last letter of a string is the length of a string minus one.

# # l = 'Python'
# # t=l[:-1]
# # print(t)

# # Reversing a String
# # We can easily reverse strings in python.

# # greeting = 'Hello, World!'
# # print(1,greeting[::-1]) 

# company="Coding For All"
# # print(company)
# # print(company.capitalize())
# # print(company.title())
# # print(company.swapcase())
# # t=company[1:]
# # print(t)

# #Check if Coding For All string contains a word Coding using the method index, find or other methods.
# # t=company.find('All')
# # print(t)

# #Replace the word coding in the string 'Coding For All' to Python.

# # t=company.replace('Coding For All','Pyython for ALL') 
# # print(t)

# Split the string 'Coding For All' using space as the separator (split()) .
company="Coding For All"
# t=company.split()
# print(t)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# t="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(',')
# print(t)
# What is the character at index 0 in the string Coding For All.
# t=company[0]
# print(t)
# What is the last index of the string Coding For All.
# t=len(company)-1
# print(t)
# What character is at index 10 in "Coding For All" string.
# t=company[10]
# print(t)
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
# t="".join([word[0] for word in company.split()])
# print(t)
# Create an acronym or an abbreviation for the name 'Coding For All'.
# Use index to determine the position of the first occurrence of C in Coding For All.

# Use index to determine the position of the first occurrence of F in Coding For All.
# t=company.index('F')
# print(t)
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
# t=company.rfind('l')
# print(t)
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
f= 'You cannot end a sentence with because because because is a conjunction'
# t=f.find('because')
# print(t)
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# rindex=f.rindex('because')
# print(rindex)
# Slice out the phrase 'because because because' in the following sentence: 
l='You cannot end a sentence with because because because is a conjunction'
# t=l[31:54]
# print(t)  
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# al=l.find('because')
# print(al)
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# t=l[31:54]
# print(t)
# Does 'Coding For All' start with a substring Coding?
# t=company.startswith('Coding')
# print(t)
# Does 'Coding For All' end with a substring coding?
# t=company.endswith('coding')
# print(t)
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# t='   Coding For All      '.strip()
# Which one of the following variables return True when we use the method isidentifier():

# 30DaysOfPython
# thirty_days_of_python

print("30DaysOfPython".isidentifier())        # False
print("thirty_days_of_python".isidentifier())
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
t='# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'])
print(t)