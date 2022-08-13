#Take union of two arrays and show only unique values, return the length of array
class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        s=set()
        for i in range(len(a)):
            s.add(a[i])
        for i in range(len(b)):
            s.add(b[i])
        return len(s)
        
n=int(input())
m=int(input())
a=[1,2,4,3,5,7]
b=[1,2,8,9,7]
ob=Solution()
print(ob.doUnion(a,n,b,m))

#TS: O(2n)
#SC:O(1)
