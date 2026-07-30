class Solution:
    def partition(self, s: str) -> List[List[str]]:
        stack=[]
        res=[]
        def dfs(i):
            if i>=len(s):
                res.append(stack.copy())
            for j in range(i,len(s)):
                if self.parti(s,i,j):
                    stack.append(s[i:j+1])
                    dfs(j+1)
                    stack.pop()
        dfs(0)
        return res
    def parti(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l,r=l+1,r-1
        return True