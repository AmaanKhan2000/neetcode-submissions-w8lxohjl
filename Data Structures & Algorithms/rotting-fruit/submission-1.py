class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        fresh = [0]


        def bfs(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLS or (r,c) in visit or grid[r][c]!=1:
                return 
            else:
                visit.add((r,c))
                q.append([r,c])
                fresh[0]-=1
                    

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh[0]+=1
                if grid[i][j] == 2:
                    visit.add((i,j))
                    q.append([i,j])           

        minutes = 0
        while q and fresh[0]>0:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                bfs(r+1,c)
                bfs(r,c+1)
                bfs(r,c-1)
                bfs(r-1,c)
            minutes+=1
        return minutes if fresh[0] == 0 else -1
     



        