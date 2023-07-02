#!/bin/python3

import math
import os
import random
import re
import sys

n = 6

def checkSum(summ, biggestSum):
    if summ > biggestSum:
        return summ
    else:
        return biggestSum

def hourglassSum(arr, i, j):
    hgSumm = 0

    for a in range(j, j + 3):
        hgSumm = hgSumm + arr[i][a] + arr[i+2][a]
    
    hgSumm += (arr[i + 1][j + 1])
    return hgSumm
        
    
def findBiggestSum(arr):
    biggestSum = -63
    i = 0
    j = 0
    
    for column in range(0, 4):
        for row in range(0, 4):
            summ = hourglassSum(arr, row, column)
            
            biggestSum = checkSum(summ, biggestSum)
    
    return biggestSum

if __name__ == '__main__':

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    print(findBiggestSum(arr))
    