class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        buc=[[] for _ in range(len(nums)+1)]
        for n,c in freq.items():
            buc[c].append(n)
        res=[]
        for i in range(len(buc)-1,0,-1):
            for n in buc[i]:
                res.append(n)
            if(len(res)==k):
                return res

        