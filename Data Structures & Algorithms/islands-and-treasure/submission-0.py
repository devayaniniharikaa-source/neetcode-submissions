class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        q=deque()
        path=set()
        def bfs(r,c):
            if r<0 or c<0 or r==rows or c==cols or (r,c) in path or grid[r][c]==-1:
                return
            path.add((r,c))
            q.append([r,c])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append([r,c])
                    path.add((r,c))
        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            dist+=1