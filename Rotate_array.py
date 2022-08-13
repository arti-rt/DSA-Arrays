#Rotate an array cyclically based on a given a rotation number.
def rotate(arr, n):
    temp=arr[0:n-1]
    temp1=[]
    temp1.append(arr[-1])
    a=temp1+temp
    return a
        
n=int(input())
arr=[1,2,4,3,5,7]
print(rotate(arr,n))

Tc: Log
SC:O(1)
