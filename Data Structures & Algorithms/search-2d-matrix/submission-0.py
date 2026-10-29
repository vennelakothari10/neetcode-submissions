class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)#rows
        n=len(matrix[0])#cols
        for i in range(m):
            l=0
            r=n-1
            while l<=r:
                m=(l+r)//2
                if matrix[i][m]==target:
                    return True
                elif matrix[i][m]<target:
                    l=m+1
                else:
                    r=m-1
        return False

