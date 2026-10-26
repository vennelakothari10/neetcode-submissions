from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket=[[] for i in range(len(nums)+1)]
        seen=Counter(nums)
        for i,j in seen.items():
            bucket[j].append(i)
        ans=[]
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans
                



        