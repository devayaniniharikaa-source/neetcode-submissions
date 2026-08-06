class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pat,alt=set(),set()
        def ocean(r,c,visit,prevheight):
            if (r<0 or c<0 or r==rows or c==cols or (r,c) in visit or heights[r][c]<prevheight):
                return
            visit.add((r,c))
            ocean(r+1,c,visit,heights[r][c])
            ocean(r-1,c,visit,heights[r][c])
            ocean(r,c+1,visit,heights[r][c])
            ocean(r,c-1,visit,heights[r][c])
        for c in range(cols):
            ocean(0,c,pat,heights[0][c])
            ocean(rows-1,c,alt,heights[rows-1][c])
        for r in range(rows):
            ocean(r,0,pat,heights[r][0])
            ocean(r,cols-1,alt,heights[r][cols-1])
        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in alt and (r,c) in pat:
                    res.append([r,c])
        return res