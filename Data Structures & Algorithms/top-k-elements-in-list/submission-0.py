class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        
        for i in nums:
            freq[i]=freq.get(i,0)+1
        res=sorted(freq, key=freq.get, reverse=True)
        return res[:k]
        