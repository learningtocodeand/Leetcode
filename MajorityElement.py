class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m=len(nums)//3
        d={}
        ans=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
            if(d[i]>m  ):
                ans.append(i)
                d[i]=-99
        return ans