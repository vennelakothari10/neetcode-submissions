class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums=sorted(nums)
        max_total=1
        total=1
        
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1 :
                total+=1
                max_total=max(max_total,total)
            elif nums[i]==nums[i-1]:
                continue
            else:
                total=1
        return max_total

        