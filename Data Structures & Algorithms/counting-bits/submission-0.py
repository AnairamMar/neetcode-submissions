class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        
        for i in range(n + 1):
            m = ans[i // 2]
            if i%2 == 0:
                ans[i]=m
            else:
                ans[i]=m+1
            

        return ans
                 


        