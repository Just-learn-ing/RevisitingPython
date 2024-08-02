'''Set is one of four builtin data types in python and is used to store collection of data
A set is unordered, unchangeable and unindexable
You can not predict in which order the elements of set will print
False and 0, True and 1 are considered same element in set and are treated as duplicates
A set item can be of any data types
you cannot change item of a set but you can add items of the set

'''
List = ["list","banana"]
myset = {3, 2, 3 ,2, 1 ,343.0 , False}   #a set can only contain a particular element single time 
print(myset)                    #duplicates are not allowed, if you did so, they will submerge into one.
print(mysett:=set((8, 3, 23 , False)))   #printing a set using its constructor #when using constructor, aware of double brackets
'''For x in myset:
    print(myset)
      '''
print(89 not in myset)

#add element using update method
myset.update(2333)
myset.update(List)                     #u can use any iterable using this method

#remove items using remove method
myset.remove("list")      #if the item is not present remove method will raise an error
myset.discard("list")        #if the item is not present discard method will not generate and error
myset.pop()                 #deletes a random item from the set 
del(mysett)                 #deletes the whole set 
#methods
'''
clear()  --> clears the set totally 
'''



"JOINING SETS"#METHODS
'''There are several methods to join sets in python:
update()  --> update with any iterable dadta type, exclude duplicate items.
union()   --> we can use operator | instead of union, u can join multiple sets       set1.union(set2, set3, set4)
              Also union method allows to join sets, with list, tuples, etc.
intersection()--> we can use & operator instead of union 
difference()
symmetric_difference() --> this set contains all the elements except duplicates. U can use ^ operator also. 
intersection_update() --> keeps only duplicates but it will change original one instead of returning a new set.
difference_update()
symmetric_difference_update()
'''
#METHODS ON SET:
'''
method                          shortcut            
copy()                                               returns a copy of set
difference()                       -                        
difference_update()               -=
intersection_update()             &=
issubset()                        <=                
                                  <                  returns whether all items are present in specified set or not
issuperset()                      >=
                                  >
symmetric_difference_update()     ^=
union_update()                    |=
'''



