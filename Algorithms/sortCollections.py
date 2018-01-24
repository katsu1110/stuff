# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:40:09 2018

@author: katsuhisa
"""

# coding: utf-8
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# PURPOSE: pick up the fastest algorithm out of "bubble sort", "merge sort",
# "quick sort" based on the structure of the given list of integers and return
# the sorted list
# INPUT: list consisted of integers
# OUTPUT: sorted list

# HOW TO USE:
# 1) in the command line, go to the Python Shell
# 2) >>> import SortCollections
# 3) make instance ... >>> inst = sortCollections.SortCollections()
# 4) define a list of integers to sort >>> list = [2,5,3,8,1]
# 5) bubble sort ... >>> inst.bubbleSort(list)
#    merge sort ... >>> inst.mergeSort(list)
#    quick sort ... >>> inst.quickSort(list)
#    optimal (?) sort ... >>> inst.sort(list)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import math

class SortCollections:

    # initialization
    def __init__(self):
        pass

    # bubble sort
    @staticmethod
    def bubbleSort(intlist):
        # get the integer list
        print("Original: ", intlist)

        copylist = intlist

        for i in range(len(intlist)-1):
            k = 0
            print("step" + str(i) + ": ", intlist)

            while k + 1 < len(copylist):
                if intlist[k] > intlist[k+1]:
                    temporary = intlist[k+1]
                    intlist[k+1] = intlist[k]
                    intlist[k] = temporary

                k = k + 1

        new_list = intlist
        
        print("Sorted :")
        return(new_list)

    # merge sort
    @staticmethod
    def mergeSort(intlist):
        # get the integer list
        print("Original: ", intlist)

        if len(intlist) > 1:
            middle = len(intlist) // 2
            left = intlist[:middle]
            right = intlist[middle:]

            left = SortCollections.mergeSort(left)
            right = SortCollections.mergeSort(right)

            new_list = []
            lind = 0
            rind = 0

            while lind < len(left) and rind < len(right):
                if left[lind] <= right[rind]:
                    new_list.append(left[lind])
                    lind = lind + 1
                else:
                    new_list.append(right[rind])
                    rind = rind + 1

            if left:
                new_list.extend(left[lind:])
            if right:
                new_list.extend(right[rind:])
        else:
            new_list = intlist

        print("Sorted :")
        return(new_list)

    # quick sort
    @staticmethod
    def quickSort(intlist):
        print("Original: ", intlist)
        
        if len(intlist) > 1:
            pivot = intlist[0]
            # take 3 points and use
            left = []
            right = []
            middle = []
            for i in range(len(intlist)):
                if intlist[i] < pivot:
                    left.append(intlist[i])
                elif intlist[i] > pivot:
                    right.append(intlist[i])
                elif intlist[i] == pivot:
                    middle.append(intlist[i])

            left = SortCollections.quickSort(left)
            right = SortCollections.quickSort(right)

            new_list = left + middle + right
        else:
            new_list = intlist

        print("Sorted :")
        return(new_list)

    # insertion sort
    @staticmethod
    def insertion_sort(intlist):
        # get the integer list
        print("Original: ", intlist)

        for i in range(1,len(intlist)):
            j = i - 1
            key = intlist[i]
            while (intlist[j] > key) and (j >= 0):
                intlist[j+1] = intlist[j]
                j -= 1
            intlist[j+1] = key
        
        print("Sorted :")
        return(intlist)

    @staticmethod
    def sort(intlist):
        # unless intlist[0] is far away from a center of the list,
        # use quicksort
        minv = min(intlist)
        maxv = max(intlist)
        if math.pow(intlist[0]-minv,2) < math.pow(intlist[0]-(minv + maxv)/2,2) or math.pow(intlist[0]-maxv,2) < math.pow(intlist[0]-(minv + maxv)/2,2):
            new_list = SortCollections.mergeSort(intlist)
            print("Merge Sort")
        else:
            new_list = SortCollections.quickSort(intlist)
            print("Quick Sort")

        # elapsed time
        print(new_list)
