class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen={}
        for i in s:
            seen[i]=seen.get(i,0)+1
        seen2={}
        for i in t:
            seen2[i]=seen2.get(i,0)+1
        if seen==seen2:
            return True
        return False

        