'''Strings are iterable. 
Strings are arrays like any other programming language, there are array of unicode characters.
Means, We can access characters of string something like this'''

def String_are_arrays():
    str = "Hello World"
    print(str[0])
    print(str[1])
    print(str[3])
# String_are_arrays()

def Iterating_through_a_string():
    for i in "Iterating_through_a_string":
        print(i)
# Iterating_through_a_string()

def Getting_a_string_length():
    str = "This is a string of length"
    print(len(str))
# Getting_a_string_length()

def Find_something_in_string():
    a = '''If a certain phrase or character is present in string we can use in keyword'''
    print("If" in a)
    print("Null"in a)
    print("Null" not in a) #we can also use it with if or else 
# Find_something_in_string()

# def Slicing_of_a_string
    

