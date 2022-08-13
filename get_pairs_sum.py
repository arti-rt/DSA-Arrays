#find total number of pairs in a array that sum up to value K

class Solution:
    def getPairsCount(self, arr, n, k):
        sum=0
        count=0
        for t in range(len(arr)):
            for j in range(t+1,len(arr)):
                sum=arr[t]+arr[j]
                if sum==k:
                    count+=1
        return count

#size of the array        
n=int(input())
#enter the sum you want to check
k=int(input())
#array defined
arr=[1,2,4,3,5,7,8,9,10]
ob=Solution()
print(ob.getPairsCount(arr,n,k))

#TC: O(n^2)  -- need to find O(n)
#SC:O(1)
