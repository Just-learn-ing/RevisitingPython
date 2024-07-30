'''Now we are going to Study about list now:
List is a collection data type
    There are four collection data types in python
        List 
        Tuple
        Set 
        Dictionary 


List is changeable 
List allows duplication of elements
list items can be of any data types



Accessing list items:
    ♥ using indexing  -->  list[9]              //print 10th element of the list
    ♥ supports slicing
    ♥ supports negative indexing and slicing
    ♥
We can also use list constructor to construct a list:
list(("apple", "banana", "mango"))

len(list) --> returns the length of the list 
'''

list = ["apple", "banana", "Papaya", "water melon", "Papaya"]

def check_items_in_list():#checking if required item exist in the list
    print("Papaya" in list)
# check_items_in_list()

def using_insert_method():#list.insert(index, value)
    list.insert(1, "jai shree ram")
    print(list[1])
# using_insert_method()





#change item value: list[2] = "apricot"
#change range of items: list[1:3] = ["apricot", "mango"]
#change 2nd value by replacing n values = list[1:2] = ["ep","hp", ...n values]
#change 2nd and 3rd value by replacing 1 value= list[1:3] = "tum tak tum tak arzi meri"

#adding items to list
def Append_list(): #append an item to list 
    list.append("Tum hi ho")
    print(list[4])
# Append_list()

def extend_list(): #extend another list to list
    list2=["aaloo","baigan","gobhi"]
    list.extend(list2)
    print(list)
# extend_list()    #list.extend(anyiterable)

def extend_any_iterable_to_list(): #using extend(iterable) method 
    tuple = (8,9, 20)
    str = "string"
    dictionary = {1:20, 2:23}
    list.extend(tuple)
    list.extend(str)
    list.extend(dictionary)
    print(list)
# extend_any_iterable_to_list()  #if extending dictionary it will only extend keys of dictionary to the list 

"Remove list items"

def List_remove():#using remove method u can remove any specified value in the list 
    list.remove("Papaya")
    print(list)
# List_remove() #if there are more than 1 occurence of any item then it will remove only first occurence.

def List_pop(): #pop method removes from specified index --> list.pop(0)
    list.pop(0)
    print(list)
# List_pop()  

def Del_keyword(): #Del_keyword is also used to delete specified index even it can delete whole list
    del list[2]
    print(list)
# Del_keyword()
# del list
# print(list)

def List_clear(): #clear all the list contents
    list.clear()
    print(list)
# List_clear()



"Looping through a list"

def looping_through_list():
    for x in list:
        print(x)
# looping_using_in_list()

def looping_using_len_and_range():
    for i in range(len(list)):
        print(list[i])
# looping_using_len_and_range()

def looping_using_while_loop():
    i = 0
    while i < len(list):
        print(list[i])
        i+=1
# looping_using_while_loop()

def looping_through_list_comprehension():
    [print(x) for x in list]
# looping_through_list_comprehension()










"List comprehension"
'''List comprehension can be useful if you want to make a new list based on the old list it can provide you shorter syntax'''

'''list2=[]
for x in list:
    if "a" in x:
        list2.append(x)
print(list2)'''

#using list comprehension
list2 = [x for x in list if "a" in x]
# print(list2)

list3 = [x for x in list2]
# print(list3)

list4 = [x for x in range(20)]
# print(list4)

list5 =[x for x in range(10) if x > 5]
# print(list5)

list6 = [x.upper() for x in list]
# print(list6)

list7 = ["lol" for x in list]
# print(list7)

list8 = [x if x == "banana" else "orange" for x in list]
# print(list8)











"Sorting of a list"
def Sorting_alphabetically(): #sorts based on ascii value means capital letter will come first and smaller second
    list.sort()
    print(list)
# Sorting_alphabetically()

numericlist= [332,234,123,11,24,124]
def Sorting_numerically():
    numericlist.sort()
    print(numericlist)
# Sorting_numerically()

AlphanumericList = [2,34,2343,3,234,23, "apple", "Apple", 65, 66 ,63]
def sorting_alphanumerically():                                      #generates error alphanumeric sorting is not possible
    AlphanumericList.sort()
# sorting_alphanumerically()

def Sort_descending_alphabet(): #list.sort(reverse = True)
    list.sort(reverse= True)
    print(list)
# Sort_descending_alphabet()


def Sort_descending_number():
    numericlist.sort(reverse=True)
    print(numericlist)
# Sort_descending_number()

"Copying list"
mylist = list.copy()
# print(mylist)

'''Joining two list, This can be acheived by 
1. using + operator between two list
2. using append method
3. using extend method'''








