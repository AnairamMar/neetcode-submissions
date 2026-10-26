class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = [[0] *COLS for _ in range(ROWS)]
        res=0
        def dfs(r, c):
           
            if memo[r][c] > 0:
                return memo[r][c]

            longestPath = 1  # La celda actual cuenta como un paso

            # Abajo
            if r + 1 < ROWS and matrix[r + 1][c] > matrix[r][c]:
                longestPath = max(longestPath, 1 + dfs(r + 1, c))

            # Arriba
            if r - 1 >= 0 and matrix[r - 1][c] > matrix[r][c]:
                longestPath = max(longestPath, 1 + dfs(r - 1, c))

            # Derecha
            if c + 1 < COLS and matrix[r][c + 1] > matrix[r][c]:
                longestPath = max(longestPath, 1 + dfs(r, c + 1))

            # Izquierda
            if c - 1 >= 0 and matrix[r][c - 1] > matrix[r][c]:
                longestPath = max(longestPath, 1 + dfs(r, c - 1))

            memo[r][c] = longestPath
            return longestPath

        for r in range(ROWS):
            for c in range(COLS):
                current=dfs(r,c)
                res=max(res,current)
        return res
