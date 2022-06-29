# -*- coding: utf-8 -*-
"""
767 leetcode
"""
"""
given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.

Example: 
Input : s="aab"
Output: "aba"

Input : s="aaab"
Output: ""
"""
import collections
import heapq

def reorganizeString(s:str) -> str:
    
    count=collections.Counter(s)  #Hashmap, count each char
    
    # I use - because python has only minheap
    maxHeap=[[-cnt,char]for char, cnt in count.items()] #list of lists of pair
    
    heapq.heapify(maxHeap) # O(n)
    
    prev=None
    res=""
    
    while maxHeap or prev:
        
        
        if prev and not maxHeap:
            return ""
        # most frequent, except prev
        cnt,char = heapq.heappop(maxHeap)
        res+=char
        cnt+=1  #because it is negative
        
        if prev:
            heapq.heappush(maxHeap, prev)
            prev=None
        
        if cnt < 0:
        
            prev=[cnt,char]
    
    
    return res