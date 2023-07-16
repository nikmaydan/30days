# Enter your code here. Read input from STDIN. Print output to STDOUT

dateReturned = input().split(" ")
dateDue = input().split(" ")

dayReturned = int(dateReturned[0])
monthReturned = int(dateReturned[1])
yearReturned = int(dateReturned[2])

dayDue = int(dateDue[0])
monthDue = int(dateDue[1])
yearDue = int(dateDue[2])

amountDue = 0

if yearReturned > yearDue:
    amountDue = 10000
elif yearReturned == yearDue:
    if monthReturned > monthDue:
        amountDue = 500 * (monthReturned - monthDue)
    elif dayReturned > dayDue:
        amountDue = 15 * (dayReturned - dayDue)
        
print(amountDue)