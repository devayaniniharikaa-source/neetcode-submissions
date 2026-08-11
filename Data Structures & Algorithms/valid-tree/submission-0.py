class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        premap={i:[] for i in range(n)}
        for crs,prev in edges:
            premap[crs].append(prev)
            premap[prev].append(crs)
        visit=set()
        def dfs(i,pre):
            if i in visit:
                return False
            visit.add(i)
            for j in premap[i]:
                if j == pre:
                    continue
                if not dfs(j,i):
                    return False
            return True
        return dfs(0,-1) and n==len(visit)
        
        