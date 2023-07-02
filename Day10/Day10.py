#!/bin/python3

import math
import os
import random
import re
import sys

def decToBin(n):
    binary = []
    while (n > 0):
        remainder = n % 2
        n = int(n / 2)
        binary.append(remainder)
            
    return(binary)

def onesCount(ele, counter, maxCount):
    if ele == 1:
        counter += 1
        if counter > maxCount:
            maxCount = counter
    else:
        counter = 0
    return counter, maxCount
    
def onesCountWrapper(binary):
    counter = 0
    maxCount = 0
    
    for ele in binary:
        counter, maxCount = onesCount(ele, counter, maxCount)
    
    return(maxCount)


if __name__ == '__main__':
    n = int(input().strip())
    binary = decToBin(n)
    
    print(onesCountWrapper(binary))
    