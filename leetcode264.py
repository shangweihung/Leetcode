class Solution:
    def nthUglyNumber(self, n):
        dp=[1]
        i2=i3=i5=0
        
        while len(dp)<n:
            MIN=min(dp[i2]*2,dp[i3]*3,dp[i5]*5)
            #紀錄每一個ugly number分別乘以2 3 5取最小值
            if MIN==dp[i2]*2:
                i2+=1
            if MIN==dp[i3]*3:
                i3+=1
            if MIN==dp[i5]*5:
                i5+=1
            dp+=[MIN]

        
        return dp[-1]

if __name__=="__main__":
    print(Solution().nthUglyNumber(10)==12)
