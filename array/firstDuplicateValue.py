# -*- coding: utf-8 -*-
"""
from Algoexpert
"""

"""

Given an array of integers between 1 and n, inclusive, where n is the length of the array, write a function 
that returns the first integer that appears more than once (when the array is read from left to right)

Example 
array=[2,1,5,3,3,4,2] returns 3, not 2, because the second 3 appears before the second 2
"""

def firstDuplicateValueFirstSol(array):
    ''' 
    this is the first solution, with O(n) time complexity and 
    O(n) space complexity
    '''
    
    #creation of a set to store the value of the array as keys
    set_val=set()
    
    for num in array:
        
        if num in set_val: # this operation is O(1) complexitiy
            return num
        set_val.add(num)

    return -1


def firstDuplicateValueSecondSol(array):
    ''' 
    this is the second solution, with O(n) time complexity and 
    O(1) space complexity.
    This solution under the clause that all the values are between 1 and n
    '''    
    for num in array:
        
        absNum=abs(num)
        
        if array[absNum-1]<0:
            return absNum
        else:
            array[absNum-1]*=-1
    
    return -1
