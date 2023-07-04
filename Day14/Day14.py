class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        minValue = 100
        maxValue = 0
        
        for ele in self.__elements:
            
            if minValue > ele:
                minValue = ele
                
            if maxValue < ele:
                maxValue = ele
            
        self.maximumDifference = maxValue - minValue
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)