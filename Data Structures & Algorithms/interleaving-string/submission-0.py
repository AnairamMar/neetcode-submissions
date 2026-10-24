class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}  # (i, j) -> ¿podemos completar s3 desde aquí?

        def backtrack(i, j):
            if i == len(s1) and j == len(s2):
                return True

            if (i, j) in dp:
                return dp[(i, j)]

            # Intentar tomar la siguiente letra de s1
            if i < len(s1) and s1[i] == s3[i + j]:
                if backtrack(i + 1, j):
                    dp[(i, j)] = True
                    return True

            # Intentar tomar la siguiente letra de s2
            if j < len(s2) and s2[j] == s3[i + j]:
                if backtrack(i, j + 1):
                    dp[(i, j)] = True
                    return True

            dp[(i, j)] = False
            return False

        return backtrack(0, 0)