class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums2)<len(nums1):
            nums1,nums2 = nums2,nums1

        #nums1 is smaller or they are the same

        a=len(nums1)
        b=len(nums2)

        m=(a+b)//2

        l=-1
        r=a-1

        while l<=r:
            i=(l+r)//2
            j=m-i-2

            aleft = nums1[i] if i>=0 else float("-inf")
            aright = nums1[i+1] if (i+1)<a else float("inf")
            bleft = nums2[j] if j>=0 else float("-inf")
            bright = nums2[j+1] if (j+1)<b else float("inf")

            if aleft<=bright and bleft<=aright:
                if (a+b)%2:
                    return min(aright,bright)
                else:
                    return (max(aleft,bleft)+min(aright,bright))/2
            
            if aleft>bright:
                r=i-1
            else:
                l=i+1
            














        