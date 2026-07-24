class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i, cur, summ):
            if summ==target:
                res.append(cur.copy())
                return
            if i>=len(nums) or summ>target:
                return
            cur.append(nums[i])
            dfs(i, cur, summ+nums[i])
            cur.pop()
            dfs(i+1, cur, summ)
        dfs(0,[],0)
        return res 
        
            