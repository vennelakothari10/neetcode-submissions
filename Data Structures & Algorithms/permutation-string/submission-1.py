class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = {}
        count2 = {}

        for c in s1:
            count1[c] = count1.get(c, 0) + 1

        left = 0

        for right in range(len(s2)):
            c = s2[right]
            count2[c] = count2.get(c, 0) + 1

            if right - left + 1 > len(s1):
                old = s2[left]
                count2[old] -= 1

                if count2[old] == 0:
                    del count2[old]

                left += 1

            if count1 == count2:
                return True

        return False

        