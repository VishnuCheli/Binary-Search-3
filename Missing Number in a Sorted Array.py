def findMissingNumber(arr):
    low=0
    high=len(arr)-1
    
    if arr[0]!=1:
        return 1
    
    if (arr[-1]==len(arr)):
        return (len(arr)+1)
    
    while low+1!=high:
        mid=low+(high-low)//2
        
        if(arr[mid]-mid)==1:
            low=mid
        else:
            high=mid
            
    return arr[low]+1

print(findMissingNumber([1,2,3,5,6,7,8,9]))