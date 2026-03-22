import heapq
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        pq= []
        row = len(grid)
        col = len(grid[0])

        #start condition
        if grid[0][0]==1:
            return -1
        #distnce matrix
        dist = [[1e9]*col for _ in range(row)]
        dist[0][0] = 0
        dx=[-1,1,0,0,-1,1,-1,1]
        dy=[0,0,1,-1,-1,1,1,-1]

        #appending source node 1st
        heapq.heappush(pq,(0,(0,0)))
        minPath = 1e9
        while pq:
            dis, points = heapq.heappop(pq)
            x,y = points
            if(x== row-1 and y == col-1):
                minPath = min(dis,minPath)

            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]

                if 0<= nx < row and 0<= ny < col and grid[nx][ny] == 0 and dis+1<dist[nx][ny]:
                    dist[nx][ny] = dis+1
                    heapq.heappush(pq,(dist[nx][ny],(nx,ny)))

        if minPath!= 1e9:
            return minPath+1
        else :
            return -1
