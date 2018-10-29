from collections import defaultdict
#leetcode 269
class Solution(object):
    def AlienDict(self,words):
        if len(words)==0:
            return ''

        indegree={}
        hashmap=defaultdict(list)
        print(words)
        for w in words:
            for ch in w:
                indegree[ch]=0;
        

        for i in range(1,len(words)):
            k=0
            while words[i-1][k]==words[i][k]:
                k+=1
            if k>= len(words[i-1]) or k>=len(words[i]):
                continue
            indegree[words[i][k]]+=1
            hashmap[words[i-1][k]].append(words[i][k])
  

        ans=''

        for i in indegree.keys():
            ch=''
            for j in indegree.keys():
                if indegree[j]==0:
                     ch=j
                     break

            if ch=='':  #means no indegree 0
                return ''

            ans+=ch
            indegree[ch]-=1

            for k in hashmap[ch]:
                indegree[k]-=1


        return ans

                     
if __name__ == "__main__":
    print( Solution().AlienDict(["wrt","wrf","er","ett","rftt"])=="wertf")
    print( Solution().AlienDict(["ra","rcc","b","abb","abc"])=="rbac")

