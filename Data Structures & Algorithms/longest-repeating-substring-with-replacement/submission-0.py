class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen={}
        left=0
        right=0
        max_length=0
        for i in range(len(s)):
            seen[s[i]]=seen.get(s[i],0)+1
            curr_len = (right-left+1)
            curr_max_freq = max(seen.values())
            if curr_len - curr_max_freq <= k:
                max_length=max(max_length,curr_len)
            else:
                seen[s[left]]-=1
                left+=1
            right+=1
        
        return max_length




        