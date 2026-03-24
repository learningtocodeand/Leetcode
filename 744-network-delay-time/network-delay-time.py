import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u,v,w in times:
            adj[u-1].append((v-1,w))
        dist = [1e9]*n

        dist[k-1] = 0

        pq = []
        # cost, node
        heapq.heappush(pq,(0,k-1))

        while pq:
            cost,node = heapq.heappop(pq)
            if cost>dist[node]:
                continue
            for v,wt in adj[node]:
                newcost = cost+wt

                if newcost< dist[v]:
                    dist[v]=newcost
                    heapq.heappush(pq,(newcost,v))
        if 1e9 not in dist:
            return max(dist)
        else :
            return -1