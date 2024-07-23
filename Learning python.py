#revision is neccesary

# print("how are you",9,0,sep='')  #this is print statement for python no need to add semicolon in the last line it self is it python is interpreted language
#sep is used at the last;



#data types
'''There are too 6 data types in python:
Sno.        Datatype        literal         initial value
1.          Integer         int()                 0                 IMMUTABLE
2.          Float           float()              0.0                IMMUTABLE
3.          Complex         complex()             0j'''             #IMMUTABLE
#Numeric data types

#sequential data  types
'''
4.          String          str()            ''(nothing)            Mutable
5.          List            list()               []                 Mutable
6.          Tuple           tuple()              ()                 Immutable'''
#MAPPING TYPE
'''
7.          Dictionary      dict()              {}empty dictionary  Mutable'''
#SET TYPE
'''
8.          Set             set()               () empty set        Mutable
9.          Frozenset       frozenset()          frozenset()        Immutable '''
#BOOLEAN TYPE
'''
10.         Bool            bool()              False               IMMUTABLE
'''
#BINARY TYPE
'''
Abhi tak padha nahi hai jab padhunga tab likhunga'''
#NONE TYPE:
'''
11.         NONE                                                     IMMUTABLE'''


#Day 1
'''topic 1:  Casting;   in python you can use casting with help of Function'''


a = str(3)
b = float(3)
c = str(3)
d = list([3])
e = (9,)#tuple([9])
f = set([3])
g = frozenset([3])
h = dict({3: ""})

print(a, type(a),"\n")
print(b, type(b),"\n")
print(c, type(c),"\n")
print(d, type(d),"\n")
print(e, type(e),"\n")
print(f, type(f),"\n")
print(g, type(g),"\n")
print(h, type(h),"\n")