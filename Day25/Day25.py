# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

T = int(input())
numbersArray = []
for i in range(T):
    numbersArray.append(input())

for ele in numbersArray:
    number = int(ele)
    
    if number == 1:
        print("Not prime")
    else:   
        flag = False
        for b in range(2,int(sqrt(number)+1)):
            if number % b == 0:
                flag = True
        
        if flag == True:
            print("Not prime")
        else:
            print("Prime")
