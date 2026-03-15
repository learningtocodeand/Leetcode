from collections import deque
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        v= len(graph)
        parent = [[] for _ in range(v)]
        outdegree = [0]*v
        for i in range (v):
            l=graph[i]
            if l:
                for j in l:
                    parent[j].append(i)
                    outdegree[i]+=1
            else:
                outdegree[i]=0
        queue=deque()

        for i in range(v):
            if outdegree[i]==0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            ans.append(node)

            for i in parent[node]:
                outdegree[i]-=1
                if outdegree[i]==0:
                    queue.append(i)

        return sorted(ans)


            
