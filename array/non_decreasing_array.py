# -*- coding: utf-8 -*-
"""
leetcode 665
"""
"""
given an array nums with n integers, your task is to check if it could become 
non-decreasing by modifying at most one element.
We define an array is non-decreasing if num[i]<=nums[i+1] holds for every i
suche that (0<= i <=n-2)
"""
"""
Example1: 
    input: nums =[4,2,3]
    Output: true
        
    explanation: you can modify the first 4 to 1 to get a non-decreasing array
    
    input: nums =[4,2,1]
    output: false
    Explanation: you can't get  a non-decreasing array by modifying at most one element
    
    
"""

def checkPossibility(nums):
    
    changed=False
    
    for i in range(len(nums)-1):
        
        if nums[i] <= nums[i + 1]:
            continue
        
        # it means this is not the first change
        if changed: 
            return False
        
        if i==0 or nums[i+1]>= nums[i-1]:
            nums[i]=nums[i+1]
        else:
            nums[i+1]=nums[i]

    return True