class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo={}

        def backtrack(i,j):

            if j==len(t):
                return 1

            if i== len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            formas = backtrack(i + 1, j)  # Saltar s[i]

            if s[i] == t[j]:
                formas += backtrack(i + 1, j + 1)  # Usar s[i]

            memo[(i, j)] = formas
            return formas
        return backtrack(0,0)
            
        