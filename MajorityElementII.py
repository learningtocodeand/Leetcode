
class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        m=n//2
        d={}
        maxcount=0
        maxele=0
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
                
            if d[i]>=m and d[i]>maxcount:
                maxcount=d[i]
                maxele=i

        return maxele
        