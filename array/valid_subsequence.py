# -*- coding: utf-8 -*-
"""
from AlgoExpert
"""
"""
    Given two non-empty arrays of integers, wirte a function that determines whether the second 
    array is a subsequence of the first one.
    A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array bu that are in the same 
    order as they appear in the array. For instance, the numbers [1,3,4] form a subsequence of the array 
    [1,2,3,4], and so do the numbers [2,4]
"""

def isValidSubsequence(array, sequence):
    # Write your code here.
    len_arr1=len(array)
    len_arr2=len(sequence)
    
    # check if the second is longer than the first,if yes, 
    # it can't be a subsequence
    if len_arr2>len_arr1:
        return False
    
    # index for the second array
    j=0
    
    for i in range(len_arr1):
        
        if sequence[j]==array[i]:
            j+=1
            if j==len_arr2:
                return True
        
    return False
    
    
