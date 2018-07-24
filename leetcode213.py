class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        length=len(nums)
        if length<=3:
            return max(nums)
        else:
            return max(self.rob_recur(nums[:-1]),self.rob_recur(nums[1:]))
            
    def rob_recur(self,nums):
        length=len(nums)
        dp=[0]*length
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        
        for i in range(2,length):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i]) 
        
        return dp[-1]

if __name__=="__main__":
    print(Solution().rob([1,2,3,1])==4)
    print(Solution().rob([2,3,2])==3)
