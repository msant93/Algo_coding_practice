# -*- coding: utf-8 -*-
"""
from Algoexpert
"""

"""

write a function that takes in an array of positive integers and returns 
the maximum sum of non - adjacent elements in the array.
If the input is empty, the function should return 0

example 
array = [75,105,120,75,90,135]
output = 330 = 75+120+135
"""

def maxSubsetSumNoAdjacent(array):
    '''
    O(n) time, O(1) space
    '''    
    # check if the list in input is empty
    if not array: 
        return 0
    
    
    if len(array)==1:
        return array[0]
    
    second =array[0]
    first=max(array[0],array[1])
    
    for i in range(2,len(array)):
 
        current=max(first,second + array[i])
        second=first
        first=current
        
    return current
