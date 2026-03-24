from collections import deque
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        adj = [[] for _ in range(n)]

        for i in flights:
            adj[i[0]].append((i[1],i[2]))
        
        dist = [1e9]*n

        dist[src] = 0

        queue = deque()
        queue.append((0,src,0))

        while queue:
            stops,node,dis = queue.popleft()
            if stops>k:
                continue
            for v,wt in adj[node]:
                if(dis+wt<dist[v]):
                    dist[v]=dis+wt
                    queue.append((stops+1,v,dist[v]))

        return -1 if dist[dst] == 1e9 else dist[dst] 