class Solution:
    def sortArr(self, arr, n): 
        counter=1
        temp=0
        while counter<=n-1:
            for i in range(0,len(arr)-1):
                    if arr[i]>arr[i+1]:
                        temp=arr[i]
                        arr[i]=arr[i+1]
                        arr[i+1]=temp
                    else:
                        arr[i]=arr[i]
            counter+=1
        return arr;
if __name__=='__main__':
        n=int(input())
        arr=[1,5,2,3,5,9,100,23,45,21,32,67]
        obj=Solution()
        ans=obj.sortArr(arr,n)
        for i in ans:
            print(i,end=" ")
        print()

#Time Complexity - O(n^2)
#Space Complexity - O(1)

#Best solution in terms of code and feasibility for sorting the array in asc
class Solution:
    def sortArr(self, arr, n): 
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:
                    arr[i],arr[j]=arr[j],arr[i]
        return arr;
   if __name__=='__main__':
        n=int(input())
        arr=[1,5,2,3,5,9,100,23,45,21,32,67]
        obj=Solution()
        ans=obj.sortArr(arr,n)
        for i in ans:
            print(i,end=" ")
        print()
#TC: O(n^2)
#SC:O(1)
  
#Solution using sorted function - Better one in terms of complexity :)
class Solution:
    def sortArr(self, arr, n): 
        return sorted(arr);
if __name__=='__main__':
        n=int(input())
        arr=[1,5,2,3,5,9,100,23,45,21,32,67]
        obj=Solution()
        ans=obj.sortArr(arr,n)
        for i in ans:
            print(i,end=" ")
        print()
#Time Complexity: O(nLogn) → Improved
#Space Complexity: O(1)


