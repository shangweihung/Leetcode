class Solution(object):
    def reverseVowels(self, s):

        left,right=0,len(s)-1
        vowels=['a','e','i','o','u','A','E','I','O','U']
        s=list(s)
        

        while left<=right:
            while s[left] not in vowels and left<right:
                left+=1
            while s[right] not in vowels and left<right:
                right-=1
      
            s[left],s[right]=s[right],s[left]
            left,right=left+1,right-1
        
        return ''.join(s)


if __name__=='__main__':
    print(Solution().reverseVowels('leetcode')=='leotcede')
