#Segreegate the negetaive and positive elements of the array and then put negatives at end of positives.
class Solution:
    def segregateElements(self, arr, n):
        a=[]
        b=[]
        for i in range(len(arr)):
            if arr[i]<0:
                a.append(arr[i])
            else:
                b.append(arr[i])
        b.extend(a)
        return b
        
n=int(input())
arr=[1,2,4,3,-5,-4,7,9,-3]
ob=Solution()
print(ob.segregateElements(arr,n))

#TC:O(n)
#SC:O(1)
