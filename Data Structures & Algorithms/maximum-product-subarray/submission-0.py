class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        curmax=1
        curmin=1
        for num in nums:
            tmp=num*curmax
            curmax=max(num*curmax,num*curmin,num)
            curmin=min(tmp,num*curmin,num)
            res=max(res,curmax)
        return res


            