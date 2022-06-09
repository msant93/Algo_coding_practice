# -*- coding: utf-8 -*-
"""
from Algoexpert
"""

""" 
    write a function that takes in a non-empty array of integers thar are sorted in ascending order
    and returns a new array of the same length with the squares of the original integers also sorted in 
    ascending order
    
    sample input = [-10,1,2,3,5]
    sample output = [1,4,9,25,100]
"""
"""
    Complexity O(n) time and O(n) Space where n is the length of the input array
"""

def sortedSquaredArray(array):
    
    #every value of the new array is set to -1 so
    # it cannot be confused with a squared value
    squaredArray=[-1 for _ in range(len(array))]
    
    #two pointers for the array, so I don't need
    # to sort the output array
    start=0
    end=len(array) -1
    index=len(squaredArray) - 1
    
    
    for i in range(len(squaredArray)): 
        
        if abs(array[start])>abs(array[end]):
            squaredArray[index]=pow(array[start],2)
            start+=1
        else:      
            squaredArray[index]=pow(array[end],2)
            end-=1
        
        index-=1
    return squaredArray            
    