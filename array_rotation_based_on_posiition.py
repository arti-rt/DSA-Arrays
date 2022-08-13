#Array Rotation, based on a specified position d
def arrayrotate(d,arr):
    temp=arr[d:]
    temp1=arr[0:d]
    temp.extend(temp1)
    return temp
d=int(input())
arr=[1,2,4,5,3,7,8]
print(arrayrotate(d,arr))

#TC: O(nlogn)
#SC: O(1)
