class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]
        k=[]
        j=[]
        for i in nums:
            if i<pivot:
                l.append(i)
            elif i==pivot:
                k.append(i)
            else:
                j.append(i)
        return(l+k+j)

            

        
