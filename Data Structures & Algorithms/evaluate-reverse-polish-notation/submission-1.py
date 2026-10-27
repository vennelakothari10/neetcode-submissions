class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        val=0
        operation=("*","+","-","/")
        for i in tokens:
            if i not in operation:
                stack.append(int(i))
            else:
                op=i
                b=stack.pop()
                a=stack.pop()
                if op=="+":
                    stack.append(a+b)
                elif op=="-":
                    stack.append(a-b)
                elif op=="*":
                    stack.append(a*b)
                elif op=="/":
                    stack.append(int(a/b))
        return stack[-1]

        