class Solution:
    def isUgly(self, num):
        if num<=0:
            return False
        if num<6:
            return True
        for x in [2,3,5]:
            while num%x==0:
                num/=x
        return True if num==1 else False

if __name__=="__main__":
    print(Solution().isUgly(6)==True)
    print(Solution().isUgly(14)==False)
