class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ser=set()
        for i in nums:
            if i in ser:
                return True
            ser.add(i)
        return False

        