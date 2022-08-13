#Solution 1- Finding Kth Smallest element in the array
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        a=sorted(arr)
        return a[k-1]
#Time Complexity : O(nLogn) → Nice, can try for O(n)
#Space Complexity : O(1)

#Solution 2- 
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
      '''
        for i in range(len(arr)):
                  for j in range(i+1,len(arr)):
                      if arr[i]>arr[j]:
                          arr[i],arr[j]=arr[j],arr[i]
        return arr[k-1];
   
#TC: O(n^2)
#SC: O(1)
