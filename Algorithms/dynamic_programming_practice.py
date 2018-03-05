# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 22:09:34 2018

@author: katsuhisa

just an exercise of a simple dynamic programming: compute a Fibonacci number
'https://www.youtube.com/watch?v=vYquumk4nWw' by 'CS Dojo'
"""

#%%
# Fibonacci number
def fib_recursion(n):
    """recursion: O(2^n)"""
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recursion(n-2) + fib_recursion(n-1)
        
def fib_memoization(n, memo):
    """memoization: O(n)"""
    if memo[n] != '':
        return memo[n]
    if n == 1 or n == 2:
        result =  1
    else:
        result = fib_memoization(n-2, memo) + fib_memoization(n-1, memo)
        memo[n] = result
    return result

def fib_bottomup(n):
    """bottom up: O(n)"""
    if n == 1 or n == 2:
        return 1
    bottom_up = [1]*(n+1)
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]