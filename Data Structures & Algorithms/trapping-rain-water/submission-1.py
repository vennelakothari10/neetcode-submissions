class Solution:
    def trap(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        maxleft=0
        maxright=nums[-1]
        area=0

        while l<r:
            if nums[l]<=nums[r]:
                maxleft=max(maxleft,nums[l])
                area+= maxleft-nums[l]
                l+=1
            elif nums[l]>nums[r]:
                maxright=max(maxright,nums[r])
                area+= maxright-nums[r]
                r-=1
        return area

















        """
        left=[0]*len(nums)
        right=[0]*len(nums)
        maxleft=0
        maxright=0
        area=0
        for i in range(len(nums)):
            left[i]=maxleft
            maxleft=max(maxleft,nums[i])
        for i in range(len(nums)-1,-1,-1):
            right[i]=maxright
            maxright=max(maxright,nums[i])
        
        for i in range(len(nums)):
            val=min(left[i],right[i]) - nums[i]
            if val>0:
                area+=val
        return area
"""
            
                



        