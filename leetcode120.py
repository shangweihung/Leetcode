class Solution:
    def minimumTotal(self, triangle):

        num_of_rows=len(triangle)
        dp=triangle[-1]
        
        for i in range(num_of_rows-2,-1,-1):   
            for j in range(i+1):
                dp[j]=triangle[i][j]+min(dp[j],dp[j+1])
                
        return dp[0]

if __name__ == "__main__":
    print( Solution().minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]) == 11)
