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

def Getting_a_string_length(): #len(str)
    str = "This is a string of length"
    print(len(str))
# Getting_a_string_length()

def Find_something_in_string():
    a = '''If a certain phrase or character is present in string we can use in keyword'''
    print("If" in a)
    print("Null"in a)
    print("Null" not in a) #we can also use it with if or else 
# Find_something_in_string()

def Slicing_of_a_string():
    b = "Hello, World!" 
    print(b[2:5])   #slices from 2 to 5(5th not included, indexing starts from 0)
    print[:4]       #slice from the start
    print[4:]       #slice to the end
    print(b[-5:-2]) #negative slicing   
# Slicing_of_a_string()

'''Modifying strings'''
#sare methods ke sath paranthesis zarur rahega

def Upper_case_strings():
    a = "hello world"
    print(a.upper())
# Upper_case_strings()

def Lower_case_strings():
    a = "HeLLo World"
    print(a.lower())
# Lower_case_strings()

def Removing_white_spaces_from_strings():# a.strip()   Removes white spaces from only beginning or end not from middle
    a = "     Removes white spaces from only beginning or end not from middle      "
    print(a.strip())
# Removing_white_spaces_from_strings()

def Replacing_a_string():   #a.replace("hi", "bi")
    a = "Hello world"
    print(a.replace("Hel", "Sol")) #it takes two arguments it finds first one in strings and if it is there is the string then it replaces from the string 
    print(a.replace("hd", "had")) #returns old string if it does not finds the first one
# Replacing_a_string()
    
def Spliting_a_string(): #a.split("on which character do you want to split") and returns a LIST
    a = "solo polo rolo joro"
    print(a.split("o"))
# Spliting_a_string()

#concatenation of a string

def f_string():#fstring was introduced in python 3.6 Format string
    '''To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.'''
    var = 899
    print(f"the value of var is {var}")
    #displaying with 2 decimal places
    print(f"value of var to two decimal places is {var:.2f}")
    print(f"you can also solve an mathematical equation {34+23222} in middle of string using an f string")
# f_string()

# def Escape_characters():



#String Methods usage = a.capitalize()
'''
captilize():    converts first character to uppercase
casefold() :    converts string into lowercase 
center()   :    returns a centered string takes agrument a integer and gives makes you text center having string length that integer
count()    :    count number of times a specific value occurs in a string
encode()   :    returns a encoded version of string
endwith()  :    returns true if string endswith 
expandtabs():   
find()     :    search the string of specified value and returns the position where it is found
format()   
format_map():   
index()    :    search the string for a specified value and returns the position where is was found
isalnum()  :    returns true if string is alphanumeric
isalpha()  :    returns true if all characters in the string is alphabet
isascii()    : returns true if all characters in the string are ascii characters
isdecimal() :   returns true if all characters in the string is decimal 
islower()  :    retuns true if all character in the string are in lowercase
isnumeric():    returns true if all the character in the string are numeric
isprintable():  returns true if all the characters in the string is printable
isspace()  :    returns true if all the character in the string are whitespaces
istitle()  :    returns true if the string follows the rule of title
isupper()  :    returns true if the all the characters of the string is in uppercase
join()     :    join elements of a iterable to the end of the string
ljust()    :    returns ljustified version of the string
lower()    :    converts the string into lowercase
lstrip()   :    returns left trim version of a string
maketrans():    return a translation table to be used in translations
partition():    returns a tuple where string is parted into three parts
replace()  :    retuns a string where specified value is replaced with the specified value
rfind()    :    Searches the string for a specified value and returns the last position of where it was found
rindex()   :    Searches the string for a specified value and returns the last postion oof where is was found
rjust()    :    returns a right justified value of a string
rpartition():   retuns a tuple with three parts of the string
rsplit()   :    splits a string of speified origin and returns a list
splitlines():   splits the string at linebreaks and returns a list
startswith():   returns True if the string startswith
strip()    :    returns a trimmed version of the string
swapcase() :    swaps cases
title()    :    convert the first character of every letter capitalize
translate():    returns a translated string
zfill()    :    fills the with a specified number of 0's at beginning



'''

def Center():
    a = "jai shree ram"
    print(a.center(90))
# Center()

def Encode():
    a = "jai shree ram "
    a.encode()
Encode()



#Booleans
'''
Boolean returns True or False based on the conditions, like:
print(10==9)          //returns false
print(10<9)           //returns False
print(9<10)           //returns True
print(bool("abc"))    //Any number in function bool always returns true except 0
print(bool(0))        //returns True


Some False values:
    --> bool(())
    --> bool([])
    --> bool("")
    --> bool(None)
    --> bool(False)
    --> bool({})
    --> bool([])
    --> class myclass():
            def __len__(self):
             return 0

        myobj = myclass()
        print(bool(myobj))

    '''

def myFunction() :
  return True
# if myFunction():
#   print("YES!")
# else:
#   print("NO!")

def Check_data_type(): #check whether a particular thing is of same data type or not
    x = 9
    y = "string"
    print(isinstance(y, str))
    print(isinstance(x, int))
    print(isinstance(x, str))
# Check_data_type() #Checkinstance


