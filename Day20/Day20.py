#!/bin/python3

import math
import os
import random
import re
import sys

def bubbleSort(n, a):
    swaps = 0
    
    for j in range(n-1):
        for i in range(n-1):
            if a[i] > a[i + 1]:
                a[i], a[i+1] = a[i+1], a[i]
                swaps += 1
        
        if swaps == 0:
            break
    return(swaps, a[0], a[n-1])


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    swaps, firstElement, lastElement = bubbleSort(n,a)
    print("Array is sorted in %d swaps." % swaps)
    print("First Element: %d" % firstElement)
    print("Last Element: %d" % lastElement)