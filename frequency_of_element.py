def findFrequency (arr, n, x):
    count=0
    for i in range(len(arr)):
        if(arr[i]==x):
            count+=1
    return count;

#TC: O(n)
#SC=O(1)
