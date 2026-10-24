class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp={} #(index, total) --> #of ways
        

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp: #Si ya hemos pasado por este caso
                return dp[(i, total)]
            #camino donde pongo el mas
            #camino donde pongo el menos
            dp[(i, total)]= (backtrack(i+1,total+nums[i]) +
                                backtrack(i+1, total- nums[i]))
            return dp[(i,total)]
        return backtrack(0,0)
        

                    

            

        