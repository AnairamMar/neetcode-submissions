class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp={} #(index, total) --> #of ways
        

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp: #Si ya hemos pasado por este caso
                return dp[(i, total)]
            formas_si_sumo = backtrack(i + 1, total + nums[i])
            formas_si_resto = backtrack(i + 1, total - nums[i])

            dp[(i, total)] = formas_si_sumo + formas_si_resto
            return dp[(i,total)]
        return backtrack(0,0)
        

                    

            

        