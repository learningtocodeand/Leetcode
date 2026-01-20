class Solution(object):
    def countPairs(self, nums, low , mid, high):
        left=low
        right = mid+1

        while(left<=mid):
            while(right<=high and nums[left]>nums[right]*2):
                right = right+1
            self.count+= (right-(mid+1))
            left+=1
        

    def merge(self, nums,low,mid,high):
        temp=[]
        left=low
        right=mid+1

        while(left<=mid and right <= high):
            if(nums[left]<=nums[right]) :
                temp.append(nums[left])
                left=left+1
            else:
                temp.append(nums[right])
                right=right+1
        while(left<=mid):
            temp.append(nums[left])
            left=left+1
        while(right<=high):
            temp.append(nums[right])
            right=right+1

        k=0
        for i in range(low,high+1):
            if(k<len(temp)):
                nums[i]=temp[k]
                k=k+1


    def mergesort(self, nums, low, high):
        if(low>=high):
            return
        mid=(low+high)//2

        self.mergesort(nums,low,mid)
        self.mergesort(nums,mid+1,high)
        self.countPairs(nums,low,mid,high)
        self.merge(nums,low,mid,high)

    def reversePairs(self, nums):
        self.count = 0
        
        low=0
        high=len(nums)-1

        self.mergesort(nums,low,high)
        return self.count
    
        