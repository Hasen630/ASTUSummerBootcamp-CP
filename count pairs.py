class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        l=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j and nums[i]+nums[j]<target:
                    l+=1
        return(l)
