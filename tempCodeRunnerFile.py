'''IN python or any programming language iterable data type is the one which we can iterate over or we can go throught each element one by one
Some think like in a string you can iterate over a string for example "Raman" --> you can iterate it like
r
a
m
a
n


There are 8 iterable data types in python:
1. String
2. List
3. Dictionary (iterates over keys)
4. Sets
5. Tuple
6. Files (iterates over line)
7. Generators 
8. Iterators'''


def iterators():  #About iterators

    '''Iterators:
    An iterator is an object that follows Iterator protocol which includes __iter__() and __next__() methods. __next__() method
    raises an StopIteration exception When there remains no value to interate over ocject. Sample example is written below'''
    my_list = [1,2,3,4]
    iterator = iter(my_list)     #making of an iterator form a iterable(string, tuple, set, etc.)

    # print(next(iterator)
    # print(next(iterator)) 
    for i in range(4):
        print(next(iterator))

def count_up_to(max): #About generators
    '''Generators are iterable that allow you to iterate over sequence but unlike list they do not store whole sequence when called using 
    yield statement which makes them memory efficient. Whenever yield statment is called the value is returned and the function status is saved.
    They generates value over fly one at a time.'''
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
print(type(counter))
for number in counter:
    print(number, type(number))

