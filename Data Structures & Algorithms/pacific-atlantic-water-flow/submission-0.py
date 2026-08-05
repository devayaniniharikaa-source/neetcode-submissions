class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        alt,pac=set(),set()
        def ocean(r,c,visit,prevheight):
            if (r<0 or c<0 or r==rows or c==cols or (r,c) in visit or heights[r][c]<prevheight):
                return
            visit.add((r,c))
            ocean(r+1,c,visit,heights[r][c])
            ocean(r-1,c,visit,heights[r][c])
            ocean(r,c+1,visit,heights[r][c])
            ocean(r,c-1,visit,heights[r][c])
        for c in range(cols):
            ocean(0,c,pac,heights[0][c])
            ocean(rows-1,c,alt,heights[rows-1][c])
        for r in range(rows):
            ocean(r,0,pac,heights[r][0])
            ocean(r,cols-1,alt,heights[r][cols-1])
        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in alt and (r,c) in pac:
                    res.append([r,c])
        return res
