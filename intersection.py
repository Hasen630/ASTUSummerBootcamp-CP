class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        y=set(nums1)
        x=set(nums2)
        for i in x:
            if i in y:
                l.append(i)
        return(l)
