# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 22:30:32 2018

@author: katsuhisa
"""

# essential algorithm questions  (https://www.toptal.com/algorithms/interview-questions)
'''How would you optimally calculate p^k, where k is non-negative integer? 
What is the complexity of the solution?'''
def pow(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        return pow(base**2, exponent/2)
    elif exponent % 2 == 1:
        return pow(base**2, (exponent - 1)/2)
# This solution results in a complexity of O(log(k))

'''Sorting algorithms?'''
# (http://python3.codes/popular-sorting-algorithms/)
# bubble sort (O(n^2))
def bubble_sort(seq):
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
    return seq
