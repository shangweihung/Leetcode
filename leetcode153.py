class Solution(object):
    def findMin(self, nums):
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<nums[right]:
                right=mid
            else:
                left=mid+1
        return nums[left]



if __name__=="__main__":
    print( Solution().findMin([4,5,6,7,0,1,2])==0)
    print( Solution().findMin([3,4,5,1,2])==1)
