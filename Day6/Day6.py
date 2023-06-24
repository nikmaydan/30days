# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys

def listtostring(a):
    str1 = ""
    for ele in a:
        str1 += ele
        
    return str1

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        #print(S)
        odd = []
        even = []
        length = len(S)
        for i in range(length):
            if i % 2 == 0:
                even += S[i]
            else:
                odd += S[i]
        odd = listtostring(odd)
        even = listtostring(even)
        print(even, odd, sep=' ')