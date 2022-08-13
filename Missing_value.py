#An array of zize 1 to element N is given, like 1,2,3,4 till 10
#we need to find the missing value in the array 
class Solution:
    def MissingNumber(self,array,n):
        a=[]
        b=[]
        for i in range(1,n+1):
            a.append(i)
        for i in range(len(a)):
            if a[i] not in array:
                b.append(a[i])
        return b
                
        
n=int(input())
array=[1,2,4,3,5,7,8,9,10]
ob=Solution()

print(ob.MissingNumber(array,n))

#Missing value is = 4
#TC:O(2n) - Lets try for O(n)
#SC:O(1)

#Solution 2 - O(n)

class Solution:
    def MissingNumber(self,array,n):
        
        for i in range(1,n+1):
            if i not in array:
                b=i
        return b
                
        
n=int(input())
array=[1,2,4,3,5,7,8,9,10]
ob=Solution()

print(ob.MissingNumber(array,n))

#Solution 2 - FASTEST Solution, yayyy

class Solution:
   
    def MissingNumber(self,array,n):
        a=[]
        b=0
        for i in range(1,n+1):
            a.append(i)
        b=list(set(a)-set(array))
        
        return b[0]
# we can take difference of two sets 
