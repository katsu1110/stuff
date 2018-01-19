# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 22:30:32 2018

@author: katsuhisa
"""

#%%
# FizzBuzz
def fizzbuzz():
    for i in range(1,101,1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

#%%
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

# insertion sort (O(n^2))
def insertion_sort(seq):
    for i in range(1,len(seq)):
        j = i - 1
        key = seq[i]
        while (seq[j] > key) and (j >= 0):
            seq[j+1] = seq[j]
            j -= 1
        seq[j+1] = key
    return seq