import numpy as np
print(np.__version__)
arr1 = np.array([1,2,3,4,5,"sd"])
print(arr1)


#dimension of arrays: nested arrays are dimensional array
#0-d array
arr0 = np.array(90)
#1-d array 
arr1 = np.array([1,22,3,4])
#2-d array
arr2 = np.array([[1,2,3],[2,3,4],[3,4,5]])
#3-d array
arr3 = np.array([[[1,2,3],[1,2,3]], [[2,3,4],[2,3,4]]])

#n-d array     you can have any number of dimensions in any array 
arrn = np.array([1,2,3,4],ndmin=45)

#checking number of dimensions
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arrn.ndim)
# print(arrn)
#array indexing is same as array indexing in c it's just that python supports negative indexing and c doesn't support negative indexing























'''Numpy:
    Numpy is a library built in c and python language. 
    Numpy is used for using arrays in python. 
    Numpy is 50x faster than lists in python.
    Numpy was created by travis oliphant in 2005.
    Array object in Numpy is called ndarray.
    Numpy arrays are located in one continuous location unlike list, So processes can access and manipulate them efficiently.
        This behaviour is called Locality of reference in computer science.
        This is the main reason behind being faster than list. Also, Numpy is optimized with latest cpu architechture.
        '''