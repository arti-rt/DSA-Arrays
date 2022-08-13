#Find all the duplicate element from the array
class Solution:
    def duplicates(self, arr, n): 
        a=[]
        s=[]
        
    	for i in range(len(arr)):
    	    for j in range(i+1,len(arr)):
        	    if arr[i]==arr[j]:
        	        a.append(arr[i])
        	        
        s=list(set(a))
        s.sort()	        
    	if s==[]:
    	    s.append(-1)
        return s
n=int(input())
arr=[1,2,3,4,2,4]
ob=Solution()
print(ob.duplicates(arr,n))

#TC:O(N^2)
#SC:O(1)
