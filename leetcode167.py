#solution1: (hashmap)
class Solution1(object):
    def twoSum(self, numbers, target):

        hashtable={}
        for i,element in enumerate(numbers):
            if element in hashtable:
                return [hashtable[element]+1,i+1] #not zero-based
            save=target-element
            hashtable[save]=i
if __name__=='__main__':
    print(Solution1().twoSum([2,7,11,15],9)==[1,2])
            
#solution2: (Two Pointers)
class Solution2(object):
    def twoSum(self, numbers, target):
        left,right=0,len(numbers)-1
        while left<right:
            s=numbers[left]+numbers[right]
            if s==target:
                return [left+1,right+1]
            elif s>target:
                right-=1
            else: #s<target
                left+=1
if __name__=='__main__':
    print(Solution2().twoSum([2,7,11,15],9)==[1,2])
