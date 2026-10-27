class Solution:
    def isValid(self, s: str) -> bool:
        seen={"{":"}","[":"]","(":")"}

        stack=[]
        for i in s:
            if i in seen:
                stack.append(i)
            elif stack and i==seen[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack
        