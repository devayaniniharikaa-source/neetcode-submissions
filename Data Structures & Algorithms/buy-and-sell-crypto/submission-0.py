class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        res=prices[0]
        for r in prices:
            l=max(l,r-res)
            res=min(res,r)
        return l

        