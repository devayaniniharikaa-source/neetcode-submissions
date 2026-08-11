class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap={i:[] for i in range(numCourses)}
        for crs,prev in prerequisites:
            premap[crs].append(prev)
        res=[]
        cycle,visit=set(),set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for prev in premap[crs]:
                if dfs(prev)==False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c)==False:
                return []
        return res
