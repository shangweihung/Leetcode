class Solution:
    def isIsomorphic(self, s, t):
        mapping={}
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] not in mapping.values():
                    mapping[s[i]]=t[i]
                else:
                    return False
        for i in range(len(t)):
            if mapping[s[i]]!=t[i]:
                return False
        return True


if __name__=='__main__':
    assert Solution().isIsomorphic('paper','title')==True
    assert Solution().isIsomorphic('egg','add')==True
    assert Solution().isIsomorphic('aa','ab')==False
    assert Solution().isIsomorphic('ab','aa')==False
