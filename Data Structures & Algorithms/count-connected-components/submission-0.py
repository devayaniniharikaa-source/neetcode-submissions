class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        premap={i:[] for i in range(n)}
        visit=[False]*n
        for crs,prev in edges:
            premap[crs].append(prev)
            premap[prev].append(crs)
        def dfs(node):
            q=deque([node])
            visit[node]=True
            while q:
                cur=q.popleft()
                for j in premap[cur]:
                    if not visit[j]:
                        visit[j]=True
                        q.append(j)
        count=0
        for node in range(n):
            if not visit[node]:
                dfs(node)
                count+=1
        return count

                
                
