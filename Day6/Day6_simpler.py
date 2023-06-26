# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        odd = ""
        even = ""
        length = len(S)
        for i in range(length):
            if i % 2 == 0:
                even += S[i]
            else:
                odd += S[i]
        print(even, odd, sep=' ')