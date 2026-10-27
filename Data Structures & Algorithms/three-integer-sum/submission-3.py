class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            l=k+1
            r=len(nums)-1
            summ=0
            while(l<r):
                summ=nums[k]+nums[l]+nums[r]
                if(summ>0):
                    r-=1
                elif summ<0:
                    l+=1
                else:
                    res.append([nums[k],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1 
        return res