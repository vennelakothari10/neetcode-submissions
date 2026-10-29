from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<k:
            return []
        q=deque()
        ans=[]

        for i in range(len(nums)):
            while q and q[0]<=i-k:
                q.popleft()
            while q and nums[q[-1]]<=nums[i]:
                q.pop()
            q.append(i)
            if i>=k-1:
                ans.append(q[0])
        
        return [nums[i] for i in ans]

        