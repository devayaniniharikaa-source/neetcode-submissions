class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has={}
        for i,n in enumerate (nums):
            rem=target-nums[i]
            if(rem in has):
                return [has[rem],i]
            has[n]=i
        return
                