class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l=1
        r = max(piles)
        

        while l<=r:
            m=(l+r)//2
            rate=0
            for i in piles:
                rate+= (i+m-1)//m
            if rate<=h:
                r=m-1
            else:
                l=m+1
        return l



        