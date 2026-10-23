class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = [[0] * (n + 1) for _ in range(amount + 1)]
        dp[0] = [1] * (n + 1)

        for a in range(1, amount + 1):
            for i in range(n - 1, -1, -1):
                # No usar esta denominación
                dp[a][i] = dp[a][i + 1]

                # Usar una moneda de esta denominación
                if a >= coins[i]:
                    dp[a][i] += dp[a - coins[i]][i]

        return dp[amount][0]