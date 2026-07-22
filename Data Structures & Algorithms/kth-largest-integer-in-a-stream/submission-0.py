class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heeap,self.k=nums,k
        heapq.heapify(self.heeap)
        while len(self.heeap)>k:
            heapq.heappop(self.heeap)
    def add(self, val: int) -> int:
        heapq.heappush(self.heeap,val)
        while len(self.heeap)>self.k:
            heapq.heappop(self.heeap)
        return self.heeap[0]
        
        
