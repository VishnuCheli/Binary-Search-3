class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums=nums;
        self.target=target;
        first=self.binarySearch(True)#search for first index with target
        last=self.binarySearch(False)#search for last index with target
        return[first,last]
    
    def binarySearch(self,LeftFlag): 
        index=-1
        low=0;
        high=len(self.nums)-1
        while(low<=high):
            mid=low+(high-low)//2
            
            if(self.nums[mid]==self.target):#after finding the element find the first and last indexes
                index=mid
                if LeftFlag:
                    high=mid-1
                else:
                    low=mid+1
                    
            elif(self.nums[mid]<self.target):
                low=mid+1
            else:
                high=mid-1
                
        return index
        