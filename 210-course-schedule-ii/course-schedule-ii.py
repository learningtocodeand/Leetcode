from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        l=[]
        adj=[[] for _ in range(numCourses) ]
        indegree = [0]*numCourses

        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u]+=1
        queue  =deque()
        for i in range (numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            l.append(node)

            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)

        if len(l) == numCourses:
            return l
        else :
            return []