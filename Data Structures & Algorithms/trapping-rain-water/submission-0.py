class Solution:
    def trap(self, nums: List[int]) -> int:
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










            
                



        