class Solution:
    def fourSum(self, nums, target):
        result=set()     #use set to ignore repeating results
        mem_set={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] in mem_set:
                    mem_set[nums[i]+nums[j]].append((i,j))
                else:
                    mem_set[nums[i]+nums[j]]=[(i,j)]
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                goal=target-(nums[i]+nums[j])
                if goal in mem_set:
                    
                    for index in mem_set[goal]:
                       # Ingore repeating results
                        if index[0] > j:
                            result.add(tuple(sorted([nums[i], nums[j], nums[index[0]], nums[index[1]]])))
        result=[list(l) for l in result]
        return result


if __name__ == "__main__":
    assert Solution().fourSum([1, 0, -1, 0, -2, 2], 0) == [[-1, 0, 0, 1], [-2, 0, 0, 2], [-2, -1, 1, 2]]
