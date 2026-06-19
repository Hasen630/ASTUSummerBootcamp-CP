class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wind=sum(nums[:k])
        maxi=wind
        left=0
        for right in range(k,len(nums)):
            wind-=nums[left]
            wind+=nums[right]
            maxi=max(maxi,wind)
            left+=1
        return(maxi/k)    



        
