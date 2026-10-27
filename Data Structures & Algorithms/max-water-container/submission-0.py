class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0
        current_water=0

        l=0
        r=len(heights)-1

        while l<r:
            current_water=(r-l)*(min(heights[r],heights[l]))
            max_water=max(max_water,current_water)
            if heights[r]>heights[l]:
                l+=1
            else:
                r-=1
        return max_water

        