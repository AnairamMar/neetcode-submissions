class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj={i:[] for i in range(n)}
        visited= set()
        resp=0

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(i):

            if i in visited:
                return
            visited.add(i)
            for nei in adj[i]:
                if nei in visited:
                    continue
                
                dfs(nei)
        for i in adj:
            if i not in visited:
                resp+=1
                dfs(i)
        return resp