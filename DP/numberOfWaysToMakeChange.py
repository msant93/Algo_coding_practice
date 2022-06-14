# -*- coding: utf-8 -*-
"""
from Algoexpert
"""
"""

 Given an array of distinct positive integer representing coind denominations and a 
 single non-negative integer n representing a target amount of money, write a function 
 that returns the number of ways to make change for tha target amount using the given coin denominations.
 Note that an unlimited amount of coins is at your disposal
 
 Example: n=6
     denoms=[1,5]
     returns 2 (1x1 + 1x5 and 6x1)
"""
"""
Complexitiy O(nd) time and O(n) space, where n is the target amount and 
d is the number of coins denominations
"""

def numberOfWaysToMakeChange(n, denoms):
        
#array of n+1 elements to find the number of ways to make changes for all amounts between 0 and n inclusive.
#Only one way to make changes for 0:  to not use any coins.
      
	ways=[0 for i in range(n+1)]

	ways[0]=1

	for denom in denoms:
		for amount in range (1,n+1):
			if denom <= amount:
				ways[amount]+=ways[amount - denom]

	return ways[n]   