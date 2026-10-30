class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=len(nums1)
        j=len(nums2)
        m=((i+j)//2)+1
        # m==odd take the prev element as well, for even dont

        arr=[]
        l1=0
        l2=0
        ans=0.0

        while l1<i and l2<j and len(arr)<m:
            if nums1[l1] <= nums2[l2]:
                arr.append(nums1[l1])
                l1+=1
            else:
                arr.append(nums2[l2])
                l2+=1
        while len(arr)<m and l1!=i:
            arr.append(nums1[l1])
            l1+=1
        
        while len(arr)<m and l2!=j:
            arr.append(nums2[l2])
            l2+=1
        
        if (i + j) % 2 == 1:
            return float(arr[-1])
        else:
            return (arr[-1] + arr[-2]) / 2


        

        

        