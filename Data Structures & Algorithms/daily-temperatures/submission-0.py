class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        stack=[]
        for i in range(len(nums)):
            while stack and nums[i]>stack[-1][0]:
                result[stack[-1][1]]= i-stack[-1][1]
                stack.pop()
            stack.append((nums[i],i))

        return result