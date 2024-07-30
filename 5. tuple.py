mytuple = ("apple", "mango","aam", "sep") #tuple contains a set of non changeable values
'''Properties of tuple:
Order collection
Unchangeable items
Allow duplicates

tuple items can be of any data type, a single tuple can contain a variety of data types



Functions:
len(tuple) is used to determine length of a tuple
'''

def difference_in_tuples(): #("aaple") is not a tuple but ("aaple",) is a tuple
    toople = ("aaple")
    toople1 = ("aaple",)
    print(f"{toople} is a {type(toople)}\n{toople1} is a {type(toople1)}")
# difference_in_tuples()

def using_tuple_constructor():
     toople = tuple(("aaple", "baanana", "maango"))

#set items are also unchangeable but u can remove or add items


#access tuple items
    #refering to the index like lists
    #negative indexing
    #range of indexes
    #slicing is supported

#update and remove items: basically tuples are unchangeable but we can change tuple into list, change the values, then again change the list into tuple
# we can append pop and every thing we want,  every methods of list and then change it back to tuple 
# we can use del keyword to delete the tuple 
def changing_2nd_element(): 
     y = list(mytuple)
     y[1] = "item change"
     y.append("Ram ram jai shree ram")
     y.pop(0)
     x = tuple(y)
     print(x)
changing_2nd_element()

def unpacking_a_tuple(): #using tuple to create mutliple variables assing to different value
     (green, yellow, red, karan) = mytuple
     print(green,yellow, red, karan )
# unpacking_a_tuple()

def using_asterisk(): #using asterisk before variable , u can assign rest of the values as a list to that variable even if u using in middle see the code below
     tuple = (9, 90, 290, 290 , 392 , 323, 2349 , 343 )
     (nine, ninety, two_ninety, *numeric_list, three_four_three) = tuple
     print(nine)
     print(ninety)
     print(two_ninety)
     print(numeric_list)
     print(three_four_three)
# using_asterisk()


#looping is same as list its just tuple doesn't use any direct comprehension

'''JOINING TUPLES
        Two tuples can be joined using + operator
        A single tuple can be multiplies using asterisk'''
tuple1=(1,2,3)
tuple2=(4,5,6)
tuple1 = tuple1 + tuple2
tuple2 = tuple2*3
# print(tuple1)


