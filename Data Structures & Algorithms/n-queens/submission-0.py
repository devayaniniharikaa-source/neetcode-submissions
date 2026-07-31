class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        pdig=set()
        ndig=set()
        res=[]
        board=[["."]*n for i in range(n)]
        def dfs(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in pdig or (r-c) in ndig:
                    continue
                col.add(c)
                pdig.add(r+c)
                ndig.add(r-c)
                board[r][c]="Q"
                dfs(r+1)
                col.remove(c)
                pdig.remove(r+c)
                ndig.remove(r-c)
                board[r][c]="."
        dfs(0)
        return res
