# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

#import math
#import os
#import random
#import re
#import sys



if __name__ == '__main__':
    phonebook = {}
    n = int(input())
    
    for i in range(n):
        entry = str(input()).split(" ")
        
        phonebook.update({entry[0]: entry[1]})
    
    while True:
        try:
            lookup = str(input())
        
            if lookup in phonebook:
                phone = phonebook[lookup]
                print(lookup + "=" + str(phone))
            else:
                print("Not found")
        except EOFError:
            break